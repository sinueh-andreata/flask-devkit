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
    schema = ProductSchema()  # cria uma instância do schema responsável por validar e serializar os dados do produto
    service = ProductsService(db.session, current_user)  # cria o serviço de produtos, passando a sessão do banco e o usuário logado
    try:
        data = schema.load(request.get_json()) # serializo os dados com o schema e carrego os dados requisitanto o json
        product = service.save_product(data) # produto é salvo com o service instanciado e salvo o produto com o método passando a data
        return jsonify(schema.dump(product)), 201 # retorno o produto serializado para JSON com o schema e status 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except IntegrityError:
        return jsonify({"error": "Produto já existe ou violação de integridade"}), 400
    except RuntimeError as err:
        return jsonify({"error": str(err)}), 500
    except Exception as err:
        return jsonify({"error": "Erro interno do servidor"}), 500

@admin_bp.route('/update/products', methods=["PUT"])
@login_required
@roles_accepted('admin', 'root')
def alter_product():
    schema = ProductSchema()
    service = ProductsService(db.session, current_user)
    try:
        data = schema.load(request.get_json())
        alter_product = service.update_product(data)
        return jsonify(schema.dump(alter_product)), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except IntegrityError:
        return jsonify({"error": "Violação de integridade"}), 400
    except RuntimeError as err:
        return jsonify({"error": str(err)}), 500
    except Exception as err:
        return jsonify({"error": "Erro interno do servidor"}), 500

