from state import State
from helpers import *

State.song = getCurrentName()

if playState() and ( playState() == "playing" or playState() ) == "recording":
	RPR_OnStopButton();
	State.record = "0"
	State.playstop = "0"
else:
	RPR_OnPlayButton()
	State.record = "0"
	State.playstop = "1"

State.broadcast()