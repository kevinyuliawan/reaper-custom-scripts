import requests

class State:
	record = "0"
	playstop = "0"
	song = ""
	@classmethod
	def set(self, record=None, playstop=None, song=None):
		if record != None:
			State.record = record
		if playstop != None:
			State.playstop = playstop
		if song != None:
			State.song = song
	@classmethod
	def broadcast(self):
		requests.post("http://localhost:5000/actions/updatestate", data={'record':State.record, 'playstop':State.playstop, 'song':State.song}) 