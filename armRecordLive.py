from helpers import *

clearAllArmed()
for key, value in armTracks.items():
	armRecord(getTrackOffset(value))