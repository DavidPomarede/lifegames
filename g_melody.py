from scamp import *
import random

s = Session()

violin = s.new_part("Violin")
sax = s.new_part("Saxaphone")
brass = s.new_part("Brass")

# define sequences
def sequence1():
    for pitch in [80, 55, 112, 45, 97, 78, 66, 33,
                  91, 60, 72, 123, 40, 105, 83, 47,
                  99, 62, 88, 41, 75, 110, 54, 71,
                  58, 122, 76, 39, 93, 116, 43, 89,
                  118, 44, 92, 67, 113, 56, 79, 32,
                  115, 50, 106, 84, 65, 103, 70, 36,
                  53, 98, 77, 38, 86, 120, 48, 68,
                  121, 46, 107, 64, 81, 95, 42, 73]:
        dur = random.uniform(0.5, 1.5)
        violin.play_note(pitch, 1, dur)

def sequence2():
    for pitch in [80, 55, 112, 45, 97, 78, 66, 33,
                  91, 60, 72, 123, 40, 105, 83, 47,
                  99, 62, 88, 41, 75, 110, 54, 71,
                  58, 122, 76, 39, 93, 116, 43, 89,
                  118, 44, 92, 67, 113, 56, 79, 32,
                  115, 50, 106, 84, 65, 103, 70, 36,
                  53, 98, 77, 38, 86, 120, 48, 68,
                  121, 46, 107, 64, 81, 95, 42, 73]:
        dur2 = random.uniform(0.02, 0.1)
        sax.play_note(pitch, 1, dur2)

def sequence3():
    brass.play_note(80, 1, 30)

# create sequences
#s1 = Sequence(sequence1, repetitions=2)
#s2 = Sequence(sequence2, repetitions=2)
#s3 = Sequence(sequence3)

fork(sequence1)
fork(sequence3)
sequence2()

# add sequences to session
s.add_synth(s1, s2, s3)

# play session
s.play_for(120)
