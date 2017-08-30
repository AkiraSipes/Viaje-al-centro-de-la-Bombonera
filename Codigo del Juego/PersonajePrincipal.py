import pygame
from Movimiento import EstadoAnimado,EstadoEstatico

class EntidadJuego(pygame.sprite.Sprite):

    def __init__(self,display):
        super(EntidadJuego,self).__init__()

        self.display=display
        self.states_dict={}
        self.current_state=None
        self.dx=0
        self.dy=0
        self.image=None
        self.jumping=False

    def set_current_state(self,key):
        self.current_state=self.states_dict[key]

    def impulse(self,dx,dy):
        self.dx=dx
        self.dy=dy

    def update(self,frames):
        raise NotImplementedError("The updated method must be called in any child class")

    def draw(self):
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.display.blit(self.image, (self.rect.x, self.rect.y))


class Personaje(EntidadJuego):

    def __init__(self,display,px,py):
        super(Personaje,self).__init__(display)

        self.speed=3.5 #velocidad del personaje
        self.walking_images=pygame.image.load('images/p1_walk_animation2.png')
        #carga la imagen del personaje
        self.number_of_sprites=4 #en esta imagen es 4
        #estado animado derecha e izquierda

        self.walking_right_state=EstadoAnimado(self.walking_images.subsurface(0,0,
                                               self.walking_images.get_width(),
                                               self.walking_images.get_height()/2),
                                               self.number_of_sprites, 400, "Caminando_Derecho")
        
        self.walking_left_state=EstadoAnimado(self.walking_images.subsurface(0,
                                              self.walking_images.get_height()/2,
                                              self.walking_images.get_width(),
                                              self.walking_images.get_height()/2),
                                              self.number_of_sprites, 400, "Caminando_Izquierdo")

        self.resting_right_state=EstadoEstatico(self.walking_images.subsurface(0,0,
                                                self.walking_images.get_width()/self.number_of_sprites,
                                                self.walking_images.get_height()/2),
                                               "Parado_Derecho")


        self.resting_left_state=EstadoEstatico(self.walking_images.subsurface(
                                               self.walking_images.get_width()*3/4,
                                               self.walking_images.get_height()/2,
                                               self.walking_images.get_width()/self.number_of_sprites,
                                               self.walking_images.get_height()/2),
                                               "Parado_Izquierdo")

        self.states_dict["Caminando_Derecho"]=self.walking_right_state
        self.states_dict["Caminando_Izquierdo"]=self.walking_left_state
        self.states_dict["Parado_Derecho"]=self.resting_right_state
        self.states_dict["Parado_Izquierdo"]=self.resting_left_state

        self.set_current_state("Parado_Izquierdo")
        self.image = self.current_state.get_sprite()
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py

        self.accelerating=False
        self.jumping=False


    def calculate_gravity(self):
        if self.dy==0:
            self.dy=1
        else:
            self.dy=self.dy+0.35

    def jump(self,jump_force):
        self.impulse(self.dx,-jump_force)

    def key_down(self,key):
        if key==pygame.K_UP:
            if not self.jumping:
                self.jump(10)
                self.jumping=True
        if key==pygame.K_DOWN:
            pass
        if key==pygame.K_RIGHT:
            self.set_current_state("Caminando_Derecho")
            self.dx=self.speed
        if key==pygame.K_LEFT:
            self.set_current_state("Caminando_Izquierdo")
            self.dx=-self.speed

    def key_up(self,key):
        if key==pygame.K_UP:
            pass
        if key==pygame.K_DOWN:
            pass
        if key==pygame.K_RIGHT:
            if self.dx>0:
                self.set_current_state("Parado_Derecho")
                self.dx=0
        if key==pygame.K_LEFT:
            if self.dx<0:
                self.set_current_state("Parado_Izquierdo")
                self.dx=0

    def update(self,frames):
        self.calculate_gravity()

        self.rect.x=self.rect.x+self.dx
        self.rect.y=self.rect.y+self.dy

        if self.rect.y+self.rect.height>self.display.get_height():
            self.rect.y=self.display.get_height()-self.rect.height
            self.jumping=False
            self.dy=0

        self.current_state.update(frames)
        self.image=self.current_state.get_sprite()

        

        
                
                
            

        
        
        
        
        
        
        
        

        
        
