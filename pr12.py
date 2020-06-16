#!C:\Users\Admin\Anaconda3\python.exe
import cgitb
cgitb.enable()
import pymysql 
import speech_recognition as sr
import cgi
print("Content-Type: text/html\n")
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("<h4>Say Something!</h4>")
    audio = r.listen(source)
    print ("<h4>Done!<h4>")
text = r.recognize_google(audio)
print('<h1> you said ' + text + '</h1>')
print("""
<html>
<head>
<style>
</style>
</head>
<body>
<h1>hello</h1>
</body>
</html>""")

