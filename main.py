import pygame
import os
import random
import pickle
from Object import *
from Front_car import *
from Fellow import *
from Player import *
from Background import *
from Animation import *
from tools import *
from constant import *
from behavior import *

pygame.mixer.init()


MAIN_MUSIC = pygame.mixer.Sound("sounds/main_music.wav")
MAIN_MUSIC.set_volume(0.01)
EXPLOSION_SOUNDS = []
for path in os.listdir("./sounds/explosions/"):
    s = pygame.mixer.Sound(os.path.join("sounds/explosions",path))
    s.set_volume(0.1)
    EXPLOSION_SOUNDS.append(s)


#road_speed, front_car_frequency, front_car_max_speed, player_x_speed, player_y_speed, duration



def tab_difficulty():

    yield (1, 0.2, 1, 8, 5, 100)
    yield (2, 0.2, 2, 8, 5, 100)
    yield (3, 0.3, 3, 8, 5, 100)
    yield (4, 0.3, 4, 8, 5, 100)
    yield (5, 0.4, 5, 8, 5, 100)
    yield (6, 0.4, 6, 8, 5, 100)
    yield (7, 0.5, 7, 8, 5, 100)
    yield (8, 0.5, 8, 8, 5, 100)
    yield (9, 0.5, 9, 8, 5, 100)
    yield (10, 0.5, 10, 8, 5, 100)
    yield (11, 0.5, 11, 8, 5, 100)
    yield (12, 0.5, 12, 8, 5, 100)
    yield (13, 0.5, 13, 8, 5, 100)
    yield (14, 0.5, 14, 8, 5, 100)
    yield (15, 0.5, 15, 8, 5, 100)
    yield (1, 0.5, 10, 8, 5, 160)
    yield (15, 2.5, 10, 12, 7, 500)
    yield (20, 3.5, 25, 20, 10, 500)
    yield (30, 4, 50, 20, 10, -1)

    """difficulty = (2, 0.2, 1, 8, 5, 100)
    yield difficulty

    while(True):

        i = (difficulty[0]+1,)
        coef = i[0]/difficulty[0]
        print("coef", coef)
        rest = tuple(el*coef for el in difficulty[1:])
        difficulty = i+rest
        print(difficulty)
        yield difficulty"""


def draw_ath(score, level, progress):
    print(progress)
    score_font = pygame.font.SysFont("comicsans", 70)
    level_font = pygame.font.SysFont("impact", 20)
    score_label = score_font.render("{0}m".format(score), 1, (255,255,255))
    level_label = level_font.render("Level {0}".format(level),1,(0,0,0))
    pygame.draw.rect(window, (0,255,0), (WIDTH - 150, score_label.get_height()+11, progress/100 * 145, 28))
    pygame.draw.rect(window, (0, 0, 0), (WIDTH - 150, score_label.get_height()+10, 145, 30), 3)
    window.blit(level_label, (WIDTH - 150 + (level_label.get_width() - 10), score_label.get_height()+10))
    window.blit(score_label, (WIDTH - score_label.get_width(), 0))

