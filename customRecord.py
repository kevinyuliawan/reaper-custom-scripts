import win32gui
import win32con
import win32api
import rtmidi_python as rtmidi

def sendMsg(m):
    RPR_ShowConsoleMsg(str(m)+"\n")

def waitAction(device):
    win32api.GetAsyncKeyState(win32con.VK_SPACE) #initial call to GetAsyncKeyState to reset the state
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
            if win32api.GetAsyncKeyState(win32con.VK_SPACE): #return if space bar is pressed
              return;
            if device >= 0:
                midi_message, delta_time = rtmidi.MidiIn().get_message()
                if midi_message:
                    sendMsg(midi_message, delta_time)
            found, msg = win32gui.PeekMessage(0, 0, 0, win32con.PM_REMOVE)
            if found:
                win32gui.TranslateMessage(msg)
                win32gui.DispatchMessage(msg);
        RPR_Main_OnCommand(40667, 0)#stop and save once you get to the end

def moveCursor():
    t2 = RPR_GetSet_LoopTimeRange(False, False,0,0,False)[3]
    RPR_SetEditCurPos(t2, False, False)
    
def setupMidi():
    # for loop in range(pypm.CountDevices()):
        # interf,name,inp,outp,opened = pypm.GetDeviceInfo(loop)
        # sendMsg(loop)
    midi_in = rtmidi.MidiIn()
    for i in range(len(midi_in.ports)):
        if "Oxygen 25" in midi_in.ports[i]:
            #midi_in.open_port(i) #this causes it to crash
            return i
    #midi_in.open_port(0)
 # for i in range( pygame.midi.get_count() ):
    # r = pygame.midi.get_device_info(i)
    # name, input = r[1:3]
    # if input and "Oxygen 25" in str(name):
      # return i;
    

device = setupMidi()
RPR_Main_OnCommand(40635, 0) #remove current time selection
RPR_Main_OnCommand(40839, 0) #move edit cursor forward one measure (if you're at the start of the region, this ensures you're ahead of it)
RPR_Main_OnCommand(53101, 0) #SWS: go to/select previous marker/region
RPR_Main_OnCommand(1013, 0) #transport record
waitAction(device)
#moveCursor() #move cursor to end of time range even if you pressed space bar to stop recording
RPR_Main_OnCommand(53100, 0) #SWS: go to/select next marker/region