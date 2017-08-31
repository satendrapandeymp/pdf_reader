from PyPDF2 import PdfFileReader
from gtts import gTTS
import os, pyttsx, time
from multiprocessing import Process

def func1():
    tts = gTTS(text=data , lang='en')
    name = str(num+1) + ".mp3"
    tts.save(name)

def func3(name):
    name = "mpg321 %s"%(name)
    os.system(name)

def func2():
    engine = pyttsx.init()
    engine.setProperty('rate', 120)
    engine.setProperty('voice', 'punjabi')
    engine.say(data)
    engine.runAndWait()

name = raw_input("Type the file name Excluding .pdf if that is in same folder else give abs path without .pdf --  ")
name = name + ".pdf"
infile = PdfFileReader(name, 'rb')

page = raw_input("Enter Page Number you wanna read --  ")
page = int(page)
num = page
reader_temp = infile.getPage(page)
data = reader_temp.extractText()

# gtts sounds pretty better than pyttsx that's why I'm reading it through gtts
# gtts takes nearly 30 sec to save that into a file and start reading but pyttsx do it within few seconds
# So if you don't want to wait then you can put func2() here and delete lines which is below

func1()

for num in range(page+1,infile.numPages):
    reader_temp = infile.getPage(page)
    data = reader_temp.extractText()
    name = str(num) + ".mp3"
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func3(name))
    p2.start()
    p1.join()
    p2.join()
