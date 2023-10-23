import pygame
import time


x_enemy = 490
y_enemy = 150

speed = 1


animation_count = 0


def enemy(x, y):
    # Все переменные, которые будут использоваться не только в этой функции, объявляем как глобальные
    global left_enemy
    global right_enemy
    global down_enemy
    global up_enemy

    global x_enemy
    global y_enemy

    if x_enemy > x and y_enemy > y:
        '''Условие, если координата x вражеского персонажа больше координаты x игрока 
    или координата y вражеского персонажа больше координаты y игрока'''
        left_enemy = True  # Отрисовываем анимацию перемещения влево
        right_enemy = False
        down_enemy = False
        up_enemy = False
        x_enemy -= speed  # Перемещаем вражеского персонажа влево
        y_enemy -= speed  # И одновременно перемещаем его вверх
    elif x_enemy < x and y_enemy < y:
        left_enemy = False
        right_enemy = True  # Отрисовываем анимацию перемещения вправо
        down_enemy = False
        up_enemy = False
        x_enemy += speed  # Перемещаем вражеского персонажа вправо
        y_enemy += speed  # И одновременно перемещаем его вниз
    elif x_enemy < x and y_enemy > y:
        left_enemy = False
        right_enemy = True  # Отрисовываем анимацию перемещения вправо
        down_enemy = False
        up_enemy = False
        x_enemy += speed  # Перемещаем вражеского персонажа вправо
        y_enemy -= speed  # И одновременно перемещаем его вверх
    elif x_enemy > x and y_enemy < y:
        left_enemy = True  # Отрисовываем анимацию перемещения влево
        right_enemy = False
        down_enemy = False
        up_enemy = False
        x_enemy -= speed  # Перемещаем вражеского персонажа влево
        y_enemy += speed  # И одновременно перемещаем его вниз
    elif x_enemy > x and y_enemy == y:
        left_enemy = True  # Отрисовываем анимацию перемещения влево
        right_enemy = False
        down_enemy = False
        up_enemy = False
        x_enemy -= speed  # Перемещаем вражеского персонажа влево
    elif x_enemy < x and y_enemy == y:
        left_enemy = False  # Отрисовываем анимацию перемещения влево
        right_enemy = True
        down_enemy = False
        up_enemy = False
        x_enemy += speed  # Перемещаем вражеского персонажа влево
    elif y_enemy < y and x_enemy == x:
        left_enemy = False  # Отрисовываем анимацию перемещения влево
        right_enemy = False
        down_enemy = False
        up_enemy = True
        y_enemy += speed  # Перемещаем вражеского персонажа влево
    elif y_enemy > y and x_enemy == x:
        left_enemy = False  # Отрисовываем анимацию перемещения влево
        right_enemy = False
        down_enemy = True
        up_enemy = False
        y_enemy -= speed  # Перемещаем вражеского персонажа влево
    else:
        left_enemy = False
        right_enemy = False
        down_enemy = False
        up_enemy = False

