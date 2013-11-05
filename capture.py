#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE

def urltoimg(url):
    std = Popen("export PATH=$PATH:/app/bin/", stdout=PIPE, shell=True).stdout.read()
    stdout = Popen("bin/phantomjs screencapture.js "+url, stdout=PIPE, shell=True).stdout.read()

def main(url):
	urltoimg(url)

if __name__ == '__main__':
	main('http://google.in')