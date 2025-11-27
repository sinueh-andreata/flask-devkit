from src.models.models import Product
from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError

class ProductsService:
    def __init__(self, db_session, current_user):
        self.db_session = db_session
        self.current_user = current_user

    def instace_product(self, dados):
        return Product(**dados, user_id=self.current_user.id)

    def save_product(self, dados):
        product = self.instace_product(dados)
        try:
            self.db_session.add(product)
            self.db_session.commit()
            return product

        except IntegrityError:
            self.db_session.rollback()
            raise IntegrityError("Produto duplicado ou violação de integridade.")

        except SQLAlchemyError as e:
            self.db_session.rollback()
            raise RuntimeError("Erro interno ao salvar o produto.") from e

    def list_all_products(self):
        return self.db_session.query(Product).filter_by(
            user_id=self.current_user.id
        ).all()

    def get_product(self, id):
        return self.db_session.query(Product).filter_by(
            id=id,
            user_id=self.current_user.id
        ).first()

    def update_product(self, dados, id):
        product = self.get_product(id)

        if not product:
            return None

        for campo, valor in dados.items():
            setattr(product, campo, valor)

        try:
            self.db_session.commit()
            return product

        except SQLAlchemyError as e:
            self.db_session.rollback()
            raise RuntimeError("Erro ao atualizar produto.") from e

    def delete_product(self, id):
        product = self.get_product(id)

        if not product:
            return None

        try:
            self.db_session.delete(product)
            self.db_session.commit()
            return product

        except SQLAlchemyError as e:
            self.db_session.rollback()
            raise RuntimeError("Erro ao excluir produto.") from e