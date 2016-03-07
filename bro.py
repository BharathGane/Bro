import os, sys
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

try:
    import apiai
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    import apiai

import pyaudio
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5

CLIENT_ACCESS_TOKEN = 'a36e008c5d284b279d6226e69c89d92d'
SUBSCRIPTION_KEY = '46493cf0-9ccb-4813-8451-9b300b3624e7' 

def web_search(response_json):
	print response_json['result']['metadata']['html']
	print response_json['result']['metadata']['speech']
	if(response_json['result']['source'] == 'domains' and response_json['result']['action'] == 'web.search'):
		if(response_json['result']['parameters']['service_name'] == "Google"):
			driver = webdriver.Firefox()
			google_search = "https://encrypted.google.com/search?q=" + response_json['result']['parameters']['q']
			driver.get(google_search)
		elif(response_json['result']['parameters']['service_name'] == "DuckDuckGo"):
			driver = webdriver.Firefox()
			duck_search = "https://duckduckgo.com/?q=" + response_json['result']['parameters']['q']
			driver.get(duck_search)

def webpage_open(response_json):
	Websites = {'Google', 'Facebook', 'YouTube', 'Gmail', 'Outlook', 'GitHub', 'DuckDuckGo', 'Quora', 'Kickass', 'Pirate Bay', 'Yify', 'Shush'}
	print "Opening " + response_json['result']['parameters']['Websites'] + " ..."
	print response_json['result']['fulfillment']['speech']
	if(response_json['result']['parameters']['Websites'] in Websites):
		if(response_json['result']['parameters']['Websites'] == "Google"):
			driver = webdriver.Firefox()
			google = "https://encrypted.google.com/"
			driver.get(google)
		if(response_json['result']['parameters']['Websites'] == "Facebook"):
			driver = webdriver.Firefox()
			fb = "https://www.facebook.com/"
			driver.get(fb)
		if(response_json['result']['parameters']['Websites'] == "YouTube"):
			driver = webdriver.Firefox()
			youtube = "https://www.youtube.com/"
			driver.get(youtube)
		if(response_json['result']['parameters']['Websites'] == "Gmail"):
			driver = webdriver.Firefox()
			gmail = "https://mail.google.com/"
			driver.get(gmail)
		if(response_json['result']['parameters']['Websites'] == "Outlook"):
			driver = webdriver.Firefox()
			outlook = "https://login.microsoftonline.com/"
			driver.get(outlook)
		if(response_json['result']['parameters']['Websites'] == "GitHub"):
			driver = webdriver.Firefox()
			github = "https://www.github.com/"
			driver.get(github)
		if(response_json['result']['parameters']['Websites'] == "DuckDuckGo"):
			driver = webdriver.Firefox()
			duckduckgo = "https://duckduckgo.com/"
			driver.get(duckduckgo)
		if(response_json['result']['parameters']['Websites'] == "Quora"):
			driver = webdriver.Firefox()
			quora = "https://www.quora.com/"
			driver.get(quora)
		if(response_json['result']['parameters']['Websites'] == "Kickass"):
			driver = webdriver.Firefox()
			kat = "https:/kat.cr/"
			driver.get(kat)
		if(response_json['result']['parameters']['Websites'] == "Pirate Bay"):
			driver = webdriver.Firefox()
			tpbt = "https://thepiratebay.vg/"
			driver.get(tpbt)
		if(response_json['result']['parameters']['Websites'] == "Yify"):
			driver = webdriver.Firefox()
			yts = "https://yts.ag/"
			driver.get(yts)
		if(response_json['result']['parameters']['Websites'] == "Shush"):
			driver = webdriver.Firefox()
			shush = "https://shush.se/"
			driver.get(shush)

