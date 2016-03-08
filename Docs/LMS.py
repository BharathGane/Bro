import re
import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

s = requests.session()

payload={'username':'IMTXXXXXXX', 'password':'XXXXXXXX'}

def login():
    url = s.post('https://lms.iiitb.ac.in/moodle/login/index.php', data=payload, verify=False)
    soup = BeautifulSoup(url.text)
    t = soup.findAll(text=re.compile("imt"));
    if(len(t)>=3):
        print "Logged in successfully!"
        print "Welcome, ", t[0] + "\n"
        return 1;
    else:
        print "Not logged in"
        return 0;

def check_new_assignments():
    url = s.post('https://lms.iiitb.ac.in/moodle/my/', data=payload, verify=False)
    soup = BeautifulSoup(url.text)
    t = soup.findAll(text=re.compile("You have assignments that need attention"))

    for i in t:
        link = i.parent.parent.parent.parent.parent.parent.findChild().findChild().findChildren()[0]['href']
        subject = i.parent.parent.parent.parent.parent.parent.findChild().findChild().findChildren()[0]['title']

        if(len(t)>=1):
            print i + "in "+ subject
            print "Link: " + link + "\n"

def check_new_forum_posts():
    url = s.post('https://lms.iiitb.ac.in/moodle/my/', data=payload, verify=False)
    soup = BeautifulSoup(url.text)
    t = soup.findAll(text=re.compile("There are new forum posts"))

    for i in t:
        link = i.parent.parent.parent.parent.parent.parent.findChild().findChild().findChildren()[0]['href']
        subject = t[0].parent.parent.parent.parent.parent.parent.findChild().findChild().findChildren()[0]['title']
        if(len(t)>=1):
            print i + "in " + subject
            print "Link: " + link + "\n"

if __name__ == '__main__':
	login()
	check_new_assignments()
	check_new_forum_posts()
