from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
   


class Solicitud(db.Model):
    __tablename__ = "solicitud"
    id = db.Column(db.Integer, primary_key = True)
    empresa = db.Column(db.String(50))
    descripcion = db.Column(db.String(60))
    fecha = db.Column(db.DateTime,default = datetime.now())
    numero = db.Column(db.Integer, unique = True)
    firmante = db.Column(db.String(50))
    solicitante = db.relationship("Solicitante")
    solicitante_id = db.Column(db.Integer, db.ForeignKey("solicitante.id"))
    responsable = db.Column(db.String(50), nullable = True )
    asignar = db.relationship("Asignar", lazy = "dynamic", backref = "solicitud")
    empresar = db.relationship("Empresa", backref = "empresa")
    empresa_id = db.Column(db.Integer, db.ForeignKey("empresa.id"))
    asig_depar = db.relationship("AsigDepar", backref='solicitud2')


    def __str__(self) -> str:
        return (
            f"Empresa: {self.empresa}"
            f"Descripcion: {self.descripcion}"
            f"Fecha: {self.fecha}"
            f"Numero: {self.numero}"
            f"Firmante: {self.firmante}"
            f"Solicitante: {self.solicitante_id}"
            f"Responsable: {self.responsable}"
        )

class Empresa(db.Model):
    __tablename__= "empresa"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    rif = db.Column(db.String(50))
    direc = db.Column(db.String(50))
    telf = db.Column(db.String(50))
    solicitud = db.relationship("Solicitud", lazy = 'dynamic')
    #solicitud_id = db.Column(db.Integer, db.ForeignKey("solicitud.id"))
    #solicitud = db.relationship("Solicitud")



class Ususario(db.Model, UserMixin):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True) #! Colocar el nullabel = True
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    cedula = db.Column(db.String(50), unique = True)
    cargo = db.Column(db.String(50))
    rango = db.Column(db.String(50))
    departamento = db.relationship("Departamento")
    departamento_id = db.Column(db.Integer, db.ForeignKey("departamento.id"))
    asignar = db.relationship("Asignar", lazy = "dynamic", backref = "usuario3")
    asig_depar = db.relationship("AsigDepar", lazy = "dynamic", backref="usuario2")

    #* Contraseña 
    password_hash = db.Column(db.String(250))

class Solicitante(db.Model):
    __tablename__ = "solicitante"
    id = db.Column(db.Integer, primary_key = True)
    tipo = db.Column(db.String(15))
    nombre = db.Column(db.String(50))
    ci = db.Column(db.String(50), unique = True)
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.String(50), unique = True)
    solicitud = db.relationship("Solicitud", lazy="dynamic")



class Departamento(db.Model):
    __tablename__= "departamento"
    id = db.Column(db.Integer, primary_key = True, unique = True)
    nombre = db.Column(db.String(50), unique = True)
    asginar = db.relationship("Asignar", lazy = "dynamic", backref = "departamento3")
    asigdepa = db.relationship("AsigDepar", lazy = "dynamic", backref="departamento2")
    usuario = db.relationship("Ususario", lazy = "dynamic")


class Asignar(db.Model):
    __tablename__ = "asignar"
    id = db.Column(db.Integer, primary_key = True, unique = True)
    depertamento = db.relationship("Departamento", backref = "departamento")
    depertamento_id = db.Column(db.Integer, db.ForeignKey("departamento.id"))
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    usuario = db.relationship("Ususario")
    solictud = db.relationship("Solicitud")
    solicitud_id = db.Column(db.Integer, db.ForeignKey("solicitud.id"))
    fecha = db.Column(db.DateTime, default= datetime.now())
    estado = db.Column(db.String(50), default= "Sin realizar" )
    descripcion = db.Column(db.String(100))

    def __str__(self):
        return(
            f"Departamento {self.depertamento_id.nombre}"
            f"Usuario {self.usuario_id.nombre}"
            f"Solicitud {self.solicitud_id.numero}"
            f"Fecha {self.fecha}"
            f"Estado {self.estado}"
        )

class AsigDepar(db.Model):
    __tablename__ = "asginar_departamento"
    id = db.Column(db.Integer, primary_key = True, unique = True)
    solicitud = db.relationship("Solicitud")
    solicitud_id = db.Column(db.Integer, db.ForeignKey("solicitud.id"))
    departamento = db.relationship("Departamento")
    departamento_id = db.Column(db.Integer, db.ForeignKey("departamento.id"))
    usuario = db.relationship("Ususario")
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    fecha = db.Column(db.DateTime, default = datetime.now())




    #@property
    #def password(self):
      #  raise AttributeError("Pasword is not a readable attribute")
    
    #@password.setter
    #def password(self, password):
     #   self.password_hash = generate_password_hash(password)

    #def verify_password(self,password):
     #   return check_password_hash(self.password_hash, password)
