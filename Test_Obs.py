import unittest
from jogador.Observer import *
from jogador.Observer.subject import Subject
from main import *


class TestePadraoObserver(unittest.TestCase):

    def setUp(self):
        self.subject = Subject()
        self.jogador1 = Jogador("Jogador 1")
        self.jogador2 = Jogador("Jogador 2")

        self.subject.attach(self.jogador1)
        self.subject.attach(self.jogador2)

        self.assertIn(self.jogador1)
        self.assertIn(self.jogador2)
    
    def removerJogador(self):
        self.subject = Subject()
        self.jogador1 = Jogador("Jogador 1")
        self.jogador2 = Jogador("Jogador 2")
    
        self.subject.disattach(self.jogador1)
        self.subject.disattach(self.jogador2)

        self.assertIn(self.jogador1)
        self.assertIn(self.jogador2)

    
    def notificaCor(self): 
         mensagem = "A cor azul foi escolhida"
         self.subject.notify(mensagem)
         print(mensagem)
         self.assertIn(mensagem, self.jogador1.notifications)
         self.assertIn(mensagem, self.jogador2.notifications)

if __name__ == '__main__':
    unittest.main()