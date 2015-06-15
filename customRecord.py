import win32gui
import win32con
import win32api
import requests

def sendMsg(m):
    RPR_ShowConsoleMsg(str(m)+"\n")

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
              return;
            found, msg = win32gui.PeekMessage(0, 0, 0, win32con.PM_REMOVE)
            if found:
                win32gui.TranslateMessage(msg)
                win32gui.DispatchMessage(msg);
        RPR_Main_OnCommand(40667, 0)#stop and save once you get to the end

def moveCursor():
    t2 = RPR_GetSet_LoopTimeRange(False, False,0,0,False)[3]
    RPR_SetEditCurPos(t2, False, False)
    
RPR_Main_OnCommand(40635, 0) #remove current time selection
RPR_Main_OnCommand(40839, 0) #move edit cursor forward one measure (if you're at the start of the region, this ensures you're ahead of it)
RPR_Main_OnCommand(53101, 0) #SWS: go to/select previous marker/region
RPR_Main_OnCommand(1013, 0) #transport record
r = requests.post("http://localhost:5000/actions/updatestate",  data={'record': 1, 'playstop':1})
# sendMsg(r.status_code)
# sendMsg(r.reason)
waitAction()
requests.post("http://localhost:5000/actions/updatestate", data={'record':0, 'playstop':0}) 
#moveCursor() #move cursor to end of time range even if you pressed space bar to stop recording
RPR_Main_OnCommand(53100, 0) #SWS: go to/select next marker/region