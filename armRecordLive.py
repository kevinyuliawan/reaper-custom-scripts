from helpers import *

beginUndo()
clearAllArmed()
for key, value in armTracks.items():
	armRecord(getTrackOffset(value))
endUndo("Undo recording all live tracks")