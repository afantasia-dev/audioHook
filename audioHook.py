import pygame, sys, pyaudio, math
import sounddevice as sd
import numpy as np

screen_width=1080
screen_height=1920
pygame.init()
screen = pygame.display.set_mode((1080, 1920))
pygame.display.set_caption("Hello World")


def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print(int(volume_norm))

def get_output_level():
    """Gets the current audio output level."""
    try:
        audio_data = sd.rec(1024, samplerate=44100, channels=1, dtype='float32',device=1)
        sd.wait()  # Wait for the recording to complete
        volume_norm = np.linalg.norm(audio_data) * 10
        return volume_norm
    except Exception as e:
        print(f"Error getting output level: {e}")
        return None

def draw_sine(amplitude):
   screen.fill((0,0,0))
   points=[]
   test = True

   if amplitude>10:
      for x in range(screen_width):
         y=screen_height/2+int(amplitude*math.sin(x*0.02))
         points.append((x,y))

   else:
      points.append((0,screen_height/2))
      points.append((screen_width,screen_height/2))

   pygame.draw.lines(screen,(255,255,255),True,points,3)
   pygame.display.flip()





while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
   

   level =(get_output_level()*7)
   amplitude=max(10,level)
   
   draw_sine(amplitude)

   pygame.display.update()

   if level is not None:
      print(f"Current output level: {level}")
  



   
