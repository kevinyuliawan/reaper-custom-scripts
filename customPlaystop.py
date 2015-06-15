from helpers import *

State.song = getCurrentName()

if playState() and playState() == "playing" or playState() == "recording":
	RPR_OnStopButton();
	State.set(record="0",playstop="0")
else:
	RPR_OnPlayButton()
	State.set(record="0",playstop="1")


State.broadcast()