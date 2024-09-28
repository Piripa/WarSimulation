
from jogador.Observer.observer import Observer

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def disattach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, mensagem: str):
        for observer in self._observers:
            observer.update(mensagem)