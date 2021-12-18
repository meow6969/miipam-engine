import pygame
import classes
import random
import cv2


def exponential(w):
    c = pygame.time.Clock()
    rika_chans = pygame.sprite.Group()
    x = random.randint(-300, 350)
    y = random.randint(70, 140)
    rika_chan = classes.rikachan(w, x, y)
    rika_chans.add(rika_chan)
    background = pygame.Rect(0, 0, 640, 480)
    background_image = pygame.image.load('content/bg.png')
    miipam = pygame.mixer.Sound("content/mipaa.flac")

    meowing = True
    while meowing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                meowing = False

        w.blit(background_image, background)
        for i in rika_chans:
            i.timer -= c.get_time()
            i.miipaaa -= c.get_time()
            if i.timer < 0:
                i.timer = random.randint(10000, 50000)
                x = random.randint(-300, 350)
                y = random.randint(70, 140)
                rika_chan = classes.rikachan(w, x, y)
                rika_chans.add(rika_chan)
            elif i.miipaaa < 0:
                i.miipaaa = random.randint(2000, 8000)
                i.mouth_state = True
                i.mouth = 1520
                if i.invert:
                    i.image = pygame.transform.flip(pygame.image.load('content/active.png'), True, False)
                else:
                    i.image = pygame.image.load('content/active.png')
                miipam.play()
            if i.mouth_state:
                i.mouth -= c.get_time()
                if i.mouth < 0:
                    i.mouth_state = False
                    if i.invert:
                        i.image = pygame.transform.flip(pygame.image.load(i.image_file), True, False)
                    else:
                        i.image = pygame.image.load(i.image_file)
        rika_chans.draw(w)

        pygame.display.flip()
        c.tick(60)
    pygame.mixer.stop()


def manual(w):
    c = pygame.time.Clock()
    rika_chans = pygame.sprite.Group()
    background = pygame.Rect(0, 0, 640, 480)
    background_image = pygame.image.load('content/bg.png')
    miipam = pygame.mixer.Sound("content/mipaa.flac")

    meowing = True
    while meowing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                meowing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # print('meow')
                    x, y = pygame.mouse.get_pos()
                    rika_chans.add(classes.rikachan(w, x - 320, y - 240))
                elif event.button == 3:
                    new_list = reversed(list(rika_chans))
                    x, y = pygame.mouse.get_pos()
                    for i in new_list:
                        if i.x + 200 < x < i.right - 200 and \
                                i.y + 90 < y < i.bottom and \
                                not i.mouth_state:
                            i.miipaaa = random.randint(2000, 4000)
                            i.mouth_state = True
                            i.mouth = 1520
                            if i.invert:
                                i.image = pygame.transform.flip(pygame.image.load('content/active.png'), True, False)
                            else:
                                i.image = pygame.image.load('content/active.png')
                            miipam.play()
                            break

        for i in rika_chans:
            i.miipaaa -= c.get_time()
            if i.miipaaa < 0:
                i.miipaaa = random.randint(2000, 4000)
                i.mouth_state = True
                i.mouth = 1520
                if i.invert:
                    i.image = pygame.transform.flip(pygame.image.load('content/active.png'), True, False)
                else:
                    i.image = pygame.image.load('content/active.png')
                miipam.play()
            if i.mouth_state:
                i.mouth -= c.get_time()
                if i.mouth < 0:
                    i.mouth_state = False
                    if i.invert:
                        i.image = pygame.transform.flip(pygame.image.load(i.image_file), True, False)
                    else:
                        i.image = pygame.image.load(i.image_file)

        w.blit(background_image, background)
        rika_chans.draw(w)

        pygame.display.flip()
        c.tick(60)
    pygame.mixer.stop()


def main_menu(w):
    c = pygame.time.Clock()
    background = pygame.Rect(0, 0, 640, 480)
    background_image = pygame.image.load('content/menu.png')

    comic_sans = pygame.font.SysFont('Comic Sans MS', 30)

    title = comic_sans.render('Rika-chan Engine!!!!!!', False, (0, 0, 0))

    exponential_mode = comic_sans.render("exponential growth rika chan mode", False, (0, 0, 0))

    manual_mode = comic_sans.render('manual rika chan mode', False, (0, 0, 0))

    video = comic_sans.render('view the original video!!!!!!!!', False, (0, 0, 0))

    # print(video.get_size())

    meowing = True
    while meowing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                meowing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # print('meow')
                x, y = pygame.mouse.get_pos()
                text_x, text_y = exponential_mode.get_size()

                # print(f"{x}, {y}")
                # print(f"{text_x}, {text_y}")

                # check if the user clicked "exponential mode"
                if text_x + 20 > x > 20 and \
                        text_y + 100 > y > 100:
                    exponential(w)
                    return

                # check if the user clicked "manual mode"
                if text_x + 20 > x > 20 and \
                        text_y + 150 > y > 150:
                    manual(w)
                    return

                # check if the user clicked "exponential mode"
                if text_x + 20 > x > 20 and \
                        text_y + 200 > y > 200:
                    view_video(w)
                    return

        w.blit(background_image, background)
        w.blit(title, (20, 10))

        w.blit(exponential_mode, (20, 100))
        w.blit(manual_mode, (20, 150))
        w.blit(video, (20, 200))

        pygame.display.flip()
        c.tick(60)


def view_video(w):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("content/miipam.flac")
    pygame.mixer.music.set_volume(.2)
    pygame.mixer.music.play()
    c = pygame.time.Clock()
    video = cv2.VideoCapture("content/miipam.mp4")
    fps = video.get(cv2.CAP_PROP_FPS)
    meowing = True
    while meowing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                meowing = False
        _, img = video.read()
        try:
            w.blit(pygame.image.frombuffer(img.tobytes(), (640, 480), "BGR"), (0, 0))
        except AttributeError:
            meowing = False
        pygame.display.flip()
        c.tick(fps)
    pygame.mixer.music.stop()
    pygame.mixer.music.load("content/msysri.ogg")
    pygame.mixer.music.set_volume(.2)
    pygame.mixer.music.play(-1)
