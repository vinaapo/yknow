from pygame import *

okno = display.set_mode((600,600))

game = True
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self,pict, x,y):
        self.image = transform.scale(image.load(pict), (80,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lastx = self.rect.x
        self.lasty = self.rect.y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def control(self):
        self.ris()
        kn = key.get_pressed()
        if kn[K_LEFT] and self.rect.x > 0:
            self.lastx = self.rect.x
            self.rect.x -= 5
        if kn[K_RIGHT] and self.rect.x < 550:
            self.lastx = self.rect.x
            self.rect.x += 5
        if kn[K_UP] and self.rect.y > 0:
            self.lasty = self.rect.y
            self.rect.y -= 5
        if kn[K_DOWN] and self.rect.y < 550:
            self.lasty = self.rect.y
            self.rect.y += 5

class Wall(sprite.Sprite):
    def __init__(self, x,y, shir, vis):
        self.image = Surface((shir,vis))
        self.image.fill((50,55,200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))

fon = transform.scale(image.load('fon.PNG'), (600,600))
chp = Player(('bur.PNG'), 10,10)

steni = [
    Wall(100, 100, 100, 10),
    Wall(100, 100, 10, 100),
    Wall(100, 200, 300, 10),
    Wall(300 ,0, 10, 210),
    Wall(500, 100, 10, 210),
    Wall(200, 300, 10, 200),
    Wall(300, 300, 10, 300),
    Wall(400, 400, 10, 100),
    Wall(400, 400, 200, 10),
    Wall(400, 500, 100, 10),
    Wall(300, 300, 200, 10),
    Wall(0, 300, 200, 10),
    Wall(100, 400, 10, 200)
]

lose = False
win = False

font.init()
wr = font.Font(None, 60)

points = 0
hp = 50

from random import *

nagrada = []
for i in range(7):
    x1 = randint(0,10) * 45 + 10
    y1 = randint(0,10) * 45 + 10
    priz = GameSprite('apel.PNG', x1,y1)
    nagrada.append(priz)

class Enemy(GameSprite):
    def parol_hor(self, x1, x2):
        self.ris()
        if self.rect.x < x1:
            self.napr = 'pravo'
        if self.rect.x > x2:
            self.napr = 'vlevo'
        if self.napr == 'pravo':
            self.rect.x += 1.5
        if self.napr == 'vlevo':
            self.rect.x -= 1.5

vrag = Enemy('vrag.PNG', 450,450)

while game:
    okno.blit(fon, (0,0))
    textpoints = wr.render(str(points), True, (127,255,0))
    okno.blit(textpoints, (10,10))
    texthp = wr.render(str(hp), True, (255,0,0))
    okno.blit(texthp, (520,10))
    for pr in nagrada:
        pr.ris()
        if sprite.collide_rect(chp,pr):
            nagrada.remove(pr)
            points += 1
    for i in event.get():
        if i.type == QUIT:
            game = False
    chp.control()
    for w in steni:
        w.ris()
        if sprite.collide_rect(w, chp):
            chp.rect.x = chp.lastx
            chp.rect.y = chp.lasty
    vrag.parol_hor(300,400)
    if sprite.collide_rect(chp,vrag):
        hp -= 1
    if hp < 1:
        game = False
    display.update()
    clock.tick(60)
    