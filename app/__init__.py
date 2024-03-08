from flask import Flask
from app import routes
from app.config import database

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=not test_config)
    
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, __name__, 'db')
    # )
    # print(os.path.join(app.instance_path, __name__, 'db'))
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=False)
    else:
        app.config.from_object('app.config.DevConfig')        
        
    app.register_blueprint(routes.clientes_bp, url_prefix='/clientes')
    
    database.init_app(app)
    
    # @app.before_request
    # def makeDB():
    #     app.before_request_funcs[None].remove(makeDB)
    #     database.drop_all()
    #     database.create_all()        
    
    return app