from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = 'clave-secreta-super-pro'

    # Importar Blueprints
    from .auth import auth_bp
    from .dashboard import dashboard_bp

    # Registrar Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    return app
