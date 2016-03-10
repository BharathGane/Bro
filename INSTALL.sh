echo 'This script will install the required dependencies required to run Bro'
echo -n 'Please enter your password to proceed: '

# GET USER PASSWORD
read password
echo $password

echo ' Installing JSON'
sudo pip install simplejson

echo '\n \n Installing APIAI'
sudo pip install apiai

echo '\n \n Installing Selenium WebDriver'
sudo pip install selenium

echo '\n \n Installing ALSA Audio Utility'
sudo apt-get install alsa-utils

echo '\n \n Installing XBACKLIGHT'
sudo apt-get install xbacklight

echo '\n \n Installing PyAudio and Numpy'
sudo apt-get install python-pyaudio python-numpy
