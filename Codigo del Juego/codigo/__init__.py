import pygame,sys
from pygame.locals import *
from random import randint
#variables globales
ancho=900
alto=480
listaEnemigo=[]
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class naveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave=pygame.image.load("imagenes/nave.jpg")
        self.imagenDestruccion=pygame.image.load("imagenes/explosion.jpg")
        self.rect=self.imagenNave.get_rect()
        self.rect.centerx=ancho/2
        self.rect.centery=alto-30
        self.listaDisparo=[]
        self.vida=True
        self.velocidad=20
        self.sonidoDisparo=pygame.mixer.Sound("musica/player_wpn1.ogg")
        self.sonidoDestruccion=pygame.mixer.Sound("musica/player_dead.ogg")
    
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
        miProyectil=proyectil(x,y,"imagenes/disparoa.jpg",True)
        self.listaDisparo.append(miProyectil)
        self.sonidoDisparo.play()
    
    def destruccion(self):
        self.sonidoDestruccion.play()
        self.vida=False
        self.velocidad=0
        self.imagenNave=self.imagenDestruccion
    
    def dibujar(self,superficie):
        superficie.blit(self.imagenNave,self.rect)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class proyectil(pygame.sprite.Sprite):
    def __init__(self,posX,posY,ruta,personaje):
        pygame.sprite.Sprite.__init__(self)
        self.imagenProyectil=pygame.image.load(ruta)
        self.rect=self.imagenProyectil.get_rect()
        self.velocidadDisparo=5
        self.rect.top=posY
        self.rect.left=posX
        self.disparoPersonaje=personaje
    
    def trayectoria(self):
        if self.disparoPersonaje==True:
            self.rect.top=self.rect.top-self.velocidadDisparo
        else:
            self.rect.top=self.rect.top+self.velocidadDisparo
    
    def dibujar(self,superficie):
        superficie.blit(self.imagenProyectil,self.rect)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////               
class invasor(pygame.sprite.Sprite):
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
        miProyectil=proyectil(x,y,"imagenes/disparob.jpg",False)
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
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def detenerTodo():
    for enemigo in listaEnemigo:
        for disparo in enemigo.listaDisparo:
            enemigo.listaDisparo.remove(disparo)
        enemigo.conquista=True        
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def cargarEnemigos():
    posx=100
    for x in range(1,5):
        enemigo=invasor(posx,100,40,"imagenes/marcianoA.jpg","imagenes/MarcianoB.jpg")
        listaEnemigo.append(enemigo)
        posx=posx+200
    posx=100
    for x in range(1,5):
        enemigo=invasor(posx,0,40,"imagenes/Marciano2A.jpg","imagenes/Marciano2B.jpg")
        listaEnemigo.append(enemigo)
        posx=posx+200
    posx=100
    for x in range(1,5):
        enemigo=invasor(posx,-100,40,"imagenes/Marciano3A.jpg","imagenes/Marciano3B.jpg")
        listaEnemigo.append(enemigo)
        posx=posx+200
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def SpaceInvader():
    pygame.init()
    ventana=pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Invasion Alienigena")
    pygame.mixer.music.load("musica/medley.mp3")
    pygame.mixer.music.play(3)
    fuente=pygame.font.SysFont("Arial",30)
    texto=fuente.render("Fin del Juego",0,(120,100,40))
    activar=True
    fondo=pygame.image.load("imagenes/Fondo.jpg")
    jugador=naveEspacial()
    cargarEnemigos()
    enJuego=True
    reloj=pygame.time.Clock()
    while activar:
        reloj.tick(60)
        tiempo=pygame.time.get_ticks()//1000
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if enJuego==True:
                if evento.type==pygame.KEYDOWN:
                    if evento.key==K_LEFT or evento.key==K_a:
                        jugador.movimientoIzquierda()
                    elif evento.key==K_RIGHT or evento.key==K_d:
                        jugador.movimientoDerecha()
                    elif evento.key==K_SPACE:
                        x,y=jugador.rect.center
                        jugador.disparar(x,y)
        ventana.blit(fondo,(0,0))
        jugador.dibujar(ventana)
        if len(jugador.listaDisparo)>0:
            for i in jugador.listaDisparo:
                i.dibujar(ventana)
                i.trayectoria()
                if i.rect.top<10:
                    jugador.listaDisparo.remove(i)
                else:
                    for enemigo in listaEnemigo:
                        if i.rect.colliderect(enemigo.rect):
                            listaEnemigo.remove(enemigo)
                            jugador.listaDisparo.remove(i)    
        if len(listaEnemigo)>0:
            for enemigo in listaEnemigo:
                enemigo.comportamiento(tiempo)
                enemigo.dibujar(ventana)
                if enemigo.rect.colliderect(jugador.rect):
                    jugador.destruccion()
                    enJuego=False
                    detenerTodo()
                if len(enemigo.listaDisparo)>0:
                    for x in enemigo.listaDisparo:
                        x.dibujar(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            enJuego=False
                            detenerTodo()
                        if x.rect.top>900:
                            enemigo.listaDisparo.remove(x)
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    enemigo.listaDisparo.remove(x)                
        if enJuego==False:
            pygame.mixer.music.fadeout(3000)
            ventana.blit(texto,(300,300))
        pygame.display.update()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
SpaceInvader()

                

    

