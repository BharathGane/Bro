from selenium import webdriver
class web(object):
	def web_search(self,response_json):
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

	def webpage_open(self,response_json):
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

	def LMSCheck(self,response_json):
		os.system('cd Docs && python LMS.py')		