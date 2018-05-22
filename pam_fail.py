#!/usr/bin/python2
import sys
import os
import pygame
import pygame.camera
import datetime
import gnupg

EMAILADDR = 'XXXX@XXX.XXX'
TEMPFILE = '/dev/shm/aaaaa.jpg'
OUTPUT = '/opt/logs'

def capture(filename):
    pygame.camera.init()
    camlist = pygame.camera.list_cameras()
    if len(camlist) == 0:
        return None
    cam = pygame.camera.Camera(camlist[0])
    cam.start()
    surface = pygame.Surface(cam.get_size())
    img = cam.get_image(surface)
    cam.stop()
    pygame.image.save(img, filename)
    return filename

def encrypt(infile, outfile):
    gpg = gnupg.GPG()
    open('/dev/shm/aa', 'wb').write(str(gpg.list_keys()))
    encrypted = gpg.encrypt(open(infile, 'rb').read(), 'pierrehpezier@gmail.com')
    open(outfile, 'wb').write(str(encrypted))
    os.unlink('/dev/shm/aa')


def logincident():
    filename = os.path.join(OUTPUT,
                            '{}.bin'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))
    encrypt(capture(TEMPFILE), filename)
    pygame.display.quit()
    os.unlink(TEMPFILE)

if __name__ == '__main__':
    try:
        logincident()
    except e:
        open(os.path.join(OUTPUT, 'err.log'), 'ab+').write(str(a))
    sys.exit(0)
