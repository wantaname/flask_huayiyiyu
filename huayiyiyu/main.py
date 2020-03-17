from flask import Flask
import menu,data,category
from flask_cors import CORS
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py', silent=True)
    CORS(app, resources=r'/*')
    app.register_blueprint(menu.bp)
    app.register_blueprint(data.bp)
    app.register_blueprint(category.bp)
    return app

app=create_app()

