#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE

def urltoimg(url):
    stdout = Popen("phantomjs screencapture.js "+url, stdout=PIPE, shell=True).stdout.read()

def main(url):
	urltoimg(url)

if __name__ == '__main__':
	main('http://yahoo.in')