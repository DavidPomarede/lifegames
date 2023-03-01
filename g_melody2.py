from scamp import *
import random

# construct a session object
s = Session()

# add new parts to the session
violin = s.new_part("Violin")
sax = s.new_part("Saxophone")
brass = s.new_part("Brass")
piano = s.new_part("Piano")
bass = s.new_part("Bass")
drums = s.new_part("Drums")

# define sequences for each part
def sequence_violin():
    for pitch in [80, 55, 112, 45, 97, 78, 66, 33,
                  91, 60, 72, 123, 40, 105, 83, 47,
                  99, 62, 88, 41, 75, 110, 54, 71,
                  58, 122, 76, 39, 93, 116, 43, 89,
                  118, 44, 92, 67, 113, 56, 79, 32,
                  115, 50, 106, 84, 65, 103, 70, 36,
                  53, 98, 77, 38, 86, 120, 48, 68,
                  121, 46, 107, 64, 81, 95, 42, 73]:
        dur = random.uniform(0.05, 0.5)
        violin.play_note(pitch, 1, dur)

def sequence_sax():
    for pitch in [80, 55, 112, 45, 97, 78, 66, 33,
                  91, 60, 72, 123, 40, 105, 83, 47,
                  99, 62, 88, 41, 75, 110, 54, 71,
                  58, 122, 76, 39, 93, 116, 43, 89,
                  118, 44, 92, 67, 113, 56, 79, 32,
                  115, 50, 106, 84, 65, 103, 70, 36,
                  53, 98, 77, 38, 86, 120, 48, 68,
                  121, 46, 107, 64, 81, 95, 42, 73]:
        dur = random.uniform(0.02, 0.1)
        sax.play_note(pitch, 1, dur)

def sequence_brass():
    brass.play_note(80, 1, 30)

def sequence_piano():
    for pitch in [48, 51, 55, 58]:
        dur = random.uniform(0.1, 0.5)
        piano.play_note(pitch, 1, dur)

def sequence_bass():
    for pitch in [40, 43, 47, 50]:
        dur = random.uniform(0.2, 0.6)
        bass.play_note(pitch, 1, dur)

def sequence_drums():
    for i in range(8):
        drums.play_note("kick", 1, 0.2)
        drums.play_note("snare", 1, 0.2)
        
fork(sequence_violin)
fork(sequence_sax)
fork(sequence_brass)
fork(sequence_piano)
fork(sequence_bass)
sequence_drums()        

