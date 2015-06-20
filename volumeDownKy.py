from helpers import *

beginUndo()
tr = getTrackKy()
changeVolume(tr,-2.5) #dB
endUndo("Undo volumeDownKy")