def draw_game_over(score, window):
    font = pygame.font.SysFont("comicsans", 70)
    game_over_label = font.render("GAME OVER !",1, (255,25,25))
    score_label = font.render("{0}".format(score),1,(255,255,255))
    window.blit(game_over_label, (WIDTH//2 - game_over_label.get_width()//2, HEIGHT//4 - game_over_label.get_height()//2))
    window.blit(score_label, (WIDTH//2 - score_label.get_width()//2, HEIGHT//3 - score_label.get_height()//2))

def main_menu():
    best = loadFile("score")
    play_font = pygame.font.SysFont("comicsans", 120)
    font = pygame.font.SysFont("comicsans", 60)
    play_label = play_font.render("PLAY",1,(255,100,100))
    Best_score_label = font.render("Best score",1,(255, 255, 255))
    score_label = font.render("{0}".format(best),1,(0, 0, 0))
    play = False
    tick = 0
    front_car_list = []
    fellow_list = []
    explosions_list = []
    difficulty = tab_difficulty()
    road_speed, front_car_frequency, front_car_max_speed, player_x_speed, player_y_speed, duration = next(difficulty)
    bg = Background(window, BACKGROUND_LIST)
    while not play:
        clock.tick(FPS)
        tick += 1

        #fix all the objects on the road
        move_object_list(0, road_speed, front_car_list)
        move_object_list(0, road_speed, explosions_list)

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game()

        if( random.uniform(0,1)>0.985  ):
            front_car_list.append(new_random_front_car(1, 10))
            fellow_list.append(Fellow(random.uniform(0, HEIGHT//2), random.choice(["left", "right"])))

        #compute all behavior and movements
        front_car_behavior(front_car_list, explosions_list, window)
        fellow_behavior(fellow_list, front_car_list, None, window)

        #draw all
        bg.vertical_scroll(road_speed)
        draw_object_list(front_car_list, window)
        draw_object_list(explosions_list, window)
        draw_object_list(fellow_list, window)
        window.blit(play_label, (WIDTH//2 - play_label.get_width()//2, HEIGHT//4 - play_label.get_height()//2))
        window.blit(Best_score_label, (WIDTH//2 - Best_score_label.get_width()//2, HEIGHT//4 + play_label.get_height()//2))
        window.blit(score_label, (WIDTH//2 - score_label.get_width()//2, HEIGHT//4 + play_label.get_height()//2 + Best_score_label.get_height()))
        pygame.display.flip()

def pause_menu():

    pygame.mixer.pause()
    pause_font = pygame.font.SysFont("comicsans", 90)
    pause_label = pause_font.render("PAUSE", 1, (255,255,255))
    window.blit(pause_label, (WIDTH//2 - pause_label.get_width()//2, HEIGHT//3 - pause_label.get_height()//2))
    pygame.display.flip()
    pause = True
    while pause:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.unpause()
                    pause = False

def game():
    run = True
    tick = 0
    front_car_list = []
    explosions_list = []
    player = Player(100,100, 8, 5, window)
    bg = Background(window, BACKGROUND_LIST)
    difficulty = tab_difficulty()
    road_speed, front_car_frequency, front_car_max_speed, player_x_speed, player_y_speed, duration = next(difficulty)
    total_duration = duration
    step = 1
    #main_menu()
    MAIN_MUSIC.play()
    while run:
        clock.tick(FPS)
        tick += 1
        if not player.destroyed:
            score = tick
        #difficulty change
        duration-=1
        if duration == 0 and not player.destroyed:
            road_speed, front_car_frequency, front_car_max_speed, player.x_speed, player.y_speed, duration = next(difficulty)
            total_duration = duration
            step += 1

        if tick%(FPS//front_car_frequency) == 0:
            front_car_list.append(new_random_front_car(1,front_car_max_speed))

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE and not player.destroyed:
                     player.disable_control()
                     pause_menu()
                 elif event.key == pygame.K_RETURN:
                     if score > loadFile("score"):
                         saveFile("score", score)
                     MAIN_MUSIC.stop()
                     main_menu()

            player.update_control(event)

        #computing
        #fix all the objects on the road
        move_object_list(0,road_speed,front_car_list)
        move_object_list(0,road_speed,explosions_list)
        player.move(0, road_speed*player.destroyed)

        #behavior control of all objects
        front_car_behavior(front_car_list, explosions_list, window)
        player_behavior(player, front_car_list, explosions_list)

        #draw all
        bg.vertical_scroll(road_speed)
        player.draw(window)
        draw_object_list(front_car_list, window)
        draw_object_list(explosions_list, window)
        if not player.destroyed:
            draw_ath(tick, step, 100 - ((duration/total_duration)*100))
        else:
            draw_game_over(score, window)
        pygame.display.flip()


pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))
main_menu()
