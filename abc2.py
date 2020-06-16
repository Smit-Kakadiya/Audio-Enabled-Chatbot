#!C:\Users\Admin\Anaconda3\python.exe
import pymysql 
import speech_recognition as sr
import cgitb
cgitb.enable()
import cgi
print("Content-Type: text/html\n")
print("<!doctype html>\n")
#print("<body background='download.png'>")

conn=pymysql.connect(host='localhost',user='root',password='',db='mini_pro')
a=conn.cursor()
r=sr.Recognizer()
spc=""
with sr.Microphone() as source:
	print('say something \n')
	print("<br>")
	audio=r.listen(source)
try:
	spc=r.recognize_google(audio)
	print('you said : \n' + spc)
	print("<br>")
except:
	print('operate in noise less environment \n')
	print("<br>")
#sql='SELECT Ans from 'mini_tab' where Que='"+spc+"'"
#sql="SELECT Ans from mini_tab"
sql= "select Answer from mini_tab where Question =%s"
a.execute(sql,spc)
data=a.fetchone()
try:
	value=data[0]
	print(value)
except:
	print('Answer is not present in databse \n')
	print("<br>")
        