def application_open(response_json):
	Applications = {'Google Chrome', 'Firefox', 'Terminal', 'Sublime Text', 'Tixati', 'Files', 'Virtual Box', 'Software Center', 'Wine', 'VLC', 'Office', 'Vim'}
	print "Opening " + response_json['result']['parameters']['Applications'] + " ..."
	print response_json['result']['fulfillment']['speech']
	if(response_json['result']['parameters']['Applications'] in Applications):
		if(response_json['result']['parameters']['Applications'] == "Google Chrome"):
			os.system('google-chrome')
		if(response_json['result']['parameters']['Applications'] == "Firefox"):
			os.system('firefox')
		if(response_json['result']['parameters']['Applications'] == "Terminal"):
			os.system('gnome-terminal')
		if(response_json['result']['parameters']['Applications'] == "Sublime Text"):
			os.system('subl')
		if(response_json['result']['parameters']['Applications'] == "Tixati"):
			os.system('tixati')
		if(response_json['result']['parameters']['Applications'] == "Files"):
			os.system('nemo')
		if(response_json['result']['parameters']['Applications'] == "Virtual Box"):
			os.system('virtualbox')
		if(response_json['result']['parameters']['Applications'] == "Software Center"):
			os.system('mintinstall')
		if(response_json['result']['parameters']['Applications'] == "Wine"):
			os.system('wine')
		if(response_json['result']['parameters']['Applications'] == "VLC"):
			os.system('vlc')
		if(response_json['result']['parameters']['Applications'] == "Office"):
			os.system('libreoffice')
		if(response_json['result']['parameters']['Applications'] == "Vim"):
			os.system('vim')

# sudo apt-get install xbacklight -- screen brightness control thru terminal
# xbacklight -inc 50
# xbacklight -dec 20
def increase_screenbright(response_json):
	print "Increasing the screen brightness by " + response_json['result']['parameters']['number'] + " percent"
	increase_string = 'xbacklight -inc ' + response_json['result']['parameters']['number']
	os.system(increase_string)
	print response_json['result']['fulfillment']['speech']

def decrease_screenbright(response_json):
	print "Decreasing the screen brightness by " + response_json['result']['parameters']['number'] + " percent"
	decrease_string = 'xbacklight -dec ' + response_json['result']['parameters']['number']
	os.system(decrease_string)
	print response_json['result']['fulfillment']['speech']

def screenshot(response_json):
	print "Bro,... Ask your monitor to say cheese !!!!"
	os.system('gnome-screenshot')
	print response_json['result']['fulfillment']['speech']

def main():
    resampler = apiai.Resampler(source_samplerate=RATE)
    vad = apiai.VAD()
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN, SUBSCRIPTION_KEY)
    request = ai.voice_request()
    request.lang = 'en'

    def callback(in_data, frame_count, time_info, status):
        frames, data = resampler.resample(in_data, frame_count)
        state = vad.processFrame(frames)
        request.send(data)

        if (state == 1):
            return in_data, pyaudio.paContinue
        else:
            return in_data, pyaudio.paComplete

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS, 
                    rate=RATE, 
                    input=True,
                    output=False,
                    frames_per_buffer=CHUNK,
                    stream_callback=callback)

    stream.start_stream()

    print ("Hello bro, what would you like to do ?!")

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
    	web_search(response_json)
    elif(response_json['result']['source'] == 'agent' and response_json['result']['metadata']['intentId'] == 'c9ce76e4-c303-48ba-b2c6-c3f667a097ba'):
    	webpage_open(response_json)
    elif(response_json['result']['source'] == 'agent' and response_json['result']['metadata']['intentId'] == 'a8e2ef36-c808-45e0-aa97-e7ac37008557'):
    	application_open(response_json)
    elif(response_json['result']['source'] == 'agent' and response_json['result']['metadata']['intentId'] == '75eefcad-dfd0-4a23-9325-34d7204e0850'):
    	increase_screenbright(response_json)
    elif(response_json['result']['source'] == 'agent' and response_json['result']['metadata']['intentId'] == '97fdce22-d080-4a3d-8316-53314707aa31'):
    	decrease_screenbright(response_json)
    elif(response_json['result']['source'] == 'agent' and response_json['result']['metadata']['intentId'] == '1093f02f-db86-40ba-ab25-ee81d222604e'):
    	screenshot(response_json)
if __name__ == '__main__':
    main()