from flask import Blueprint, render_template, request, redirect, session, url_for

auth_bp = Blueprint('auth', __name__, template_folder='../templates/auth')

USUARIOS = {
    'admin': '1234',
    'sergio': 'python',
    'ana': 'flasklover'
}

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USUARIOS and password == USUARIOS[username]:
            session['usuario'] = username
            return redirect(url_for('dashboard.dashboard'))
        else:
            error = 'Usuario o contraseña incorrectos'
    return render_template('login.html', error=error)

@auth_bp.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))

    mensaje = None

    if request.method == 'POST':
        nuevo_usuario = request.form.get('nuevo_usuario')
        if nuevo_usuario:
            session['usuario'] = nuevo_usuario
            mensaje = 'Nombre de usuario actualizado con éxito.'

    return render_template('perfil.html', usuario=session['usuario'], mensaje=mensaje)

@auth_bp.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('auth.login'))
