from reaper_python import * 
from sws_python import * 
from state import State

# false = False
# true = True

def sendMsg(m, *args):
	temp = ""
	for arg in args:
		temp+= " " + str(arg)
	RPR_ShowConsoleMsg(str(m)+ temp + "\n")

def command(commandNumber):
	RPR_Main_OnCommand(commandNumber, 0)

def stop():
	RPR_OnStopButton();

def play():
	RPR_OnPlayButton();

def playState(): #parse the playState
	cur = RPR_GetPlayState()
	if cur == 0:	
		return "stopped"
	elif cur == 1:
		return "playing"
	elif cur == 2:
		return "paused"
	elif cur == 5:
		return "recording"
	elif cur == 6:
		return "record paused" #??? http://wiki.cockos.com/wiki/index.php/RPR_GetPlayStateEx
	else:
		return False

project = RPR_EnumProjects(-1, None, 1)[0] #return current project

def getCurrentLoop(full=False): #returns tBeginning and tEnd of current selection
	if full:
		return RPR_GetSet_LoopTimeRange(False, False,0,0,False)
	else:
		return (RPR_GetSet_LoopTimeRange(False, False,0,0,False)[2:4]); #only want elements 2 and 3

def findRegion(t1, t2): #given two times, find the region between them
#only the first two vars are needed (project and the region index youre examining)
#RPR_EnumProjectMarkers3(proj, idx, isrgnOut, posOut, rgnendOut, nameOut, markrgnindexnumberOut, colorOut) = 
#Int retval, ReaProject* proj, Int idx, Boolean isrgnOut, Float posOut, Float rgnendOut, String nameOut, Int markrgnindexnumberOut, Int colorOut)
	returnBool = 1 #this will keep the loop going until we hit an index where there's no region and we get a 0
	foundId = -1
	i=0
	while returnBool != 0:
		temp = (RPR_EnumProjectMarkers3(project,i,False,0,0,"",0,0))
		if temp[4] == t1 and temp[5] == t2: #4=starting position, 5=region ending position
			foundId = temp[7] #markerrgnindexnumber (as opposed to the idx which is its index in order)
		returnBool = temp[0]
		i += 1
	return foundId;

def getName(region):	
#file:///C:/Users/Kevin/AppData/Local/Temp/reascripthelp.html#SNM_GetProjectMarkerName
#returns true if found
#Boolean RPR_SNM_SetProjectMarker(ReaProject* proj, Int num, Boolean isrgn, Float pos, Float rgnend, String name, Int color)
	fast_Str = SNM_CreateFastString("")
	SNM_GetProjectMarkerName(project, region, True, fast_Str)
	marker_name = SNM_GetFastString(fast_Str)
	SNM_DeleteFastString(fast_Str)
	if len(marker_name) > 0:
		return marker_name
	else:
		return "(unnamed)"

def getCurrentName(): #convenience method
	return getName(findRegion(getCurrentLoop(True)[2],getCurrentLoop(True)[3]))

def moveCursor(): #move cursor to end of time range even if you pressed space bar to stop recording
    t2 = RPR_GetSet_LoopTimeRange(False, False,0,0,False)[3]
    RPR_SetEditCurPos(t2, False, False)
