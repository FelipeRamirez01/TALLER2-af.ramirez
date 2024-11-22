from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager, UserMixin, login_user, login_required


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder='views')
    """ app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/taller1modulo3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Clave secreta para manejar sesiones y seguridad
    app.config['SECRET_KEY'] = os.urandom(24)  # Genera una clave aleatoria

    

    db.init_app(app)
    """
    from controllers.controller import main
    app.register_blueprint(main)

    #with app.app_context():
        #db.create_all() 

    return app

 