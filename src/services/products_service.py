from models import Produto

class ProductsService:
    def __init__(self, db_session, current_user):
        self.db_session = db_session
        self.current_user = current_user
    
    def criar_produto(self, dados):
        return Produto(**dados, user_id=self.current_user.id)

    def salvar_produto(self, dados):
        produto = self.criar_produto(dados)
        self.db_session.add(produto)
        self.db_session.commit()
        return produto