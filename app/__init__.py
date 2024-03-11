from flask import Flask
from app import routes
from app.config import database
from .models.cliente import ClienteModel

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
    
    @app.before_request
    def makeDB():
        app.before_request_funcs[None].remove(makeDB)
        database.drop_all()
        database.create_all()  
        cliente = ClienteModel(nome='o barato sai caro', limite=1000 * 100, saldo=0)
        cliente.save()
        cliente = ClienteModel(nome='zan corp ltda', limite=800 * 100, saldo=0)
        cliente.save()
        cliente = ClienteModel(nome='les cruders', limite=10000 * 100, saldo=0)
        cliente.save()
        cliente = ClienteModel(nome='padaria joia de cocaia', limite=100000 * 100, saldo=0)
        cliente.save()
        cliente = ClienteModel(nome='kid mais', limite=5000 * 100, saldo=0)
        cliente.save()
        cliente = None
    return app