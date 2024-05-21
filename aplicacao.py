import boto3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Configurações do DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Users_luca')

# Modelo Pydantic para usuário
class Usuario(BaseModel):
    usuario_id: int
    nome: str

# Inicializa a aplicação FastAPI
app = FastAPI()

# Funções auxiliares
def get_usuario(usuario_id):
    try:
        response = table.get_item(Key={'UserID': str(usuario_id)})
        return response.get('Item', None)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter usuário {usuario_id}: {str(e)}")

def criar_usuario(usuario: Usuario):
    try:
        if get_usuario(usuario.usuario_id):
            raise HTTPException(status_code=400, detail="ID de usuário já existe")
        table.put_item(Item={'UserID': str(usuario.usuario_id), 'Name': usuario.nome})
        return usuario
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar usuário: {str(e)}")

def listar_usuarios():
    try:
        response = table.scan()
        return response.get('Items', [])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar usuários: {str(e)}")

def atualizar_usuario(usuario_id: int, usuario: Usuario):
    try:
        if not get_usuario(usuario_id):
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        table.update_item(
            Key={'UserID': str(usuario_id)},
            UpdateExpression='SET Name = :n',
            ExpressionAttributeValues={':n': usuario.nome}
        )
        return usuario
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar usuário {usuario_id}: {str(e)}")

def deletar_usuario(usuario_id: int):
    try:
        if not get_usuario(usuario_id):
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        table.delete_item(Key={'UserID': str(usuario_id)})
        return {"message": f"Usuário {usuario_id} deletado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao deletar usuário {usuario_id}: {str(e)}")

# Rotas da Aplicação
@app.post("/usuarios/")
async def criar_usuario(usuario: Usuario):
    return criar_usuario(usuario)

@app.get("/usuarios/")
async def listar_usuarios():
    return listar_usuarios()

@app.put("/usuarios/{usuario_id}")
async def atualizar_usuario(usuario_id: int, usuario: Usuario):
    return atualizar_usuario(usuario_id, usuario)

@app.get("/usuarios/{usuario_id}") 
async def buscar_usuario(usuario_id: int):
    usuario = get_usuario(usuario_id)
    if usuario:
        return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.delete("/usuarios/{usuario_id}")
async def deletar_usuario(usuario_id: int):    
    return deletar_usuario(usuario_id)