import requests

playState = RPR_GetPlayState();
if playState and playState != 2: #playing/recording
	RPR_OnStopButton();
	requests.post("http://localhost:5000/actions/updatestate", data={'record':0, 'playstop':0}) 
else:
	RPR_OnPlayButton()
	requests.post("http://localhost:5000/actions/updatestate", data={'record':0, 'playstop':1}) 