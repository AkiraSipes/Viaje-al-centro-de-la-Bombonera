import pygame
from TamañoYColorPantalla import SKY_BLUE,SIZE
from PersonajePrincipal import Personaje
size=SIZE
screen=pygame.display.set_mode(size)#creacion de pantalla
pygame.display.set_caption("Viaje al centro de la bombonera")#titulo


class Main(object):
    def __init__(self):
        self.running=True #verifica si esta corriendo el programa
        self.clock=pygame.time.Clock() #define tiempos del juego,limita frames etc
        self.drawable_sprites=pygame.sprite.Group() #crea grupo de sprites,actualiza
        self.personaje=Personaje(screen,300,0)
        self.drawable_sprites.add(self.personaje)
        
    def keydown(self,event_key): #funcion que se ejecuta cuando se presiona una tecla
        self.personaje.key_down(event_key)

    def keyup(self,event_key): #funcion que se ejecuta cuando no se presiona una tecla
        self.personaje.key_up(event_key)

    def main(self):
        while (self.running):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                if event.type==pygame.KEYDOWN:
                    self.keydown(event.key)
                if event.type==pygame.KEYUP:
                    self.keyup(event.key)
            screen.fill(SKY_BLUE)   #pantalla azul
            frames=self.clock.tick(60) #limita frames

            self.personaje.update(frames) #actualiza personaje

            for sprite in self.drawable_sprites.sprites():
                sprite.draw()
            
            pygame.display.flip() #maneja buffers
        pygame.quit()    
            
if __name__=="__main__":
    main=Main()
    main.main()
            

            
            
                    
                    
        

