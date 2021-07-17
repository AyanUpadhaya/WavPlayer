
from pygame import mixer

# external functionalities

def increase_volume(event):
    mixer.init()
    current_vol = mixer.music.get_volume()
    mixer.music.set_volume(current_vol+0.5)

def decrease_volume(event):
    mixer.init()
    current_vol = mixer.music.get_volume()
    mixer.music.set_volume(current_vol-0.5)
