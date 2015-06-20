from helpers import *

beginUndo()
tr = getTrackWy()
changeVolume(tr,-2.5) #dB
endUndo("Undo volumeDownWy")