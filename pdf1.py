import os
import pymysql 
import speech_recognition as sr
conn=pymysql.connect(host='localhost',user='root',password='',db='mini_pro')
a=conn.cursor()
r=sr.Recognizer()
with sr.Microphone() as source:
		print('say something')
		audio=r.listen(source)
try:
	text=r.recognize_google(audio)
	print('you said : \n' + text)
except:
	print('operate in noise less environment')
#print ((text.split())[0])
text.lower()
value=len(text.split())
print(value)
flag=list()
for i in range(value):
    if (text.split())[i]=='it':
        flag.append('it')
    elif (text.split())[i]=='mech':
        flag.append('mech')
    elif (text.split())[i]=='mechanical':
       flag.append('mech')
    elif (text.split())[i]=='computer':
        flag.append('cp')
    elif (text.split())[i]=='cp':
        flag.append('cp')
    elif (text.split())[i]=='electronics':
        flag.append('el')
    elif (text.split())[i]=='electrical':
        flag.append('ee')
    elif (text.split())[i]=='production':
       flag.append('pe')
    elif (text.split())[i]=='communication':
        flag.append('ec')
    elif (text.split())[i]=='ec':
        flag.append('ec')
    elif (text.split())[i]=='ee':
        flag.append('ee')
    elif (text.split())[i]=='el':
        flag.append('el')
    elif (text.split())[i]=='technology':
        flag.append('it')
    elif (text.split())[i]=='civil':
       flag.append('ce')
    elif (text.split())[i]=='ce':
        flag.append('ce')
for i in range(value):
    if (text.split())[i]=='table':
        flag.append('timetable')
str1 = ' '.join(flag)
print(str1)
a.execute("""SELECT path FROM files WHERE name=%s""",str1)
data=a.fetchone()
#print('data ' + data)
try:
	value=data[0]
	os.startfile(value)
   #print('file opened')
except:
	print('no such file present in database')
