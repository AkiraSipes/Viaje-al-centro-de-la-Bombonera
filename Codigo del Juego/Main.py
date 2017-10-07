"""Trabajo Practico Seminario de Lenguajes
Nombre del Juego: Invacion Alienigena
Integrantes del Grupo:Akira Molas-Esteban Rodriguez-Nicolas Romero-Oscar Ruina"""
import pygame,sys
from pygame.locals import *
from Nave import NaveEspacial
from Invasor import Invasor as Enemigo
#variables globales
ancho=900
alto=480
listaEnemigo=[]
#///////////////////////////////////////////////////////////////////////////////
#Creacion de ventana de Inicio
pygame.init()
pygame.display.set_caption("Invasion Alienigena")
ventana=pygame.display.set_mode((ancho,alto))
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
        enemigo=Enemigo(posx,100,40,'imagenes/MarcianoA.png','imagenes/MarcianoB.png')
        listaEnemigo.append(enemigo)
        posx=posx+200
    posx=100
    for x in range(1,5):
        enemigo=Enemigo(posx,0,40,'imagenes/Marciano2A.png','imagenes/Marciano2B.png')
        listaEnemigo.append(enemigo)
        posx=posx+200
    posx=100
    for x in range(1,5):
        enemigo=Enemigo(posx,-100,40,'imagenes/Marciano3A.png','imagenes/Marciano3B.png')
        listaEnemigo.append(enemigo)
        posx=posx+200
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def SpaceInvader():
    pygame.mixer.music.load('musica/medley.mp3')
    pygame.mixer.music.play(3)
    fondo=pygame.image.load('imagenes/Fondo.jpg')
    jugador=NaveEspacial(ancho,alto)
    cargarEnemigos()
    reloj=pygame.time.Clock()
    tiempo=pygame.time.get_ticks()
    salirJuego=False
    finJuego=False
    while not salirJuego:
        reloj.tick(60)
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if finJuego==False:
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
                    detenerTodo()
                    finJuego=True
                if len(enemigo.listaDisparo)>0:
                    for x in enemigo.listaDisparo:
                        x.dibujar(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            detenerTodo()
                            finJuego=True
                        if x.rect.top>900:
                            enemigo.listaDisparo.remove(x)
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    enemigo.listaDisparo.remove(x)                
        #loop para reiniciar el juego
        if finJuego==True:
            if(pygame.time.get_ticks()-tiempo)>3000:#retardo para que la pantalla de game over no apraezca muy pronto
                fondo=pygame.image.load('imagenes/gameover.jpg')
                ventana.blit(fondo,(0,0))
                pygame.mixer.music.fadeout(3000)
                if len(listaEnemigo)>0:
                    for enemigo in listaEnemigo:
                        listaEnemigo.remove(enemigo)
                    for enemigo in listaEnemigo:
                        listaEnemigo.remove(enemigo)
                    for enemigo in listaEnemigo:
                        listaEnemigo.remove(enemigo)
                for evento in pygame.event.get():
                    if evento.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()  
                    if evento.type==pygame.KEYDOWN:
                        if evento.key==pygame.K_c:
                            SpaceInvader()    
        pygame.display.update()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
SpaceInvader()