def draw_window():
    global animation_count
    global bullet_1

    # if animation_count + 1 >= 40:
    #    animation_count = 0


    # чтобы делать анимацию быстрее/медленне в 94 строке после // и в 96 умножай/дели на одно и то же число
    if left_enemy:  # Анимация перемещения влево
        window.blit(player_left_enemy[animation_count // 20 - 1], (x_enemy, y_enemy))
        animation_count += 1
        if animation_count == 40:
            animation_count = 0
    elif right_enemy:  # Анимация перемещения вправо
        window.blit(player_right_enemy[animation_count // 20 - 1], (x_enemy, y_enemy))
        animation_count += 1
        if animation_count == 40:
            animation_count = 0
    elif up_enemy:  # Анимация перемещения вверх
        window.blit(player_up_enemy[animation_count // 20 - 1], (x_enemy, y_enemy))
        animation_count += 1
        if animation_count == 40:
            animation_count = 0
    elif down_enemy:  # Анимация перемещения вниз
        window.blit(player_down_enemy[animation_count // 20 - 1], (x_enemy, y_enemy))
        animation_count += 1
        if animation_count == 40:
            animation_count = 0
    else:
        window.blit(player_stand_enemy, (x_enemy, y_enemy))  # Всегда отрисовываем персонажа, когда он не перемещается

    pygame.display.update()


class Object(pygame.sprite.Sprite):

    def __init__(self, x, y, file):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect(center=(x, y))

        self.dx = 0
        self.dy = 0

        self.Go = False
        self.Frame = 0

        self.Left = False
        self.Right = False
        self.Up = False
        self.Down = True

    def update(self, *args):
        if self.dx != 0:
            self.rect.x += self.dx
            self.dy = 0
        if self.dy != 0:
            self.rect.y += self.dy
            self.dx = 0

        if self.Right:
            file = 'right'
        elif self.Left:
            file = 'left'
        elif self.Up:
            file = 'up'
        elif self.Down:
            file = 'down'

        if self.Go:
            self.Frame += 0.2
            if self.Frame > 2:
                self.Frame -= 2

            Personnel = ['2.png', '3.png']
            self.image = pygame.image.load('Player/' + file + '/' + Personnel[int(self.Frame)]).convert_alpha()
        else:
            self.image = pygame.image.load('Player/' + file + '/main.png').convert_alpha()

        for object in colission_list:
            if self.rect.colliderect(object):
                if self.dx > 0:
                    self.rect.right = object.left
                if self.dx < 0:
                    self.rect.left = object.right
                if self.dy > 0:
                    self.rect.bottom = object.top
                if self.dy < 0:
                    self.rect.top = object.bottom

        self.dx = 0
        self.dy = 0


pygame.init()

player = Object(200, 200, './player/down/main.png')

Length = 900
Width = 900

window = pygame.display.set_mode((Length, Width))
pygame.display.set_caption('In house of death')

Start_location = pygame.image.load('./map/1.png')
location_coridor = pygame.image.load('./map/2.png')
Rules_location = pygame.image.load('./map/3.png')
coridor1 = pygame.image.load('./map/4.png')
coridor2 = pygame.image.load('./map/5.png')
coridor3 = pygame.image.load('./map/10.png')
coridor4 = pygame.image.load('./map/7.png')
Window_room = pygame.image.load('./map/9.png')
trap_room = pygame.image.load('./map/8.png')
coridor5 = pygame.image.load('./map/11.png')
main_room = pygame.image.load('./map/12.png')
kitchen = pygame.image.load('./map/13.png')
color_black = (0, 0, 0)

clock = pygame.time.Clock()

location = "start"
teleport_flag = True

teleport = pygame.Rect(0, 0, 111, 111)
teleport_pravila = pygame.Rect(0, 0, 20, 20)
teleport_coridor1 = pygame.Rect(0, 0, 20, 20)
teleport_coridor2 = pygame.Rect(0, 0, 20, 20)
teleport_coridor3 = pygame.Rect(0, 0, 20, 20)
teleport_coridor4 = pygame.Rect(0, 0, 20, 20)
teleport_Window_room = pygame.Rect(0, 0, 20, 20)
teleport_trap_room = pygame.Rect(0, 0, 20, 20)
teleport_coridor5 = pygame.Rect(0, 0, 20, 20)
teleport_main_room = pygame.Rect(0, 0, 20, 20)
teleport_kitchen = pygame.Rect(0, 0, 20, 20)

player_stand_enemy = pygame.image.load('./Monster/down/2.png')
player_right_enemy = [pygame.image.load(f'./Monster/right/{i}.png') for i in range(2, 4)]
player_left_enemy = [pygame.image.load(f'./Monster/left/{i}.png') for i in range(2, 4)]
player_up_enemy = [pygame.image.load(f'./Monster/down/{i}.png') for i in range(2, 4)]
player_down_enemy = [pygame.image.load(f'./Monster/up/{i}.png') for i in range(2, 4)]

while_time = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type not in [pygame.K_w, pygame.K_d, pygame.K_a, pygame.K_s]:
            player.Go = False
    window.fill(color_black)
    key = pygame.key.get_pressed()

    if key[pygame.K_d]:
        player.dx = 5
        player.Go = True

        player.Left = False
        player.Right = True
        player.Down = False
        player.Up = False

    if key[pygame.K_a]:
        player.dx = -5
        player.Go = True

        player.Left = True
        player.Right = False
        player.Down = False
        player.Up = False

    if key[pygame.K_w]:
        player.dy = -5
        player.Go = True

        player.Left = False
        player.Right = False
        player.Down = False
        player.Up = True

    if key[pygame.K_s]:
        player.dy = 5
        player.Go = True

        player.Left = False
        player.Right = False
        player.Down = True
        player.Up = False

    if key[pygame.K_RIGHT]:
        player.dx = 10
        player.Go = True

        player.Left = False
        player.Right = True
        player.Down = False
        player.Up = False

    if key[pygame.K_LEFT]:
        player.dx = -10
        player.Go = True

        player.Left = True
        player.Right = False
        player.Down = False
        player.Up = False

    if key[pygame.K_UP]:
        player.dy = -10
        player.Go = True

        player.Left = False
        player.Right = False
        player.Down = False
        player.Up = True

    if key[pygame.K_DOWN]:
        player.dy = 10
        player.Go = True

        player.Left = False
        player.Right = False
        player.Down = True
        player.Up = False

    window.blit(player.image, player.rect)

    if location == 'start':

        colission_list = []

        window.blit(Start_location, (0, 0))
        teleport = pygame.Rect(345, 0, 220, 115)

        wall1 = pygame.Rect(0, 0, 110, 1000)
        # pygame.draw.rect(window, (0, 2, 255), wall1)
        colission_list.append(wall1)

        wall2 = pygame.Rect(785, 0, 110, 1000)
        # pygame.draw.rect(window, (0, 2, 255), wall2)
        colission_list.append(wall2)

        wall3 = pygame.Rect(0, 780, 1000, 110)
        # pygame.draw.rect(window, (0, 2, 255), wall3)
        colission_list.append(wall3)

        wall4 = pygame.Rect(0, 0, 370, 120)
        # pygame.draw.rect(window, (0, 2, 255), wall4)
        colission_list.append(wall4)

        wall5 = pygame.Rect(530, 0, 350, 120)
        # pygame.draw.rect(window, (0, 2, 255), wall5)
        colission_list.append(wall5)


    elif location == 'coridor':
        colission_list.clear()
        window.blit(location_coridor, (0, 0))
        teleport = pygame.Rect(378, 800, 160, 400)

        wall1 = pygame.Rect(270, 0, 110, 1000)
        # pygame.draw.rect(window, (0, 2, 255), wall1)
        colission_list.append(wall1)

        wall2 = pygame.Rect(540, 0, 110, 1000)
        # pygame.draw.rect(window, (0, 2, 255), wall2)
        colission_list.append(wall2)

        teleport_pravila = pygame.Rect(381, 0, 160, 110)

    elif location == 'pravila':
        colission_list.clear()
        window.blit(Rules_location, (0, 0))
        teleport_pravila = pygame.Rect(568, 790, 220, 150)

        enemy(player.rect.x, player.rect.y)  # Вызываем функциию игрока
        draw_window()  # Отрисовываем все наше окно игры

        wall1 = pygame.Rect(0, 0, 110, 1000)
        # pygame.draw.rect(window, (0, 2, 255), wall1)
        colission_list.append(wall1)

        wall2 = pygame.Rect(0, 0, 900, 110)
        # pygame.draw.rect(window, (0, 2, 255), wall2)
        colission_list.append(wall2)

        wall3 = pygame.Rect(0, 680, 580, 660)
        # pygame.draw.rect(window, (0, 2, 255), wall3)
        colission_list.append(wall3)

        wall4 = pygame.Rect(790, 0, 540, 280)
        # pygame.draw.rect(window, (0, 2, 255), wall4)
        colission_list.append(wall4)

        wall5 = pygame.Rect(790, 400, 540, 1000)
        # pygame.draw.rect(window, (0, 2, 255), wall5)
        colission_list.append(wall5)

        teleport_coridor1 = pygame.Rect(790, 220, 200, 225)

    elif location == 'coridor1':
        colission_list.clear()
        window.blit(coridor1, (0, 0))
        teleport_coridor1 = pygame.Rect(0, 335, 129, 181)
        pygame.draw.rect(window, (0, 10, 20), teleport_coridor1)

        teleport_coridor2 = pygame.Rect(774, 336, 125, 180)
        pygame.draw.rect(window, (0, 10, 20), teleport_coridor2)

    elif location == 'coridor2':
        colission_list.clear()
        window.blit(coridor2, (0, 0))
        teleport_coridor2 = pygame.Rect(266, 710, 80, 140)

        teleport_coridor3 = pygame.Rect(348, 65, 79, 130)

        teleport_coridor5 = pygame.Rect(596, 65, 79, 130)

    elif location == 'coridor3':
        colission_list.clear()
        window.blit(coridor3, (0, 0))
        teleport_coridor3 = pygame.Rect(800, 469, 100, 230)

        teleport_coridor4 = pygame.Rect(340, 350, 220, 114)

        teleport_trap_room = pygame.Rect(0, 126, 110, 230)

    elif location == 'coridor4':
        colission_list.clear()
        window.blit(coridor4, (0, 0))
        teleport_coridor4 = pygame.Rect(390, 760, 180, 150)

        teleport_Window_room = pygame.Rect(395, 0, 180, 145)

    elif location == 'Window_room':
        colission_list.clear()
        window.blit(Window_room, (0, 0))
        teleport_Window_room = pygame.Rect(340, 752, 222, 160)

    elif location == 'trap_room':
        colission_list.clear()
        window.blit(trap_room, (0, 0))
        teleport_trap_room = pygame.Rect(752, 310, 300, 300)

    elif location == 'coridor5':
        colission_list.clear()
        window.blit(coridor5, (0, 0))
        teleport_coridor5 = pygame.Rect(0, 563, 90, 230)

        teleport_main_room = pygame.Rect(820, 120, 80, 210)

    elif location == 'main_room':
        colission_list.clear()
        window.blit(main_room, (0, 0))
        teleport_main_room = pygame.Rect(0, 160, 80, 140)

        teleport_kitchen = pygame.Rect(79, 840, 165, 100)

    elif location == 'kitchen':
        colission_list.clear()
        window.blit(kitchen, (0, 0))
        teleport_kitchen = pygame.Rect(88, 0, 160, 150)

    if player.rect.colliderect(teleport):
        if location == 'start':
            location = 'coridor'
            player.rect.y += 610
            continue

        if location == 'coridor':
            player.rect.y -= 600
            location = 'start'
            continue

    if player.rect.colliderect(teleport_pravila):

        if location == 'coridor':
            location = 'pravila'
            player.rect.y += 600
            player.rect.x += 200
            continue

        if location == 'pravila':
            location = 'coridor'
            player.rect.y -= 590
            player.rect.x -= 200
            continue

    if player.rect.colliderect(teleport_coridor1):

        if location == 'pravila':
            location = 'coridor1'
            player.rect.y += 125
            player.rect.x -= 600
            continue

        if location == 'coridor1':
            location = 'pravila'
            player.rect.y -= 125
            player.rect.x += 600
            continue

    if player.rect.colliderect(teleport_coridor2):

        if location == 'coridor1':
            location = 'coridor2'
            # player.rect.y += 335
            # player.rect.x -= 370
            continue

        if location == 'coridor2':
            location = 'coridor1'
            # player.rect.y -= 335
            # player.rect.x += 370
            continue

    if player.rect.colliderect(teleport_coridor3):

        if location == 'coridor2':
            location = 'coridor3'
            # player.rect.y += 420
            # player.rect.x += 10
            continue

        if location == 'coridor3':
            location = 'coridor2'
            # player.rect.y -= 420
            # player.rect.x -= 300
            continue

    if player.rect.colliderect(teleport_coridor4):

        if location == 'coridor3':
            location = 'coridor4'
            player.rect.y += 80
            player.rect.x -= 0
            continue

        if location == 'coridor4':
            location = 'coridor3'
            player.rect.y -= 150
            player.rect.x -= 0
            continue

    if player.rect.colliderect(teleport_Window_room):

        if location == 'coridor4':
            player.rect.y += 450
            player.rect.x += 0
            location = 'Window_room'
            continue

        if location == 'Window_room':
            player.rect.y -= 450
            player.rect.x += 0
            location = 'coridor4'
            continue

    if player.rect.colliderect(teleport_trap_room):

        if location == 'coridor3':
            location = 'trap_room'
            player.rect.y += 200
            player.rect.x += 600
            continue

        if location == 'trap_room':
            location = 'coridor3'
            player.rect.y -= 200
            player.rect.x -= 600
            continue

    if player.rect.colliderect(teleport_coridor5):

        if location == 'coridor2':
            location = 'coridor5'
            player.rect.y += 550
            player.rect.x -= 400
            continue

        if location == 'coridor5':
            location = 'coridor2'
            player.rect.y -= 530
            player.rect.x += 440
            continue

    if player.rect.colliderect(teleport_main_room):

        if location == 'coridor5':
            location = 'main_room'
            player.rect.y += 10
            player.rect.x -= 700
            continue

        if location == 'main_room':
            location = 'coridor5'
            player.rect.y -= 10
            player.rect.x += 700
            continue

    if player.rect.colliderect(teleport_kitchen):

        if location == 'main_room':
            location = 'kitchen'
            player.rect.y -= 600
            player.rect.x += 0
            continue

        if location == 'kitchen':
            location = 'main_room'
            player.rect.y += 600
            player.rect.x += 0
            continue

    player.update(Length - player.rect.height, colission_list)
    window.blit(player.image, player.rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
