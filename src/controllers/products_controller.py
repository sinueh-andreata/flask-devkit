from flask import Blueprint
from flask_security import login_required
from flask_security.utils import roles_accepted

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/', methods=['GET'])
@login_required
@roles_accepted('admin', 'user')
def cadastrar_produto():
    schema = ProdutoSchema()
    dados = {schema.load