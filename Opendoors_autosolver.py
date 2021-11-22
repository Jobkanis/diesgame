from pynput.keyboard import Controller
from pygame import mixer
import pyautogui
import time

# If it works, don't touch it
# You have two seconds to make your browser the active window
time.sleep(2)
keyboard = Controller()
mixer.init()

# Specify music paths
SoundObj = mixer.Sound("C:/Users/fail.mp3")
FinishObj = mixer.Sound("C:/Users/win.mp3")

# I assume that you split your screen, place game window on left, script on right
# I assume resolution 1920x1080
# Checks the pixel right under the player if green, if that is the case, then falling and result found
def check_falling():
    # Check the pixel right under player
    im = pyautogui.screenshot()
    px = im.getpixel((460, 900))

    # If green, then falling
    if px == (49, 77, 121):
        return True
    else:
        return False

def overkill(n, times):
    def pressArrowRight(s):
        keyboard.press('d')
        
        # Time to reach door
        time.sleep(s)
        keyboard.release('d')
        keyboard.press('a')
        keyboard.release('a')

        # Delay for safetyaed
        time.sleep(0.025)

        check = check_falling()
        if check:
            print("Player is falling, solution found!")
            return True

        keyboard.press('e')
        keyboard.release('e')

    # All doors to open in order
    # Add found doors here
    for i, t in enumerate(times):
        if i == 0:
            res = pressArrowRight(1.2)
            if res:
                return True # Falling, result found
        else:
            if i == len(times) - 1:
                res = pressArrowRight(0.6 + t * 0.2)
                if res:
                    return True # Falling, result found
                SoundObj.play()
                time.sleep(1) # Play sound 1 second
                SoundObj.stop()
            else:
                res = pressArrowRight(0.6 + t * 0.2)
                if res:
                    return True # Falling, result found

    time.sleep(1)

# If you only want to do one run:
#overkill(0)

found = [1, 2, 3, 2, 3, 5, 1, 5, 8, 2, 6, 10, 4, 8, 5, 9, 13, 7, 13, 19, 3, 15, 10, 3, 17, 26, 24, 26, 14, 1, 2, 21, 9, 12, 5, 25, 3, 24, 9, 12, 8, 0]

print("Solver will try to solve 18 levels")
for i in range(18):
    # Level to solve by algorithm, leave it like this
    Level_to_solve = len(found)
    for n in range(1, Level_to_solve + 2):
        n = Level_to_solve - n + 2
        found[-1] = n
        print("Trying: " + str(found))
        
        #n = Level_to_solve - n

        start = time.time()
        print(n)
        res = overkill(n, found)

        if res:
            found[-1] = n - 1
            found.append(0)
            
            FinishObj.play()
            time.sleep(3) # Play sound 1 second
            FinishObj.stop()

            Level_to_solve += 1
            print("Result is {}".format(n - 1))
            print("Level to solve updated: " + str(Level_to_solve))
            
            # It the height is extreme (more than 20s falling), update this value!
            time.sleep(20)
            end = time.time()
            break
        
        end = time.time()
        print("Finished function in {} seconds".format(round(end - start - 1, 2)))
    
    print("Current found doors: " + str(found))
    print("LEVEL COMPLETED \n")