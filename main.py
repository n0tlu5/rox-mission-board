from PIL.ImageOps import grayscale
import pyautogui
import time
import sys

questPos = [(265,200), (520,215), (740,240), (945,185), (1120, 235), (220,460), (435,455), (635, 465), (870,455), (1050, 495)]

def imageExist(img):
    if(pyautogui.locateOnScreen(img)):
        return 1
    else:
        print("image does not exist. img: " + img + " not found!")
        return 0

def clickDelay(img, s, pos=None):
    try:
        if(pos):
            pyautogui.click(pos[0], pos[1])
        else:
            pyautogui.click(img)
        time.sleep(s)
    except:
        print("unable to click. img: " + img + " not found!")
        return -1

def autoPath():
    clickDelay("autopath/0.png", 1)
    if(imageExist("autopath/1.png")):
        clickDelay("autopath/1.png", 1)
        clickDelay("autopath/2.png", 1)
    else:
        clickDelay("autopath/3.png", 2)
        # missionBoard()

def terminal(cond):
    clickDelay("terminalConds/" + cond + ".png", 1)
    if(cond == "complete"):
        clickDelay("misc/submit.png", 5)
    elif(cond == "handOver"):
        clickDelay("misc/handOver.png", 5)

def missionBoard():
    clickDelay("missionBoard/0.png", 1)
    clickDelay("missionBoard/1.png", 1)
    clickDelay("missionBoard/2.png", 1)
    clickDelay("missionBoard/3.png", 1)
    while(not imageExist("missionBoard/4.png")):
        time.sleep(2)

def acceptMission(pos):
    clickDelay(None, 2, pos)
    if(not imageExist("acceptMission/1.png")):
        return -1
    clickDelay("acceptMission/1.png", 1)
    clickDelay("acceptMission/2.png", 1)

def completeMission(pos):
    clickDelay(None, 2, pos)
    if(not imageExist("misc/submit.png")):
        return -1
    clickDelay("misc/submit.png", 1)

def main():
    for pos in questPos:
        if(not imageExist("terminalConds/missionBoard.png")):
            return -1
        acceptMission(pos)
        while(not imageExist("terminalConds/missionBoard.png")):
            if(imageExist("terminalConds/skip.png")):
                terminal("skip")
            elif(imageExist("terminalConds/hand.png")):
                terminal("hand")
                time.sleep(5)
            elif(imageExist("terminalConds/handOver.png")):
                terminal("handOver")
            elif(imageExist("autopath/0.png")):
                if(imageExist("misc/battle.png")):
                    time.sleep(30)
                autoPath()
                time.sleep(3)
        completeMission(pos)

if(__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)