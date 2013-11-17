#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from datetime import datetime
import sys

def urltoimg(url):
    stdout = Popen("bin/phantomjs screencapture.js "+url, stdout=PIPE, shell=True).stdout.read()
    print str(datetime.now())+' - filename stored(stdout phantomjs): '+stdout
    sys.stdout.flush()
    return 'capture-'+stdout.encode('utf-8').strip()+'.png'

def main(url):
	urltoimg(url)

if __name__ == '__main__':
	main('http://google.in')