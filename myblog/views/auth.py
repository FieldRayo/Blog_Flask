from flask import(
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from myblog.models.user import User 
from myblog import db

auth = Blueprint('auth', __name__, url_prefix='/auth')

# Registrar usuario
@auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
    
        user = User(username, generate_password_hash(password))

        error = ''
        if not username:
            error = 'Se requiere nombre de usuario'
        elif password:
            error = 'se requiere una contraseña'

        user_name = User.query.filter_by(username = username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()

        else:
            error = f'El usuario "{username}" ya existe'

        flash(error)

    return render_template('auth/register.html')

@auth.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
    

        error = ''
        user = User.query.filter_by(username = username).first()
        if not user:
            error = 'Nombre de usuario incorrecto'
        elif not check_password_hash(user.password, password):
            error = 'Constraseña incorrecta'


        if not error:
            session.clear()
            session['user_id'] = user.id
            #return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
