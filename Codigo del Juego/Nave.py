import pygame
from Proyectil import Proyectil
class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self,ancho,alto):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave=pygame.image.load('imagenes/nave.png')
        self.imagenDestruccion=pygame.image.load('imagenes/explosion.png')
        self.rect=self.imagenNave.get_rect()
        self.rect.centerx=ancho/2
        self.rect.centery=alto-30
        self.listaDisparo=[]
        self.vida=True
        self.velocidad=20
        self.sonidoDisparo=pygame.mixer.Sound('musica/player_wpn1.ogg')
        self.sonidoDestruccion=pygame.mixer.Sound('musica/player_dead.ogg')
    
    def movimientoDerecha(self):
        self.rect.left+=self.velocidad
        self.__movimiento()
    
    def movimientoIzquierda(self):
        self.rect.left-=self.velocidad
        self.__movimiento()
    
    def __movimiento(self):
        if self.vida==True:
            if self.rect.left<=0:
                self.rect.left=0
            elif self.rect.right>900:
                self.rect.right=899
    
    def disparar(self,x,y):
        miProyectil=Proyectil(x,y,'imagenes/disparoa.png',True)
        self.listaDisparo.append(miProyectil)
        self.sonidoDisparo.play()
    
    def destruccion(self):
        self.sonidoDestruccion.play()
        self.vida=False
        self.velocidad=0
        self.imagenNave=self.imagenDestruccion
    
    def dibujar(self,superficie):
        superficie.blit(self.imagenNave,self.rect)
