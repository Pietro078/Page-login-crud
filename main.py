from flask import Flask, url_for, render_template
from markupsafe import escape
from routes.home import home_route
from routes.cliente import clientes_route
from configuration import configure_all
#Colocamos uma variavel atrelada ao Objeto flask e o inicio do server
app = Flask(__name__)


configure_all(app)


#Inicia/executa o servidor flask no modo desenvolvedor(algumas vantagens vem com ele): atualiza sempre que salvamos o programa
app.run(debug=True)

