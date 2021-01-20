# -*- coding: utf-8 -*-

import webbrowser
import time
import platform
import os

urls = [
    'abv.bg',
    'google.com',
    'aws.amazon.com',
    'stackoverflow.com',
    'pymotw.com/3/'
        ]

chrome_exe = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser(chrome_exe))

while True:
    for i in urls:
        webbrowser.get('chrome').open(i)
        time.sleep(15)
    
    if platform.system() == 'Windows':
        os.system("taskkill /f /im chrome.exe")
    if platform.system() == 'Linux':
        os.system('kill -9  chrome')