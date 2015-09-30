#!/usr/bin/python

import urllib
import re

class user(object):

    def __init__(self,username):
        self.username = username
        #makes youtube address for the username
        self.address = "http://www.youtube.com/user/" + self.username + "/about"

    def dataRetrieve(self):
        #pulls data out of the page
        data = urllib.urlopen(self.address).read()
        #this is how number of subscribers coded in the page
        regex = '<span class="about-stat"><b>(.+?)</b> subscribers</span>'
        #converts regex to a form that re needs
        pattern = re.compile(regex)
        self.matches = re.findall(pattern, data)
        return self.matches

    def serve(self):
        print self.username,"has",self.matches[0],"subscribers on his/her youtube channel!"

print "---------------YT-Subscribers------------------"
name = user(raw_input("Give me username of the youtuber:)\n"))
name.dataRetrieve()
name.serve()