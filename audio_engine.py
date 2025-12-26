import pygame

class AudioEngine:
    def __init__(self, sound_files):
        pygame.mixer.init()
        # Pre-load sounds into memory
        self.sounds = [pygame.mixer.Sound(f) for f in sound_files]

    def play(self, index):
        if 0 <= index < len(self.sounds):
            self.sounds[index].play()