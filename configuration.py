from routes.home import home_route
from routes.cliente import clientes_route
from DataBase.database import db
from DataBase.models.cliente import Cliente

def configure_all(app):
    configure_routs(app)
    configure_db()

def configure_routs(app):
    app.register_blueprint(home_route)
    app.register_blueprint(clientes_route, url_prefix='/clientes')

def configure_db():
    db.connect()
    db.create_tables([Cliente])