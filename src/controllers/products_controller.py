from flask import Blueprint, jsonify, request, current_user
from flask_security import login_required
from flask_security.utils import roles_accepted
from schemas.schemas import ProdutoSchema
from services.products_service import ProdutoService
from extensions import db

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/cadastrar', methods=['POST'])
@login_required
@roles_accepted('admin', 'user')
def cadastrar_produto():
    schema = ProdutoSchema()
    dados = schema.load(request.form)
    service = ProdutoService(db.session, current_user)
    produto = service.cadastrar_produto(dados)
    return jsonify(schema.dump(produto)), 201