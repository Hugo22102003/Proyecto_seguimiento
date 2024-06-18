from flask import Flask, flash, render_template, url_for, request
from flask_migrate import Migrate
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
from flask_sqlalchemy import SQLAlchemy 
from models import   Solicitud, Empresa, Ususario, Solicitante, Departamento, Asignar, AsigDepar
from forms import   SolicitudForm, EmpresaForm, UsuarioForm, LoginForm, SolicitanteForm, DepartamentoForm,  AsginarForm, AsigDeparForm
from flask_login import login_required, UserMixin, current_user, LoginManager, login_user, logout_user
from models import Solicitud
app = Flask(__name__)

# Configuracion de la base de datos 
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'pasantia_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQL_TRACK_MODIFICATIONS'] = False

#Incializacion del obejto db
db.init_app(app)

#Configurar Flask Migrate 
migrate = Migrate()
migrate.init_app(app, db)

#* Configuracion de flask-wtf
app.config['SECRET_KEY'] = 'NO.'

#* Configuracion del login de flask
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return Ususario.query.get(int(user_id))



@app.route("/inicio")
@login_required
def inicio():
    asignaciones = Asignar.query.all()
    return render_template('inicio.html', asignaciones = asignaciones)








#@app.route("/", methods = ["GET", "POST"])
#def login():
#    loginForm = LoginForm()
#    if loginForm.validate_on_submit():
#        user = Ususario.query.filter_by(username = loginForm.username.data).first()
#        if user:
#            # * Revisar el hash
#            if check_password_hash(user.password_hash, loginForm.password.data):
#                login_user(user)
#                flash("Ha inicido sesion correctamente")
#                return redirect(url_for("inicio"))
#            else:
#                flash("Contraseña incorrecta, Intente nuevamente")
#        else:
#            flash("Ese usuario no existe, intenta nuevamente")

#    return render_template("login.html", loginForm=loginForm)





@app.route("/adminprueba", methods = ["GET", "POST"])
@login_required
def admin():
    id = current_user.id
    if id == 11:
        return render_template("adminprueba.html")
    else: 
        flash("Esta funcion es lo para el administrador")
        return redirect(url_for("inicio"))



@app.route("/mostrar", methods = ["GET", "POST"])
@login_required
def mostrar():
    solicitudes = Solicitud.query.order_by("numero")
    departamentos = AsigDepar.query.order_by("id")
    #empleados= Asignar.query.order_by("id")
    total_solicitudes = Solicitud.query.count()
    return render_template("mostrar.html",solicitudes = solicitudes, total_solicitudes = total_solicitudes)

@app.route("/mostrar2", methods = ["GET", "POST"])
@login_required
def mostrar2():
    departamentos = AsigDepar.query.order_by("id")
    return render_template("mostrar2.html", departamentos = departamentos)

@app.route("/mostrar3", methods = ["GET", "POST"])
@login_required
def mostrar3():
    empleados = Asignar.query.order_by("id")
    return render_template("mostrar3.html", empleados = empleados)
    


@app.route("/todo", methods = ["GET", "POST"])
@login_required
def todo():
    id = current_user.id
    asignaciones = Asignar.query.filter_by(usuario_id = id).all()
    return render_template("todo.html", asignaciones = asignaciones)

@app.route("/estado/<int:id>", methods = ["GET", "POST"])
@login_required
def estado(id):
    asignar = Asignar.query.get_or_404(id)
    form = AsginarForm()
    if request.method == "POST":
        asignar.estado = request.form["estado"]
        try:
            db.session.commit()
            flash("Estado cambiado exitosamente")
            return render_template("estado.html", asignarForm = form, asignar = asignar)
        except:
            flash("Ocurrio un error intenta nuevament")
            return render_template("estado.html", asignarForm = form, asignar = asignar)
    else:
        return render_template("estado.html", asignarForm= form, asignar = asignar)
    
@app.route("/detalle/<int:id>)", methods = ["GET", "POST"])
def detalle(id):
    asignacion = Asignar.query.get_or_404(id)
    
    return render_template("ver.html", asignacion = asignacion)

