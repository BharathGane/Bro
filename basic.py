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

    print ("Give me a second bro,... fetching the results!")
    response = request.getresponse()

    string = response.read().decode('utf-8')
    response_json = json.loads(string)

    print response_json['result']['metadata']['html']
    print response_json['result']['metadata']['speech']
    
    if(response_json['result']['source'] == 'domains' and response_json['result']['action'] == 'web.search'):
        if(response_json['result']['parameters']['service_name'] == "Google"):
            driver = webdriver.Firefox()
            google_search = "https://encrypted.google.com/search?q=" + response_json['result']['parameters']['q']
            driver.get(google_search)
        if(response_json['result']['parameters']['service_name'] == "DuckDuckGo"):
            driver = webdriver.Firefox()
            duck_search = "https://duckduckgo.com/?q=" + response_json['result']['parameters']['q']
            driver.get(duck_search)

if __name__ == '__main__':
    main()