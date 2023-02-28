# trying to run scamp in thonny

from scamp import *
# import the random module from
# the python standard library
import random

# construct a session object
s = Session()
# add a new violin part to the session
violin = s.new_part("Violin")
sax = s.new_part("Saxaphone")

for _ in range(2):  # loop twice
    for pitch in [80, 55, 112, 45, 97, 78, 66, 33,
91, 60, 72, 123, 40, 105, 83, 47,
99, 62, 88, 41, 75, 110, 54, 71,
58, 122, 76, 39, 93, 116, 43, 89,
118, 44, 92, 67, 113, 56, 79, 32,
115, 50, 106, 84, 65, 103, 70, 36,
53, 98, 77, 38, 86, 120, 48, 68,
121, 46, 107, 64, 81, 95, 42, 73]:
        # pick a duration between 0.5 to 1.5
        dur = random.uniform(0.05, 0.5)
        dur2 = random.uniform(0.02, 0.1)
        # play a note of that duration
        violin.play_note(pitch, 1, dur)
        sax.play_note(pitch, 1, dur2)
        # with probability of one half, wait for between 0 and 1 seconds
#        if random.random() < 0.5:
            # note that "wait" is the same here as "s.wait". What "wait" does it find the
            # clock operating on the given thread and call wait on that. In this case, that
            # clock is the Session as a whole.
#            wait(random.random())
