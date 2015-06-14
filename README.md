# reaper-custom-scripts
A folder of custom scripts for the music software Reaper

##customRecord.py
A record function that will record from the beginning of the current region to the end, and at the end of recording, go onto the next region. The idea is so that when performing live, I only need to press the record button once for each song. It can also respond to 'spacebar' presses in order to interrupt recording, e.g. during practice (something that the SWS action I borrowed from couldn't do).

###TODO:
Add broadcast functions (post requests to localhost) in order to keep the client UIs in-sync.
