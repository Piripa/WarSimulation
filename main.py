from jogador.preparacao.cor import *
from jogador.preparacao.objetivos import *
from jogador.jogadorFactory import *
from jogador.distribuir_exercito.distribuidor_posicao import *
from jogador.distribuir_exercito.distribuidor_exercito import *
from jogador.distribuir_exercito.territorios import *

from fastapi import FastAPI, HTTPException, Response

 

app = FastAPI()

jogadores = []
ultimo_id = 0
max_jogadores = 6

@app.post("/novoJogador",summary="Entrar no jogo", description="Escolha a uma cor para ser a cor do seu exercito: 1 - AZUL; 2 - BRANCA; 3 - VERMELHA; 4 - PRETA; 5 - AMARELO; 6 - VERDE")
async def novo_jogador(select_cor:int):
    global ultimo_id

    if len(jogadores) >= max_jogadores:
        raise HTTPException(status_code=400, detail="O número máximo de jogadores (6) já foi atingido.")

    try:
        ultimo_id += 1
        novo_jogador = JogadorFactory.create_jogador(ultimo_id, select_cor, jogadores)
        jogadores.append(novo_jogador)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return Response(status_code=201)

@app.get("/num-player")
async def get_playernum(id:int):
    return jogadores[id-1]

@app.get("/prepara/cor")
async def get_color(id:int):
    return jogadores[id-1].get_cor()

@app.get("/prepara/objetivo")
async def get_objetivos(id:int):
    return jogadores[id-1].get_objetivo()

@app.get("/distribui/territorio")
async def get_terri(id:int):
    return jogadores[id-1].get_territorio()

@app.get("/distribui/posicao")
async def get_posicional(id:int):
    return jogadores[id-1].get_posicao()

@app.get("/distribui/qtdexercito")
async def get_qtd_exercito_jogador(id:int):
    return jogadores[id-1].get_qtd_exercito()

@app.get("/show_id")
async def show_id():
    return jogadores