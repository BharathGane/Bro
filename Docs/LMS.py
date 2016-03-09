#!/usr/local/bin/env python

# This script is my first try at web scraping, aimed at students of IIIT-B, to quickly check notifications, new assignments and forum posts in LMS portal.
# Script under development, further features will be added as and when I find free time :p ;)

import re
import requests
import selenium
from lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

s = requests.session()

payload={'username':'IMTXXXXXXX', 'password':'XXXXXX'}

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

def individual_details(link):
    url = s.get(link)
    soup = BeautifulSoup(url.text)
    details = soup.find_all("div", class_="activityinstance")
    tree = html.fromstring(url.content)
    data = tree.xpath('//span[@class="instancename"]/text()')
    j=0
    for i in details:
        link = i.findChildren()[0]['href']
        if(len(details)>=1):
            print "\t" + '"\033[1m' + data[j] + '\033[0m"'
            print "\t    " + "Link :" + link
            j+=1
    print "\n"

def check_new_assignments():
    url = s.get('https://lms.iiitb.ac.in/moodle/my/')
    soup = BeautifulSoup(url.text)
    check_assignments = soup.findAll(text=re.compile("You have assignments that need attention"))

    for i in check_assignments:
        link = i.parent.parent.parent.parent.parent.parent.findChild().findChild().findChildren()[0]['href']
        subject = i.parent.parent.parent.parent.parent.parent.findChild().findChild().findChildren()[0]['title']


        if(len(check_assignments)>=1):
            print i + "in " + '"\033[44m' + subject + '\033[0m"'
            print "Link: " + link
            individual_details(link)

def check_new_forum_posts():
    url = s.get('https://lms.iiitb.ac.in/moodle/my/')
    soup = BeautifulSoup(url.text)
    check_posts = soup.findAll(text=re.compile("There are new forum posts"))

    for i in check_posts:
        link = i.parent.parent.parent.parent.parent.parent.findChild().findChild().findChildren()[0]['href']
        subject = check_posts[0].parent.parent.parent.parent.parent.parent.findChild().findChild().findChildren()[0]['title']
        if(len(check_posts)>=1):
            print i + "in " + '"\033[44m' + subject + '"\033[0m'
            print "Link: " + link + "\n"

if __name__ == '__main__':
	login()
	check_new_assignments()
	check_new_forum_posts()