@app.route("/analizar/<int:id>", methods = ["GET","POST"])
def analizar(id):
    asignar = Asignar.query.get_or_404(id)
    return render_template("ver.html", asignar = asignar)

@app.route("/logout", methods = ["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("Has cerrado sesion")
    return redirect(url_for("login"))

@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template("404.html" )

@app.errorhandler(500)
def error_en_servidor(e):
    return render_template("500.html")

@app.route("/prueba", methods = ["GET", "POST"])
def prueba():
    usuarios = Ususario.query.all()
    return render_template("prueba.html", usuarios = usuarios)

@app.route("/solicitante2", methods = ["GET", "POST"])
@login_required
def solcitante2():

    if request.method == "POST":
        try:
            ci = request.form.get("cedula")
            nombre = request.form.get("nombre")
            tipo= request.form.get("tipo")
            direccion = request.form.get("direccion")
            telefono = request.form.get("telefono")
        
            solicitante = Solicitante(nombre = nombre, tipo = tipo, ci = ci, direccion = direccion, telefono = telefono)
            db.session.add(solicitante)
            db.session.commit()
            return render_template("solicitante2.html")
        except:
            flash("Ocurrio nun error intenta nuevamente")
            return render_template("solicitante2.html")
    return render_template("solicitante2.html")

@app.route("/asignar2", methods = ["GET", "POST"])
@login_required
def asignar2():
    departamentos = Departamento.query.all()
    usuarios = Ususario.query.order_by(Ususario.nombre)
    solicitudes = Solicitud.query.order_by(Solicitud.numero)
    if request.method == "POST":
        departamento = request.form.get("departamento")
        usuario = request.form.get("usuario")
        solicitud = request.form.get("solicitud")
        password = request.form.get("password")
        user = Ususario.query.filter_by(id = usuario).first()

        if user:
            if check_password_hash(user.password_hash, password):

                asignar = Asignar(depertamento_id = departamento, usuario_id = usuario, solicitud_id = solicitud)
                db.session.add(asignar)
                db.session.commit()
                return render_template("asignar2.html", departamentos = departamentos, usuarios = usuarios, solicitudes = solicitudes)
            else:
                print("contraseña incorrecta")
        else: 
            print("El usuario no existe")

    return render_template("asignar2.html", departamentos = departamentos, usuarios= usuarios, solicitudes = solicitudes)

@app.route("/departamento_nuevo", methods=["GET","POST"])
@login_required
def departamentoNuevo():
    if request.method == "POST":
        nombre = request.form.get("departamento")
        departamento = Departamento(nombre = nombre)
        db.session.add(departamento)
        db.session.commit()
        return render_template("departamento2.html")
    return render_template("departamento2.html")

@app.route("/usuario_nuevo", methods = ["GET","POST"])
def usuarioNuevo():
    departamentos = Departamento.query.all()
    if request.method == "POST":
        try:
            username = request.form.get("username")
            nombre = request.form.get("nombre")
            apellido = request.form.get("apellido")
            cedula = request.form.get("cedula")
            cargo = request.form.get("cargo")
            departamento = request.form.get("departamento")
            password = request.form.get("password")
            hashed_pw = generate_password_hash(password)


            usuario = Ususario(username = username, nombre = nombre, apellido = apellido, cedula = cedula, cargo = cargo, departamento_id = departamento, password_hash = hashed_pw )
            db.session.add(usuario)
            db.session.commit()
            flash("La información se envio correctamente")
            return render_template("usuario2.html", departamentos = departamentos)
        except:
            flash("usuario2.html", departamentos = departamentos)
            return render_template("Ocurrio un error Intente nuevamente")
    return render_template("usuario2.html", departamentos = departamentos)

@app.route("/solicitud_nuevo", methods = ["GET", "POST"])
@login_required
def solicitud_nuevo():
    responsable = current_user.nombre
    solicitantes = Solicitante.query.order_by(Solicitante.nombre)
    empresaa = Empresa.query.order_by(Empresa.nombre)
    if request.method == "POST":
        try:
            empresa = request.form.get("empresa")
            descripcion = request.form.get("descripcion")
            numero = request.form.get("numero")
            firmante = request.form.get("firmante")
            solicitante = request.form.get("solicitante")
            empresaa = request.form.get("empresaa")

            solicitud = Solicitud(empresa = empresa, descripcion = descripcion, numero = numero, firmante = firmante, solicitante_id = solicitante, empresa_id = empresaa, responsable = responsable )

            db.session.add(solicitud)
            db.session.commit()
            return render_template("solicitud2.html", solicitante = solicitante, empresa = empresa)
        except:
            flash("Ocurrio un error por favor intenta nuevamente")
            return render_template("solicitud2.html", solicitante = solicitante, empresaa = empresaa)
    return render_template("solicitud2.html", solicitantes = solicitantes, empresaa = empresaa)

@app.route("/asig_depar_nuevo", methods =["GET", "POST"])
@login_required
def asig_depar2():
    solicitudes = Solicitud.query.all()
    usuarios = Ususario.query.all()
    departamentos = Departamento.query.all()
    if request.method == "POST":
        solicitud = request.form.get("solicitud")
        usuario = request.form.get("usuario")
        departamento = request.form.get("departamento")
        password = request.form.get("password")
        user = Ususario.query.filter_by(id = usuario).first()

        if user:
            if check_password_hash(user.password_hash, password):

                asigdepar = AsigDepar(solicitud_id = solicitud, usuario_id = usuario, departamento_id = departamento)
                db.session.add(asigdepar)
                db.session.commit()
                return render_template("asig_depar2.html", solicitudes = solicitudes, usuarios = usuarios, departamentos = departamentos)
            else:
                flash("La contraseña es incorrecta")
                return render_template("asig_depar2.html", solicitudes = solicitudes, usuarios = usuarios, departamentos = departamentos)
        else:
            flash("El usuario no existe")
            return render_template("asig_depar2.html", solicitudes = solicitudes, usuarios = usuarios, departamentos = departamentos)
    return render_template("asig_depar2.html", solicitudes = solicitudes, usuarios = usuarios, departamentos = departamentos)

@app.route("/empresa_nuevo", methods = ["GET", "POST"])
@login_required
def empresa2():
    if request.method == "POST":
        try:
            nombre = request.form.get("nombre")
            rif = request.form.get("rif")
            direc = request.form.get("direccion")
            telf = request.form.get("telefono")
            
            empresa = Empresa(nombre = nombre, rif = rif, direc = direc, telf = telf)
            db.session.add(empresa)
            db.session.commit()
            return render_template("empresa2.html")
        except:
            flash("Ocurrio un error intent nuevamente")
            return render_template("empresa2.html")   
    return render_template("empresa2.html")

@app.route("/estado_nuevo/<int:id>", methods = ["GET","POST"])
@login_required
def estado2(id):
    asignar = Asignar.query.get_or_404(id)
    if request.method == "POST":
        try:
            asignar.estado = request.form.get("estado")
            asignar.descripcion = request.form.get("descripcion")
            db.session.commit()
            return render_template("estado2.html")
        except:
            flash("Ocurrio un error por favor intente nuevamente")
            return render_template("estado2.html")
    return render_template("estado2.html")

@app.route("/", methods = ["GET", "POST"])
def login():
    
    if request.method == "POST":
        try:
            usuario = request.form.get('usuario')
            password = request.form.get("password")
            user = Ususario.query.filter_by(username = usuario).first()

            if user:
                if check_password_hash(user.password_hash, password):
                    login_user(user)
                    flash("Ha iniciado sesion correctamente")
                    return redirect(url_for('inicio'))
                else:
                    flash("Contraseña incorrecta intenta nuevamente")
                    return render_template("login2.html")
            else:
                flash("El usuario no existe intenta nuevamente")
                return render_template("login2.html")
        except:
            flash("Ocurrio un error intenta nuevamnet")
            return render_template("login2.html")
    return render_template("login2.html")

@app.route("/menu_selec", methods = ["GET", "POST"])
def select_box():
    return render_template("select_menu.html")

@app.route("/navbar3", methods = ["GET", "POST"])
def navbar():
    return render_template("navbar3.html")
#https://youtu.be/UN43B6bIrSM?si=9r9OcYkykJe4vayt
