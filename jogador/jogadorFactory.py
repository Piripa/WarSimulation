from jogador.preparacao.cor import *
from jogador.preparacao.objetivos import *
from jogador.distribuir_exercito.distribuidor_posicao import *
from jogador.distribuir_exercito.distribuidor_exercito import *
from jogador.distribuir_exercito.territorios import *
from jogador.jogador import Jogador

class JogadorFactory:
    @staticmethod
    def create_jogador(ultimo_id, select_cor, jogadores):
        cor_escolhida = buscar_cor(select_cor)
        for jogador in jogadores:
            if jogador.cor == cor_escolhida:
                raise ValueError(f"A cor {cor_escolhida} já foi escolhida por outro jogador.")
        return Jogador(
            ultimo_id,
            buscar_cor(select_cor),
            buscar_objetivo(),
            distribuir_terri(),
            pegar_posicao(jogadores),
            receber_exercito_inicio()
        )
