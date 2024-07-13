import os

from flask import Flask, render_template, request, redirect, url_for, flash

from datetime import datetime
from model import Comentarios, Mensaje, db
from config import Config


# ! Estructura básica de una aplicación Flask - Seguir implementando



template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)

app.config.from_object(Config)

db.init_app(app)


#- Establecer el contexto de la aplicación -#
with app.app_context():
    db.create_all()


#- Routes -#

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/candidatosYpropuestas')
def candidatosYpropuestas():
    return render_template('candYprop.html')


@app.route('/encuesta')
def encuesta():
    return render_template('encuesta.html')

@app.route('/encuestaForm', methods=['POST'])
def encuestaForm():
    return redirect(url_for('encuesta'))


@app.route('/comentarios')
def comentarios():

    # Consultar y mostrar comentarios utilizando SQLAlchemy
    comentarios = Comentarios.query.order_by(db.func.concat(Comentarios.fecha_formateada, ' ', Comentarios.hora).desc()).all()
    print(type(comentarios))
    return render_template('comentarios.html', data=comentarios)




@app.route('/agregarComentario', methods=['GET', 'POST'])
def add_comentario():
    if request.method == 'POST':

        nombre = request.form['nombre']
        correo = request.form['correo']
        asunto = request.form['asunto']
        comentario = request.form['comentario']

        if nombre and correo and asunto and comentario:
            nuevo_comentario = Comentarios(
                nombre=nombre, correo=correo, asunto=asunto,
                comentario=comentario)
            db.session.add(nuevo_comentario)
            db.session.commit()
            flash('Comentario agregado correctamente', 'success')
        else:
            flash('Por favor completa todos los campos', 'error')

        return redirect(url_for('comentarios'))

    return redirect(url_for('comentarios'))


@app.route('/borrar/<int:id>')
def delete_comentario(id):
    comentario = Comentarios.query.get(id)
    if comentario:
        db.session.delete(comentario)
        db.session.commit()
        flash('Comentario eliminado correctamente', 'success')
    else:
        flash('Comentario no encontrado', 'error')

    return redirect(url_for('comentarios'))


@app.route('/editar/<int:id>', methods=['GET'])
def get_contact(id):
    comentario = Comentarios.query.get(id)
    if comentario is None:
        flash('Comentario no encontrado', 'error')
        return redirect(url_for('comentarios'))

    return render_template('edit_comentario.html', coment_modif=comentario)


@app.route('/update/<int:id>', methods=['POST'])
def update_contact(id):
    comentario = Comentarios.query.get(id)
    if comentario is None:
        flash('Comentario no encontrado', 'error')
        return redirect(url_for('comentarios'))

    if request.method == 'POST':
        fecha_hora = datetime.now()
        fecha_formateadaEdit = fecha_hora.strftime('%d/%m/%Y')
        horaEdit = fecha_hora.strftime('%H:%M:%S')

        comentario.nombre = request.form['nombre'].strip()
        comentario.correo = request.form['correo'].strip()
        comentario.asunto = request.form['asunto'].strip()
        comentario.comentario = request.form['comentario'].strip()
        comentario.fecha_formateada_edit = fecha_formateadaEdit
        comentario.hora_edit = horaEdit

        db.session.commit()
        flash('Comentario actualizado correctamente', 'success')
        return redirect(url_for('comentarios'))

    flash('No se pudo actualizar el comentario', 'error')
    return redirect(url_for('comentarios'))



@app.route('/contactanos')
def contactanos():
    return render_template('contactanos.html')

@app.route('/mensajes_contacto', methods=['POST'])
def add_contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        asunto = request.form['asunto']
        comentario = request.form['comentario']
        checkk = request.form.get('checkk', False)
        checkk = True if checkk == 'on' else False  # Convierte a booleano
        fecha = datetime.datetime.now()

        if nombre and apellido and email and telefono and asunto and comentario:
            nuevo_mensaje = Mensaje(
                nombre=nombre.strip(),
                apellido=apellido.strip(),
                email=email.strip(),
                telefono=telefono.strip(),
                asunto=asunto.strip(),
                comentario=comentario.strip(),
                checkk=checkk,
                fecha=fecha
            )
            db.session.add(nuevo_mensaje)
            db.session.commit()
            flash('Contacto agregado', 'success')
        else:
            flash('Por favor completa todos los campos', 'error')

        return redirect(url_for('contactanos'))




if __name__ == "__main__":
    app.run(port=4000, debug=True)