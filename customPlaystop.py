import requests
from reaper_python import * 
from sws_python import * 

def sendMsg(m1, m2):
    RPR_ShowConsoleMsg(str(m1)+ ' ' + str(m2) + "\n")

playState = RPR_GetPlayState();
project = RPR_EnumProjects(-1, None, 1)[0]
sendMsg("project: ", project)
#RPR_EnumProjectMarkers3(proj, idx, isrgnOut, posOut, rgnendOut, nameOut, markrgnindexnumberOut, colorOut)
#Int retval, ReaProject* proj, Int idx, Boolean isrgnOut, Float posOut, Float rgnendOut, String nameOut, Int markrgnindexnumberOut, Int colorOut) = 

###  RPR_EnumProjectMarkers(idx, isrgn, pos, rgnend, name, markrgnindexnumber) =
### (Int retval, Int idx, Boolean isrgn, Float posOut, Float rgnendOut, String nameOut, Int markrgnindexnumberOut)
t1, t2 = RPR_GetSet_LoopTimeRange(False, False,0,0,False)[2:4]; #only want elements 2 and 3
ret = 1;
found = 0;
i=0;
temp = None
while ret != 0:
	temp = (RPR_EnumProjectMarkers3(project,i,False,0,0,"",0,0))
	if temp[4] == t1 and temp[5] == t2:
		found = temp[7]
	ret = temp[0]
	i = i+1

fast_Str = SNM_CreateFastString("")
SNM_GetProjectMarkerName(project, found, True, fast_Str)
marker_name = SNM_GetFastString(fast_Str)
SNM_DeleteFastString(fast_Str)

sendMsg("t1: ",t1)
sendMsg("t2: ",t2)
sendMsg("pos: ", temp[4])
sendMsg("rgnend: ", temp[5])
sendMsg("matching marker name: ",marker_name)


# sendMsg("retval: ", temp[0])
# sendMsg("proj: ", temp[1])
# sendMsg("idx: ", temp[2])
# sendMsg("isrgn: ", temp[3])

# sendMsg("name: ", temp[6])
# sendMsg("markrgnindexnumber: ", temp[7])
# sendMsg("color: ", temp[8])



# name = SNM_GetProjectMarkerName(project,0,True,"")
# sendMsg(name)
if playState and playState != 2: #playing/recording
	RPR_OnStopButton();
	requests.post("http://localhost:5000/actions/updatestate", data={'record':0, 'playstop':0, 'song':marker_name}) 
else:
	RPR_OnPlayButton()
	requests.post("http://localhost:5000/actions/updatestate", data={'record':0, 'playstop':1, 'song':marker_name}) 