# turn a process into a tool

from scamp import *

s = Session ( )

s. tempo = 120

violin = s.new part("violin" )

# pitches and durations from the opening of the Sibelius violin concerto

pitches = [79, 81, 74, , 74, 77, 76, 77, 76, 74, 81, 84, 83, 81, 80, 81, 86, 88, 84, 83, 81, 80, 81, 81]

durations = [3.5, 0.5, 5, 1, 1.5, 0.5/3, 0.5/3, 0.5/3, 5, 1, 1.5, 0.5, 1.5, 0.25, 0.25, 3, 1, 1.5, 0.5, 1.5, 0.25, 0.25, 4]

for pitch, dur in zip(pitches, durations) :
	violin.play_note(pitch, 0.75, dur)
