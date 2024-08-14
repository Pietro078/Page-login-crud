from flask import render_template,Blueprint, request, redirect, url_for
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
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente=cliente)

@clientes_route.route('/<int:cliente_id>/edit')
def form_Edit_cliente(cliente_id):
    ''' alterar informações cliente '''
    cliente = Cliente.get_by_id(cliente_id) 
    return render_template('cria_cliente.html', cliente=cliente)

@clientes_route.route('/<int:cliente_id>/update', methods=['PUT'])
def form_atualizar_cliente(cliente_id):
    ''' atulizar informações cliente '''
    data = request.json
    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.email = data['email']
    cliente_editado.senha = data['senha']
    cliente_editado.save()
    
    return render_template('item_cliente.html', cliente = cliente_editado )

@clientes_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    ''' deletar informações cliente '''
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return {'deleted': 'ok'}


