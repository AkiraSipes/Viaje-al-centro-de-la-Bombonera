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
negro=(0,0,0)
blanco=(255,255,255)
verde=(0,255,0)
#///////////////////////////////////////////////////////////////////////////////
#Creacion de ventana de Inicio
pygame.init()
pygame.display.set_caption("Invasion Alienigena")
ventana=pygame.display.set_mode((ancho,alto))
#///////////////////////////////////////////////////////////////////////////////
fuentechica=pygame.font.SysFont("Arial",25)
fuentemediana=pygame.font.SysFont("Arial",50)
fuentegrande=pygame.font.SysFont("Arial",80)
#///////////////////////////////////////////////////////////////////////////////
def menu():
    loopMenu=False
    while not loopMenu:
        pantalla()
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                pygame.quit()
                sys.exit()  
            if evento.type==pygame.KEYDOWN:
                if evento.key==pygame.K_RETURN:#return=enter
                    SpaceInvader()
                if evento.key==pygame.K_m:
                    while not loopMenu and not evento.key==K_RETURN:
                        manual()
                if evento.key==pygame.K_p:
                    pass
                if evento.key==pygame.K_s:
                    pygame.quit()
                    sys.exit()
#///////////////////////////////////////////////////////////////////////////////
def pantalla():
    pygame.display.update()
    ventana.fill(negro)
    mensaje("Invacion Alienigena",verde,desplazamientoY=-190,tamaño="grande")
    mensaje("MENU",blanco,-100,tamaño="mediano")
    mensaje("JUGAR Presione la tecla ENTER",blanco,-50,tamaño="chico")
    mensaje("MANUAL DE USO Presione la tecla M",blanco,-10,tamaño="chico")
    mensaje("PUNTAJE Presione la tecla P",blanco,30,tamaño="chico")
    mensaje("SALIR Presione la tecla S",blanco,70,tamaño="chico")
#///////////////////////////////////////////////////////////////////////////////
def objeto_texto(texto,color,tamaño):
    if tamaño=="chico":
        textSurface=fuentechica.render(texto,True,color)
    elif tamaño=="mediano":
        textSurface=fuentemediana.render(texto,True,color)
    elif tamaño=="grande":
        textSurface=fuentegrande.render(texto,True,color)
    return textSurface,textSurface.get_rect()
#///////////////////////////////////////////////////////////////////////////////
def mensaje(msg,color,desplazamientoY=0,tamaño="chico"):
    textSurf,textRect=objeto_texto(msg,color,tamaño)
    textRect.center=(ancho/2),(alto/2)+desplazamientoY
    ventana.blit(textSurf,textRect)
#///////////////////////////////////////////////////////////////////////////////
def puntajeJuego(puntaje):
      fuenteP=pygame.font.SysFont("Arial",25,True,False)
      contador=fuenteP.render("Puntaje: " + str(puntaje),0,blanco)
      ventana.blit(contador,(0,0))
#///////////////////////////////////////////////////////////////////////////////
def manual():
    ventana.fill(blanco)
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
                pygame.quit()
                sys.exit()  
        if evento.type==pygame.KEYDOWN:
            if evento.key==pygame.K_ESCAPE:
                menu()
    mensaje("Las teclas para mover la nave y disparar son:",negro,-50,tamaño="chico")
    mensaje("-Movimiento de la nave derecho TECLA FLECHA DERECHA o TECLA D",negro,-25,tamaño="chico")
    mensaje("-Movimiento de la nave izquierdo TECLA FLECHA IZQUIERDA o TECLA A",negro,0,tamaño="chico")
    mensaje("-Disparar misiles BARRA ESPACIADORA",negro,25,tamaño="chico")
    mensaje("Ir al menu presione la tecla Esc",negro,50,tamaño="chico")
    pygame.display.update()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def detenerTodo():
    for enemigo in listaEnemigo:
        for disparo in enemigo.listaDisparo:
            enemigo.listaDisparo.remove(disparo)
        enemigo.conquista=True        
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def nivelUno():
    posx=100
    for x in range(1,5):
        enemigo=Enemigo(posx,100,40,'imagenes/MarcianoA.png','imagenes/MarcianoB.png')
        listaEnemigo.append(enemigo)
        posx=posx+200
#////////////////////////////////////////////////////////////////////////////////
def nivelDos():
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
#///////////////////////////////////////////////////////////////////////////////        
def nivelTres():
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
    nivelTres()
    puntaje=0
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
        puntajeJuego(puntaje)
        if len(jugador.listaDisparo)>0:
            for i in jugador.listaDisparo:
                i.dibujar(ventana)
                i.trayectoria()
                if i.rect.top<10:
                    jugador.listaDisparo.remove(i)
                else:
                    for enemigo in listaEnemigo:
                        if i.rect.colliderect(enemigo.rect):
                            puntaje+=10
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
        else:
            if len(listaEnemigo)<=0:
                jugador.victoria=True
        #loop para reiniciar el juego si gana
        if jugador.victoria==True:
            if(pygame.time.get_ticks()-tiempo)>3000:#retardo para que la pantalla de game over no apraezca muy pronto
                fondo=pygame.image.load('imagenes/win.jpg')
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
                            menu()
        #loop para reiniciar el juego si pierde
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
                            menu()
        
        pygame.display.update()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
menu()
