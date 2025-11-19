from src.models.models import Produto

class ProductsService:
    def __init__(self, db_session, current_user):
        self.db_session = db_session
        self.current_user = current_user
    
    def criar_produto(self, dados):
        return Produto(**dados, user_id=self.current_user.id)

    def salvar_produto(self, dados):
        produto = self.criar_produto(dados)
        try:
            self.db_session.add(produto)
            self.db_session.commit()
            return produto
        except Exception as e:
            self.db_session.rollback()
            raise e
        
    def listar_produtos(self):
        return Produto.query.all()
    
    def listar_produto(self, id):
        return self.db_session.query(Produto).filter_by(id=id).first()