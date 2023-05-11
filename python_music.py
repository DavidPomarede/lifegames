from scamp import *

s = Session(tempo=50)
clar = s.new_part("Clarinet")
s.start_transcribing()

melody = []

for pitch, duration in melody:
    clar.play_note(pitch, 0.7, duration)
    
s.stop_transcribing().to_score().show()