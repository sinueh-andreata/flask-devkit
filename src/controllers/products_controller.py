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
    dados = schema.load(request.form)
    service = ProductsService(db.session, current_user)
    produto = service.salvar_produto(dados)
    return jsonify(schema.dump(produto)), 201