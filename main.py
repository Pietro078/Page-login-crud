from flask import Flask, url_for, render_template
from markupsafe import escape
#Colocamos uma variavel atrelada ao Objeto flask e o inicio do server
app = Flask(__name__)


#Rotas em flask
@app.route('/', methods=['GET'])
def ola_mundo():
   return 'ola'

#Inicia/executa o servidor flask no modo desenvolvedor(algumas vantagens vem com ele): atualiza sempre que salvamos o programa
app.run(debug=True)