from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    
class ProdutoSchema(Schema):
    class Meta:
        unknown = 'EXCLUDE'
        
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    preco = fields.Float(required=True)
    estoque = fields.Int(required=True)