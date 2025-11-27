from flask import Blueprint, jsonify, request
from flask_security import login_required
from flask_security.decorators import current_user, roles_accepted
from src.schemas.schemas import ProductSchema
from src.services.products_service import ProductsService
from src.extensions import db
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/create/products', methods=['POST'])
@login_required
@roles_accepted('admin', 'user')
def create_product():
    schema = ProductSchema()
    service = ProductsService(db.session, current_user)
    try:
        dados = schema.load(request.get_json())
        product = service.save_product(dados)
        return jsonify(schema.dump(product)), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except IntegrityError:
        return jsonify({"error": "Produto já existe ou violação de integridade"}), 400
    except RuntimeError as err:
        return jsonify({"error": str(err)}), 500
    except Exception as err:
        return jsonify({"error": "Erro interno do servidor"}), 500