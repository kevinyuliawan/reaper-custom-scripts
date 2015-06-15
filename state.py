import requests

class State:
	record = "0"
	playstop = "0"
	song = ""
	@classmethod
	def broadcast(self):
		requests.post("http://localhost:5000/actions/updatestate", data={'record':State.record, 'playstop':State.playstop, 'song':State.song}) 