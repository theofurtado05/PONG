import pygame
import time
import sys

from jogo.cores import CORES

class Placar:
    def __init__(self) -> None:
        self.p1 = 0
        self.p2 = 0

    def atualiza(self, paletas, bola):
        """
        Atualiza o placar conforme a posição da bola e das paletas.
        Retorna True se o placar foi atualizado, e False se não foi.
        """
        if self.verifica_posicao(paletas[0], bola, 35):
            self.p2 += 1
            return True

        if self.verifica_posicao(paletas[1], bola, 565):
            self.p1 += 1
            return True

            
        return False

    def mostra_vencedor(self, tela):
        fonte = pygame.font.SysFont(None, 40)
        p1_vencedor = fonte.render("Player 1 ganhou!", True, CORES.branco)
        p2_vencedor = fonte.render("Player 2 ganhou!", True, CORES.branco)

        if self.p1 == 5:
            tela.fill(CORES.preto)
            tela.blit(p1_vencedor, (200, 20))
            

        if self.p2 == 5:
            tela.fill(CORES.preto)
            tela.blit(p2_vencedor, (200, 20))
            
        
    def verifica_posicao(self, paleta, bola, limite):
        """
        Verifica se a bola está colidindo no limite e se está na paleta.
        Retorna False caso não esteja encontrando na paleta.
        """
        if bola.posicao[0] == limite:
            if paleta.posicao[1] <= bola.posicao[1] <= paleta.posicao[1] + paleta.altura:
                return False

            return True

        return False

    def desenha(self, tela):
        # define a fonte. None significa que vamos usar a fonte padrão
        fonte = pygame.font.SysFont(None, 30)

        # renderizamos o placar. Veja que usamos a função str() para converter
        # o valor numético para string
        p1_fonte = fonte.render(str(self.p1), True, CORES.vermelho)
        p2_fonte = fonte.render(str(self.p2), True, CORES.vermelho)

        # blit é usado para determinar a posição em que o texto vai ser
        # desenhado
        tela.blit(p1_fonte, (5, 20))
        tela.blit(p2_fonte, (585, 20))
        self.mostra_vencedor(tela)
