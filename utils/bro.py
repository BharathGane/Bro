import os, sys
import json
import time
import pyaudio

from config import Config
from sys_ai import sys_service
from web_services import web

#Check if API.AI module is available
try:
	import apiai
except ImportError:
	sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
	import apiai

def main():
	resampler = apiai.Resampler(source_samplerate=Config.RATE)
	vad = apiai.VAD()
	ai = apiai.ApiAI(Config.CLIENT_ACCESS_TOKEN, Config.SUBSCRIPTION_KEY)
	request = ai.voice_request()
	request.lang = 'en'

	def stream_callback(in_data, frame_count, time_info, status):
		frames, data = resampler.resample(in_data, frame_count)
		state = vad.processFrame(frames)
		request.send(data)

		if (state == 1):
			return in_data, pyaudio.paContinue
		else:
			return in_data, pyaudio.paComplete

	p = pyaudio.PyAudio()

	stream = p.open(format=Config.FORMAT,
					channels=Config.CHANNELS, 
					rate=Config.RATE, 
					input=True,
					output=False,
					frames_per_buffer=Config.CHUNK,
					stream_callback=stream_callback)


	print ("Hello bro, what would you like to do ?!")
	stream.start_stream()

	try:
		while stream.is_active():
			time.sleep(0.1)
	except Exception:
		raise e
	except KeyboardInterrupt:
		pass

	stream.stop_stream()
	stream.close()
	p.terminate()

	print ("Give me a second bro,... Will be back with what you want right away!")
	response = request.getresponse()

	response_string = response.read().decode('utf-8')
	response_json = json.loads(response_string)

	if(response_json['result']['source'] == 'domains' and response_json['result']['action'] == 'web.search'):
		web.web_search(response_json)
	elif(response_json['result']['source'] == 'agent' and response_json['result']['action'] == 'browse.open'):
		web.webpage_open(response_json)
	elif(response_json['result']['source'] == 'agent' and response_json['result']['action'] == 'app.open'):
		sys_service.application_open(response_json)
	elif(response_json['result']['source'] == 'agent' and response_json['result']['action'] == 'increase.brightness'):
		sys_service.increase_screenbright(response_json)
	elif(response_json['result']['source'] == 'agent' and response_json['result']['action'] == 'decrease.brightness'):
		sys_service.decrease_screenbright(response_json)
	elif(response_json['result']['source'] == 'agent' and response_json['result']['action'] == 'capture.screen'):
		sys_service.screenshot(response_json)
	elif(response_json['result']['source'] == 'agent' and response_json['result']['action'] == 'lms.notif'):
		web.LMSCheck(response_json)
	elif(response_json['result']['source'] == 'agent' and response_json['result']['action'] == 'set.volume'):
		sys_service.set_volume(response_json)
	elif(response_json['result']['source'] == 'agent' and response_json['result']['action'] == 'mute.volume'):
		sys_service.mute(response_json)
	elif(response_json['result']['source'] == 'agent' and response_json['result']['action'] == 'unmute.volume'):
		sys_service.unmute(response_json)
	elif(response_json['result']['source'] == 'agent' and response_json['result']['action'] == 'increase.volume'):
		sys_service.increase_volume(response_json)
	elif(response_json['result']['source'] == 'agent' and response_json['result']['action'] == 'decrease.volume'):
		sys_service.decrease_volume(response_json)

if __name__ == '__main__':
	main()