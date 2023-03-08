from flask import Flask
from app.controllers import user_controller, auth_controller, home_controller, auth_dash_controller, setting_controller
from app.adapters import database_adapter
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object('app.config.Config')
    
    # Register controllers
    app.register_blueprint(user_controller.bp)
    app.register_blueprint(auth_controller.bp)
    app.register_blueprint(home_controller.bp)
    
    # Register controllers dashboard
    app.register_blueprint(auth_dash_controller.bp)
    app.register_blueprint(setting_controller.bp)
    
    # Initialize database
    database_adapter.DatabaseAdapter()
    
    return app