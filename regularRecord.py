from helpers import *

command(1013) #regular record
if playState() and playState() == "recording":
	State.set(record="1",playstop="1")
else:
	State.set(record="0",playstop="1")

State.broadcast()