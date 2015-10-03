import win32gui
import win32con
import win32api
import requests
import time
from helpers import *

class Stopped:
    manual = False

def waitAction():
    win32api.GetAsyncKeyState(win32con.VK_SPACE) #initial call to GetAsyncKeyState to reset the state
    win32api.GetAsyncKeyState(win32con.VK_F10)
    playState = RPR_GetPlayState();
    if playState and playState != 2: # playing/recording, not paused        
        dStart = RPR_GetPlayPosition();
        dStop = t1 = t2 = None
        t1, t2 = RPR_GetSet_LoopTimeRange(False, False,0,0,False)[2:4]; #only want elements 2 and 3
        if (t1 == t2):
            return;
        dStop = t2;

        #Check for cursor going past stop, user stopping, and looping around
        while RPR_GetPlayPosition() < dStop and RPR_GetPlayState() and RPR_GetPlayPosition() >= dStart:
            #Keep the UI updating
            if win32api.GetAsyncKeyState(win32con.VK_SPACE) or win32api.GetAsyncKeyState(win32con.VK_F10): #return if space bar is pressed
              Stopped.manual = True
              return;
            found, msg = win32gui.PeekMessage(0, 0, 0, win32con.PM_REMOVE)
            if found:
                win32gui.TranslateMessage(msg);
                win32gui.DispatchMessage(msg);
        command(40667)#stop and save once you get to the end


command(40635) #remove current time selection
command(40839) #move edit cursor forward one measure (if you're at the start of the region, this ensures you're ahead of it)
command(53101) #SWS: go to/select previous marker/region
command(1013) #transport record
State.set(record="1",playstop="1",song=getCurrentName()); State.broadcast();
waitAction()
if Stopped.manual == False: #only move if you didn't manually stop it (i.e. during practice and you stop, don't go to the next song)
    command(53100) #SWS: go to/select next marker/region
    win32api.keybd_event(win32con.VK_F1, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(win32con.VK_F1, 0, win32con.KEYEVENTF_KEYUP, 0)

#State.set(record="0",playstop="0",song=getCurrentName()); State.broadcast();