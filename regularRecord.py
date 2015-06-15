from helpers import *

RPR_Main_OnCommand(1013, 0) #regular record
if playState() and playState() == "recording":
	State.set(record="1",playstop="1")
	
else:
	State.set(record="0",playstop="1")

State.broadcast()