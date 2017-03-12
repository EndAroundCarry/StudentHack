import pygame
import mail
import time
import cv2
#variabile
detectat = False
timplipsadetectie =0
poza =True
raw_input("Press Enter to continue...")
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)
# Initialize the game engine
pygame.init()
# Define the colors we will use in RGB format
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
YELOW = (218, 165, 32)
# Set the height and width of the screen
lenghtx=1280
lenghty=720
screen = pygame.display.set_mode([lenghtx, lenghty])

pygame.display.set_caption("Future Bell")

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
#Initialization of sound
pygame.mixer.init()
def dume(numarfete):
    global detectat ,timplipsadetectie,poza
    if detectat:
        print "Fete = {0}".format(numarfete)
        if numarfete > 0:
            ochi()
        elif numarfete == 0:
            timplipsadetectie +=1
            if timplipsadetectie > 100:
                detectat = False
                boord(0)
                timplipsadetectie=0
                poza =True

    else:
        boord(numarfete)
def boord(numar):
    global detectat
    if numar !=0:
        detectat =True
        smile()
    screen.fill(YELOW)
    pygame.draw.rect(screen, BLACK, [520, 210, 60, 60])
    pygame.draw.rect(screen, BLACK, [820, 210, 60, 60])
    pygame.draw.rect(screen, BLACK, [(lenghtx/2)-100, (lenghty/2)+100, 300, 30])
    pygame.draw.rect(screen, BLACK, [(lenghtx/2)+160, (lenghty/2)-180, 110, 22])
    pygame.draw.rect(screen, BLACK, [(lenghtx/2)-155, (lenghty/2)-180, 110, 22])

    pygame.display.update()
    pygame.display.flip()
def plans():
    screen.fill(YELOW)
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        pygame.mixer.music.load("getoutoffmypropriety.mp3")
        pygame.mixer.music.play()

    pygame.draw.rect(screen, BLACK, [520, 210, 60, 60])
    pygame.draw.rect(screen, BLACK, [820, 210, 60, 60])
    pygame.draw.rect(screen, BLUE, [825, 255, 50, 40])
    pygame.draw.rect(screen, BLACK, [(lenghtx/2)-100, (lenghty/2)+100, 300, 30])
    pygame.draw.rect(screen, BLACK, [(lenghtx/2)+230, (lenghty/2)+160, 30, 30])
    pygame.draw.rect(screen, BLACK, [(lenghtx/2)+200, (lenghty/2)+130, 30, 30])
    pygame.draw.rect(screen, BLACK, [(lenghtx/2)-160, (lenghty/2)+160, 30, 30])
    pygame.draw.rect(screen, BLACK, [(lenghtx/2)-130, (lenghty/2)+130, 30, 30])

    pygame.display.update()
    pygame.display.flip()
    while pygame.mixer.music.get_busy():
        pass

def smile():
    screen.fill(YELOW)

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        pygame.mixer.music.load("getoutoffmypropriety.mp3")
        pygame.mixer.music.play()

    # pygame.mixer.music.unpause()

    for x in range(0, 3):
         pygame.draw.rect(screen, BLACK, [520, 180+x*30, 40, 30])
    for x in range(0, 3):
         pygame.draw.rect(screen, BLACK, [820, 180+x*30, 40, 30])

    pygame.draw.rect(screen, BLACK, [(lenghtx/2)-100, (lenghty/2)+100, 300, 30])
    pygame.draw.rect(screen, BLACK, [(lenghtx/2)+230, (lenghty/2)+40, 30, 30])
    pygame.draw.rect(screen, BLACK, [(lenghtx/2)+200, (lenghty/2)+70, 30, 30])
    pygame.draw.rect(screen, BLACK, [(lenghtx/2)-160, (lenghty/2)+40, 30, 30])
    pygame.draw.rect(screen, BLACK, [(lenghtx/2)-130, (lenghty/2)+70, 30, 30])

    pygame.display.update()
    pygame.display.flip()
    while pygame.mixer.music.get_busy():
            pass
    # pygame.mixer.music.stop()

def ochi():
    screen.fill(YELOW)
    # pygame.mixer.music.pause()
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        pygame.mixer.music.load("somestrangepeopleareatyouredoor.mp3")
        pygame.mixer.music.play()
    pygame.draw.rect(screen, BLACK, [520, 210, 60, 60])
    pygame.draw.rect(screen, BLACK, [820, 230, 80, 30])
    pygame.draw.rect(screen, BLACK, [(lenghtx/2)-100, (lenghty/2)+100, 300, 30])
    pygame.draw.rect(screen, BLACK, [(lenghtx/2)+230, (lenghty/2)+40, 30, 30])
    pygame.draw.rect(screen, BLACK, [(lenghtx/2)+200, (lenghty/2)+70, 30, 30])


    pygame.display.update()
    pygame.display.flip()
    # pygame.mixer.music.stop()
    while pygame.mixer.music.get_busy():
        pass
def close():
    video_capture.release()
    cv2.destroyAllWindows()
    pygame.quit()


boord(0)
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    clock.tick(10)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(60, 60),
    )
    a = len(faces)
    if poza and a >0:
         poza = False
         cv2.imwrite("fatavecin.jpg", frame)
         mail.mail()

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display the resulting frame
    cv2.imshow('Video', frame)
    dume(a)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        close()
        break

