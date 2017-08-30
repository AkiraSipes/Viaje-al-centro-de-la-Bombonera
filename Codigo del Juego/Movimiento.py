import pygame

class Estado(object):
    def __init__(self):
        self.current_sprite=None #por ahora no hay sprite
        self.name=""

    def get_sprite(self):
        return self.current_sprite

    def get_name(self):
        return self.name

    def get_width(self): #retorna el tamaño del sprite
        return self.current_sprite.get_width()

    def get_height(self):
        return self.current_sprite.get_height() #retorna el peso del sprite

    def update(self,frames):
        pass

class EstadoAnimado(Estado):
    def __init__(self,images,number_of_sprites,speed,name):
        super(EstadoAnimado,self).__init__()

        self.images=images
        self.number_of_sprites=number_of_sprites
        self.speed=speed
        self.name=name
        self.current_sprite=self.images.subsurface(0,0,self.images.get_width()/self.number_of_sprites,self.images.get_height())

        self.width=self.images.get_width()/self.number_of_sprites
        self.height=self.images.get_height()
        self.is_loop=False
        self.current_delta=0

    def update(self,frames):
        self.current_delta=self.current_delta + frames

        if self.current_delta>self.speed:
            self.current_delta=0

        sprite_index=int((self.current_delta*self.number_of_sprites/self.speed))

        if sprite_index>self.number_of_sprites-1:
            sprite_index=self.number_of_sprites-1

        self.current_sprite=self.images.subsurface(
                              sprite_index*self.width,
                              0, self.width, self.height)

class EstadoEstatico(Estado):

    def __init__(self,image,name):
        super(EstadoEstatico,self).__init__()

        self.current_sprite=image
        self.name=name


        

        
        

            
            
        
        

        
    
    
    
    
        

    
        
        
        
    
    
