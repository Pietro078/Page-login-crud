from flask import Flask, url_for, render_template
from markupsafe import escape
from routes.home import home_route
#Colocamos uma variavel atrelada ao Objeto flask e o inicio do server
app = Flask(__name__)


#Rotas em flask
app.register_blueprint(home_route)





#Inicia/executa o servidor flask no modo desenvolvedor(algumas vantagens vem com ele): atualiza sempre que salvamos o programa
app.run(debug=True)