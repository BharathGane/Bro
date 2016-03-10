#!/usr/local/bin/env python

# This script is my first try at web scraping, aimed at students of IIIT-B, to quickly check notifications, new assignments and forum posts in LMS portal.
# Script is under development, further features will be added as and when I find free time :p ;)

import re
import urllib2
import requests
import selenium
from lxml import html
from bs4 import BeautifulSoup

s = requests.session()

payload={'username':'IMT2015521', 'password':'ashokthiru24597'}

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

def download(link,file_name, download_directory):
    print "\n \t Downloading " + file_name
    data = s.get(link, stream=True)
    with open(download_directory+'/'+file_name, 'wb') as file:
        for chunk in data.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
                file.flush()

def get_files(link, download_directory):
    url = s.get(link)
    soup = BeautifulSoup(url.text)
    files = soup.find_all("span", class_="fp-filename-icon")

    for i in files:
        download_link = i.findChildren()[0]['href']
        download_file_name = i.findChildren()[0].findChildren()[2].text

        download(download_link, download_file_name, download_directory)

def check_sildes_notes(link, download_directory):
    url = s.get(link)
    soup = BeautifulSoup(url.text)

    print '\033[1m' + "\nDownloading files from Slides Folder" + '\033[0m'
    SlidesFolder = soup.findAll(text=re.compile("Slides Folder"))
    SlidesDirectory = SlidesFolder[0].parent.parent.parent.findChildren()[0]['href']
    get_files(SlidesDirectory, download_directory)

    print '\033[1m' + "\nDownloading files from Notes Folder" + '\033[0m'
    NotesFolder = soup.findAll(text=re.compile("Notes Folder"));
    NotesDirectory = NotesFolder[0].parent.parent.parent.findChildren()[0]['href']
    get_files(NotesDirectory, download_directory)

def check_new_assignments():
    url = s.get('https://lms.iiitb.ac.in/moodle/my/')
    soup = BeautifulSoup(url.text)
    check_assignments = soup.findAll(text=re.compile("You have assignments that need attention"))

    for i in check_assignments:
        link = i.parent.parent.parent.parent.parent.parent.findChild().findChild().findChildren()[0]['href']
        subject = i.parent.parent.parent.parent.parent.parent.findChild().findChild().findChildren()[0]['title']

        if(len(check_assignments)>=1):
            print i + "in " +'"\033[31m' + '\033[1m' + subject + '\033[0m' + '\033[0m"'
            print "Link: " + link
            individual_details(link)

            directory = raw_input('\033[1m' + "Where would you like to download files from slides and notes folder of " + subject + " ?  ::  " + '\033[0m')
            check_sildes_notes(link,directory)

def check_new_forum_posts():
    url = s.get('https://lms.iiitb.ac.in/moodle/my/')
    soup = BeautifulSoup(url.text)
    check_posts = soup.findAll(text=re.compile("There are new forum posts"))

    for i in check_posts:
        link = i.parent.parent.parent.parent.parent.parent.findChild().findChild().findChildren()[0]['href']
        subject = check_posts[0].parent.parent.parent.parent.parent.parent.findChild().findChild().findChildren()[0]['title']
        if(len(check_posts)>=1):
            print i + "in " +'"\033[31m' + '\033[1m' + subject + '"\033[0m' + '\033[0m"'
            print "Link: " + link

if __name__ == '__main__':
	login()
	check_new_assignments()
	check_new_forum_posts()
