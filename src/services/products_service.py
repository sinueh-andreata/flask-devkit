

class ProductsService:
    def __init__(self, db_session, current_user):
        self.db_session = db_session
        self.current_user = current_user
    
    def salvar_produto(self, dados):
        produto = ProductsService.criar_produto(dados)
        self.db_session.add(produto)
        self.db_session.commit()
        return produto
    
    