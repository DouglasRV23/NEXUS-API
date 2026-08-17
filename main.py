from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="NEXUS Services API",
    description="API simples para serviços profissionais",
    version="1.0.0"
)


class Servico(BaseModel):

    nome: str
    categoria: str
    descricao: str
    cidade: str
    preco: float
    telefone: str
    avaliacao: float


servicos = []


@app.get("/")
def inicio():

    return {
        "mensagem": "NEXUS API funcionando!"
    }


@app.post("/servicos")
def criar_servico(servico: Servico):

    novo_servico = servico.model_dump()

    novo_servico["id"] = len(servicos) + 1

    servicos.append(novo_servico)

    return {
        "mensagem": "Serviço criado com sucesso!",
        "servico": novo_servico
    }


@app.get("/servicos")
def listar_servicos():

    return servicos


@app.get("/servicos/{servico_id}")
def consultar_servico(servico_id: int):

    for servico in servicos:

        if servico["id"] == servico_id:

            return servico

    return {
        "erro": "Serviço não encontrado"
    }
