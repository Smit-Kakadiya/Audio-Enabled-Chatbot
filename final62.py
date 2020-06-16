import pymysql 
import speech_recognition as sr

conn=pymysql.connect(host='localhost',user='root',password='',db='mini_pro')
a=conn.cursor()
r=sr.Recognizer()
spc=""
with sr.Microphone() as source:
	print('say something')
	audio=r.listen(source)
try:
	spc=r.recognize_google(audio)
	print('you said : \n' + spc)
except:
	print('operate in noise less environment')
	break
#sql='SELECT Ans from 'mini_tab' where Que='"+spc+"'"
#sql="SELECT Ans from mini_tab"
sql= "select Answer from mini_tab where Question =%s"
a.execute(sql,spc)
data=a.fetchone()
try:
	value=data[0]
	print(value)
except:
	print('Answer is not present in databse')
	break
        

