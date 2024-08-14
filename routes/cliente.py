from flask import render_template,Blueprint, request, redirect, url_for
from DataBase.cliente import CLIENTES
from DataBase.models.cliente import Cliente
clientes_route= Blueprint('cliente',__name__)




@clientes_route.route('/')
def lista_clientes():
    
    cliente = Cliente.select()
    return render_template('lista_clientes.html', clientes=cliente)

@clientes_route.route('/', methods=['POST'])
def obter_clientes():
    ''' cirar usuario '''
    data = request.json
    novo_usuario=Cliente.create(
        email = data['email'],
        senha = data['senha']
    )

    

    return render_template('item_cliente.html', cliente=novo_usuario)

@clientes_route.route('/new')
def cria_cliente():
    ''' formulario cadastro cliente '''
    c = request.method
    
    return render_template('cria_cliente.html', c=c)

@clientes_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    ''' formulario mostrar informações '''
    return render_template('detalhe_cliente.html')

@clientes_route.route('/<int:cliente_id>/edit')
def form_Edit_cliente(cliente_id):
    ''' alterar informações cliente '''
    cliente = None
    for c in CLIENTES:
        if c["id"] == cliente_id:
            cliente = c
    return render_template('cria_cliente.html', cliente=cliente)

@clientes_route.route('/<int:cliente_id>/update', methods=['PUT'])
def form_atualizar_cliente(cliente_id):
    ''' atulizar informações cliente '''
    cliente = None
    data = request.json
    for c in CLIENTES:
        if c['id'] ==  cliente_id:
            c['email'] = data['email']
            c['senha'] = data['senha']
            cliente_editado = c
        return render_template('item_cliente.html', cliente = cliente_editado )

@clientes_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    ''' deletar informações cliente '''
    global CLIENTES
    CLIENTES = [c for c in CLIENTES if c['id'] != cliente_id]

    return {'deleted': 'ok'}


