import pyautogui
import time
import os 
dir_path=os.path.dirname(os.path.realpath(__file__))
pyautogui.hotkey('ctrl','shift','x')
time.sleep(1)
pyautogui.write('c++ testmate')
time.sleep(3)
point=None
while point is None:
    point=pyautogui.locateOnScreen(dir_path+"\\testmate.jpeg",confidence=0.7)
    
if point is not None:
        pyautogui.moveTo(point[0]+150,point[1]+50,duration=0.10)
        pyautogui.click(point[0]+150,point[1]+50,duration=0.10)
        time.sleep(1)

