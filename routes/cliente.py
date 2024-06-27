from flask import render_template,Blueprint
from DataBase.cliente import CLIENTES

clientes_route= Blueprint('clientes',__name__)

@clientes_route.route('/')
def lista_clientes():
    '''listar clientes'''
    return render_template('lista_clientes.html', clientes=CLIENTES)

@clientes_route.route('/', methods=['POST'])
def obter_clientes():
    ''' cirar usuario '''
    pass

@clientes_route.route('/new')
def cria_cliente():
    ''' formulario cadastro cliente '''
    return render_template('cria_cliente.html')

@clientes_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    ''' formulario mostrar informações '''
    return render_template('detalhe_cliente.html')

@clientes_route.route('/<int:cliente_id>/edit')
def form_Edit_cliente(cliente_id):
    ''' alterar informações cliente '''
    pass

@clientes_route.route('/<int:cliente_id>/update', methods=['PUT'])
def form_atuluzar_cliente(cliente_id):
    ''' atulizar informações cliente '''
    pass

@clientes_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def form_delete_cliente(cliente_id):
    ''' atulizar informações cliente '''
    pass

