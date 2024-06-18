from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms_alchemy import QuerySelectMultipleField, QuerySelectField
from models import Departamento

numeros = ["0","1","2","3","4","5","6","7","8","9"]
def que_no_sea_numero(form, field):
    for caracter in field.data:
        if caracter == numeros:
            raise ValidationError ("El campo no acepta numeros")

class SolicitudForm(FlaskForm):
    empresa = StringField("Empresa/Persona", validators = [DataRequired()])
    descripcion = StringField("Descripcion", validators = [DataRequired()])
    numero = IntegerField("Numero de solicitud", validators = [DataRequired()])
    firmante = StringField("Firmante", validators=[DataRequired()])
    solicitante_id = SelectField("Solicitante", choices=[], coerce= int)
    empresa_id = SelectField("Empresa", choices=[], coerce= int)
    guardar = SubmitField()


class EmpresaForm(FlaskForm):
    nombre = StringField("Nombre de la empresa", validators=[DataRequired()])
    rif = StringField("RIF", validators=[DataRequired()])
    direc = StringField("Direccion", validators=[DataRequired()])
    telf = StringField("Telefono", validators=[DataRequired()])
    guardar = SubmitField()

class UsuarioForm(FlaskForm):
    nombre = StringField("Nombre", validators= [DataRequired(), que_no_sea_numero])
    apellido = StringField("Apellido", validators = [DataRequired()])
    cedula = StringField("Cedula", validators= [DataRequired()])
    cargo = StringField("Cargo", validators=[DataRequired()])
    username = StringField("Usuario", validators=[DataRequired()])
    password_hash = PasswordField("Contraseña", 
                                  validators=[DataRequired(),
                                              EqualTo("password_hash2", message="Las contraseñas deben coincidir !"), 
                                              Length(max=16, min=8, message=" La contraseña deber tener 8 caracteres")])
    password_hash2 = PasswordField("Confirmar contraseña", validators=[DataRequired(), 
                                                                       EqualTo("password_hash", message = "La contraseña debe coincidir")])
    departamento = SelectField("Departamento", choices=[], coerce= int)
    guardar = SubmitField()


class LoginForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired()]) 
    password = PasswordField("Contraseña", validators=[DataRequired()])
    iniciar = SubmitField("Iniciar Sesion")

class SolicitanteForm(FlaskForm):

    tipo = StringField("Natural o Juridica", validators=[DataRequired()])
    nombre = StringField("Nombre", validators=[DataRequired(), que_no_sea_numero])
    ci =StringField("Cedula o RIF", validators=[DataRequired()])
    direccion = StringField("Direccion", validators=[DataRequired()])
    telefono = StringField("Telefono", validators=[DataRequired()])
    guardar = SubmitField("Guardar")

#class EmpleadoForm(FlaskForm):
  #  nombre = StringField("Nombre", validators=[DataRequired()])
   # apellido = StringField("Apellido", validators=[DataRequired()])
    #ci = StringField("Cedula", validators=[DataRequired()])
    #cargo = StringField("Cargo", validators=[DataRequired()])
    #departamento = SelectField("Departamento", choices=[], coerce= int)
    #guardar = SubmitField("Guardar")

class DepartamentoForm(FlaskForm):
    nombre = StringField("Departamento", validators=[DataRequired()])
    guardar = SubmitField("Guardar")

class AsginarForm(FlaskForm):
    departamento_id = SelectField("Departamento", choices=[], coerce= int)
    solicitud_id = SelectField("Solicitud", choices=[], coerce= int)
    usuario_id = SelectField("Usuario", choices=[], coerce= int)
    estado = SelectField("Estado", choices=["Realizado", "Sin realizar"])
    guardar = SubmitField("Guardar")

class AsigDeparForm(FlaskForm):
    solicitud_id = SelectField("Solicitud", choices=[], coerce= int)
    departamento_id = SelectField("Departamento", choices=[], coerce= int)
    usuario_id = SelectField("Usuario", choices=[], coerce= int)
    guardar = SubmitField("Guardar")