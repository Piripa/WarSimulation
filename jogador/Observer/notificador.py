
from jogador.Observer.observer import Observer


class Notificador(Observer):
    def update(self, jogador):
        print(f"Jogador {jogador.id} se juntou ao jogo com a cor {jogador.cor}.")
