#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE

def urltoimg(url):
    stdout = Popen("bin/phantomjs screencapture.js "+url, stdout=PIPE, shell=True).stdout.read()
    print 'filename stored(stdout phantomjs): '+stdout
    return 'capture-'+stdout.encode('utf-8').strip()+'.png'

def main(url):
	urltoimg(url)

if __name__ == '__main__':
	main('http://google.in')