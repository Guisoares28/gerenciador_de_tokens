from flask import Flask

from extensions.database import db, migrate
from middlewares.error_handler import init_error_handler
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123@localhost:5432/gerenciaToken"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = "super-secreta-e-unica"

    from datetime import timedelta
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=7)

    db.init_app(app)
    migrate.init_app(app, db)

    jwt = JWTManager(app)
    init_error_handler(app)

    from routes.clientes_routes import clientes_bp
    app.register_blueprint(clientes_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)