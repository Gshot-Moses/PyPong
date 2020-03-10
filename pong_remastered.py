import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, ball, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(ball)
        self.rect = self.image.get_rect()
        self.speed = [5, 5]
        self.rect.left, self.rect.bottom = location
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > screen[0]:
            self.speed[0] = -self.speed[0]
        
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]
        
class Paddle(pygame.sprite.Sprite):
    def __init__(self, location):
        self.surface = pygame.surface.Surface([100,20])
        self.image = self.surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = location

class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('box.jpg')
        self.display = display_surf
        self.rect = self.image.get_rect()
        self.width = self.image.get_size()[0]
        self.height = self.image.get_size()[1]
        self.display_rect = self.display.get_rect()
        

    #def blitme(self):
    #    display_surf.blit(self.img, self.rect)
    
screen = [640,480]
pygame.init()
display_surf = pygame.display.set_mode(screen)
display_surf.fill([255,255,255])
box = Box()
boxes = pygame.sprite.Group()
ball = 'ball.jpg'
score = 0
score_font = pygame.font.SysFont('arial', 18)
step = 30
paddle_pos = [320,screen[1] - step]
ball_pos = [320,300]
ball_instance = Ball(ball, ball_pos)
paddle_instance = Paddle(paddle_pos)
group = pygame.sprite.Group(ball_instance)
clock = pygame.time.Clock()
for x in range(60,595,box.width):
    for y in range(30,200,box.height):
        box = Box()
        box.rect.x = x
        box.rect.y = y
        #display_surf.blit(box.img, [x,y])
        boxes.add(box)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
			
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
        paddle_instance.rect.left -= 10
        if paddle_instance.rect.left <= 5:
            paddle_instance.rect.left = 5
    elif pressed[pygame.K_d]:
        paddle_instance.rect.left += 10
        if paddle_instance.rect.right >= 635:
            paddle_instance.rect.right = 635
	elif pressed[pygame.K_ESCAPE]:
		running = False
    display_surf.fill([255,255,255])
    display_surf.blit(ball_instance.image, ball_instance.rect)
    display_surf.blit(paddle_instance.image, paddle_instance.rect)
    score_text = score_font.render('Score:' + str(score), True, [0,0,0]) 
    #display_surf.blit(box.img, [320,100])
    if pygame.sprite.spritecollide(paddle_instance, group, False):
        #ball_instance.speed[0] *= -1
        ball_instance.speed[1] *= -1
    collisions = pygame.sprite.groupcollide(boxes, group, True, False)
    if collisions:
        #ball_instance.speed[0] *= -1
        ball_instance.speed[1] *= -1
        score += 1
    boxes.draw(display_surf)
    ball_instance.move()
    display_surf.blit(score_text, [10,10])
    pygame.display.update()
    clock.tick(30)
pygame.quit()
