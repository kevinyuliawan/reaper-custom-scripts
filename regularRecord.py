import requests

RPR_Main_OnCommand(1013, 0) #regular record
playState = RPR_GetPlayState();
if playState and playState == 5: #5 means recording
	requests.post("http://localhost:5000/actions/updatestate",  data={'record': 1, 'playstop':1})
else:
	requests.post("http://localhost:5000/actions/updatestate",  data={'record': 0, 'playstop':1})