from flask import Blueprint, jsonify, request
from flask_security import login_required
from flask_security.decorators import current_user, roles_accepted
from src.schemas.schemas import ProdutoSchema
from src.services.products_service import ProductsService
from src.extensions import db

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/cadastrar', methods=['POST'])
@login_required
@roles_accepted('admin', 'user')
def cadastrar_produto():
    schema = ProdutoSchema()
    dados = schema.load(request.get_json())
    service = ProductsService(db.session, current_user)
    produto = service.salvar_produto(dados)
    return jsonify(schema.dump(produto)), 201

@products_bp.route('/listar', methods=['GET'])
@login_required
@roles_accepted('admin', 'user')
def listar_produtos():
    service = ProductsService(db.session, current_user)
    produtos = service.listar_produtos()
    schema = ProdutoSchema(many=True)
    return jsonify(schema.dump(produtos)), 200

@products_bp.route('/listar/<int:id>', methods=['GET'])
@login_required
@roles_accepted('admin', 'user')
def listar_produto(id):
    service = ProductsService(db.session, current_user)
    produto = service.listar_produto(id)
    if not produto:
        return jsonify({'message': 'Produto não encontrado'}), 404

    schema = ProdutoSchema()
    return jsonify(schema.dump(produto)), 200

@products_bp.route('/atualizar/<int:id>', methods=['PUT'])
@login_required
@roles_accepted('admin', 'user')
def atualizar_produto(id):
    schema = ProdutoSchema()
    dados = schema.load(request.get_json())
    service = ProductsService(db.session, current_user)
    produto = service.atualizar_produto(dados, id)
    
    if not produto:
        return jsonify({'message': 'Produto não encontrado'}), 404
    return jsonify(schema.dump(produto)), 200

@products_bp.route('/deletar/<int:id>', methods=['DELETE'])
@login_required
@roles_accepted('admin', 'user')
def deletar_produto(id):
    service = ProductsService(db.session, current_user)
    produto = service.deletar_produto(id)
    
    if not produto:
        return jsonify({'message': 'Produto não encontrado'}), 404
    
    return jsonify({'message': 'Produto deletado com sucesso'}), 200