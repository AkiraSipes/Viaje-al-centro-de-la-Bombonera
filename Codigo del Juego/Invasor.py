import pygame
from Proyectil import Proyectil
from random import randint

class Invasor(pygame.sprite.Sprite):
    def __init__(self,posX,posY,distancia,imagenUno,imagenDos):
        pygame.sprite.Sprite.__init__(self)
        self.imagenA=pygame.image.load(imagenUno)
        self.imagenB=pygame.image.load(imagenDos)
        self.listaImagenes=[self.imagenA,self.imagenB]
        self.posImagen=0
        self.imagenInvasor=self.listaImagenes[self.posImagen]
        self.rect=self.imagenInvasor.get_rect()
        self.velocidad=5
        self.listaDisparo=[]
        self.rect.top=posY
        self.rect.left=posX
        self.rangoDisparo=5
        self.tiempoCambio=1
        self.derecha=True
        self.contador=0
        self.maxDescenso=self.rect.top+40
        self.limiteDerecha=posX+distancia
        self.limiteIzquierda=posX-distancia
        self.conquista=False
    
    def dibujar(self,superficie):
        self.imagenInvasor=self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor,self.rect)
        
    def comportamiento(self,tiempo):
        if self.conquista==False:
            self.__movimiento()
            self.__ataque()
            if self.tiempoCambio==tiempo:
                self.posImagen+=1
                self.tiempoCambio+=1
                if self.posImagen>len(self.listaImagenes)-1:
                    self.posImagen=0
                
    def __ataque(self):
        if (randint(0,100)<self.rangoDisparo):
            self.__disparo()
     
    def __disparo(self):
        x,y=self.rect.center
        miProyectil=Proyectil(x,y,'imagenes/disparob.jpg',False)
        self.listaDisparo.append(miProyectil)
        
    def __movimiento(self):
        if self.contador<3:
            self.__movimientoLateral()
        else:
            self.__descenso()    
    
    def __movimientoLateral(self):
        if self.derecha==True:
            self.rect.left=self.rect.left+self.velocidad
            if self.rect.left>self.limiteDerecha:
                self.derecha=False
                self.contador+=1
        else:
            self.rect.left=self.rect.left-self.velocidad
            if self.rect.left<self.limiteIzquierda:
                self.derecha=True
                
    def __descenso(self):
        if self.maxDescenso==self.rect.top:
            self.contador=0
            self.maxDescenso=self.rect.top+40
        else:
            self.rect.top+=1
