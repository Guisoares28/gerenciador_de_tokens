from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from middlewares.error_handler import init_error_handler



db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123@localhost:5432/gerenciaToken"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    init_error_handler(app)

    from routes.clientes_routes import clientes_bp
    app.register_blueprint(clientes_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)