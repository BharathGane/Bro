import os, sys
class sys_service(object):
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
			if(response_json['result']['parameters']['Applications'] == "Calculator"):
				os.system('gnome-calculator')

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
		
	def mute(response_json):
		os.system('amixer -D pulse sset Master mute')
		print response_json['result']['fulfillment']['speech']

	def unmute(response_json):
		os.system('amixer -D pulse sset Master unmute')
		print response_json['result']['fulfillment']['speech']

	def set_volume(response_json):
		set_string = 'amixer -D pulse sset Master ' + response_json['result']['parameters']['percentage']
		os.system(set_string)
		print response_json['result']['fulfillment']['speech']

	def increase_volume(response_json):
		increase_string = 'amixer -D pulse sset Master ' + response_json['result']['parameters']['percentage'] + '+'
		os.system(increase_string)
		print response_json['result']['fulfillment']['speech']

	def decrease_volume(response_json):
		decrease_string = 'amixer -D pulse sset Master ' + response_json['result']['parameters']['percentage'] + '-'
		os.system(decrease_string)
		print response_json['result']['fulfillment']['speech']
