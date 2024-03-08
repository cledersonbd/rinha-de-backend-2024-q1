from flask import Blueprint, jsonify, request
from .models.cliente import ClienteModel
from .models.transacao import TransacaoModel
from datetime import datetime

clientes_bp = Blueprint(
    'cliente_bp', 
    __name__
)

@clientes_bp.route('/', endpoint='teste0')
def getClientes():
    return jsonify([item.toJSON() for item in ClienteModel.findAll()])
    
@clientes_bp.route('/', methods=['POST'], endpoint='teste1')
def post():
    # if id is None:
    #     return {'message': 'Requisição incorreta- - ID inválido'}, 400
    
    data = request.json
    if data is None:
        return {'message': 'Requisição incorreta - Dados inválidos'}, 400
    
    cliente = ClienteModel(**data)
    try: 
        cliente.save()
        return cliente.toJSON()
    except Exception as error:
        return {'message': error.__str__()}, 500
    

@clientes_bp.route('/<id>/extrato', endpoint='teste2')
def get(id=None):
    if id:
        cliente = ClienteModel.findById(id)
        if cliente is None:
            return {'message': 'Cliente não encontrado'}, 404
        
    return {
        'saldo': {
            'total': cliente.saldo,
            'data_extrato': datetime.now(),
            'limite': cliente.limite
        },
        'ultimas_transacoes': [item.toJSON() for item in TransacaoModel.getAllByClientID(cliente.id, limit=10)]
    }

@clientes_bp.route('/<id>/transacoes', methods=['POST'])
def post(id):
    data = request.json
    if id is None:
        return {'message': 'Requisição incorreta - ID de cliente inválido'}, 400
    
    cliente = ClienteModel.findById(id)
    if cliente is None:
        return {'message': 'Cliente não encontrado'}, 404
    
    transacao = TransacaoModel(**data, cliente=cliente.id)
    try:
        if cliente.updateSaldo(transacao):
            transacao.save()
            cliente.save()
        else:
            return {'message': 'Operação fora do limite do cliente'}, 422
        
    except Exception as error:
        return  {'message': 'Deu merda braba: {}'.format(error.__str__())}, 500
    
    return {
        'limite': cliente.limite,
        'saldo' : cliente.saldo
    }
    cliente = ClienteModel.findById(id)
    if cliente:
        return jsonify(cliente)
    
    
    