
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Column, Integer, String, Text, Time, DateTime, Boolean
from datetime import datetime


db = SQLAlchemy()

#- Tablas de la base de datos -----------------------------------------------------------------

class Comentarios(db.Model):
    __tablename__ = 'comentarios_blog'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(60), nullable=False)
    correo = Column(String(60), nullable=False)
    asunto = Column(String(80), nullable=False)
    comentario = Column(Text, nullable=False)
    fecha_hora = Column(DateTime, nullable=False)
    hora = Column(Time, nullable=False)
    fecha_formateada = Column(String(10), nullable=False)
    fecha_formateada_edit = Column(String(10), nullable=True)
    hora_edit = Column(Time, nullable=True)

    def __init__(self, nombre, correo, asunto, comentario,
                 fecha_formateada_edit=None, hora_edit=None):
        self.nombre = nombre
        self.correo = correo
        self.asunto = asunto
        self.comentario = comentario
        self.fecha_hora = datetime.now()
        self.hora = self.fecha_hora.strftime('%H:%M:%S')
        self.fecha_formateada = self.fecha_hora.strftime('%d/%m/%Y')
        self.fecha_formateada_edit = fecha_formateada_edit
        self.hora_edit = hora_edit

    def __repr__(self):
        return f'''
                nombre: {self.nombre} // correo: {self.correo}\n
                asunto: {self.asunto} // comentario: {self.comentario}\n
                fecha: {self.fecha_formateada} // hora: {self.hora}\n
                fechaEdit: {self.fecha_formateada_edit} // horaEdit: {self.hora_edit}\n
                FECHA HORA: {self.fecha_hora}
                '''



class Mensaje(db.Model):
    __tablename__ = 'mensajes_contacto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(60), nullable=False)
    apellido = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    telefono = Column(String(12), nullable=False)
    asunto = Column(String(80), nullable=False)
    comentario = Column(Text, nullable=False)
    checkk = Column(Boolean, nullable=False)
    fecha = Column(DateTime, nullable=False )

    def __init__(self, nombre, apellido, email, telefono, asunto, comentario, checkk):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.asunto = asunto
        self.comentario = comentario
        self.checkk = checkk
        self.fecha = datetime.now()

    def __repr__(self):
        return f'''
                nombre: {self.nombre} // apellido: {self.apellido}\n
                email: {self.email} // telefono: {self.telefono}\n
                asunto: {self.asunto} // comentario: {self.comentario}\n
                checkk: {self.checkk} // fecha: {self.fecha}\n
                FECHA HORA: {self.fecha}
                '''



