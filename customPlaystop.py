from helpers import *

State.song = getCurrentName()

if playState() and playState() == "playing" or playState() == "recording":
	stop();
	State.set(record="0",playstop="0")
else:
	play();
	State.set(record="0",playstop="1")

State.broadcast()