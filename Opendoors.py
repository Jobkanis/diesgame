from pynput.keyboard import Controller
import time

# If it works, don't touch it
# You have to seconds to make your browser the axtive window
time.sleep(2)
keyboard = Controller()

def overkill(n):
    keyboard = Controller()
    def pressArrowRight(s):
        keyboard.press('d')

        # Time to reach door
        time.sleep(s)
        keyboard.release('d')
        keyboard.press('a')
        keyboard.release('a')

        # Delay for safety
        time.sleep(0.05)
        keyboard.press('e')
        keyboard.release('e')

    # All doors to open in order
    # Add found doors here
    times = [1, 2, 3, 2, 3, 5, 1, 5, 8, 2, 6, 10, 4, 8, 5, 9, 13, 7, 13, 19, 3, 15, 10, 3, 17, 26, 24, 26, 14, 1, 2, 21, 9, n]
    for i, t in enumerate(times):
        if i == 0:
            pressArrowRight(1.2)
        else:
            pressArrowRight(0.6 + t * 0.2)

    time.sleep(5)

# If you only want to do one run:
#overkill(0)

# Level to solve by algorithm
Level_to_solve = 35
for n in range(1, Level_to_solve):
    n = Level_to_solve - n

    start = time.time()
    print(n)
    overkill(n)
    end = time.time()
    print("Finished function in {} seconds".format(round(end - start - 5, 2)))

