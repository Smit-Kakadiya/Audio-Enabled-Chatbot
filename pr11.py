import pymysql 
import speech_recognition as sr

conn=pymysql.connect(host='localhost',user='root',password='',db='mini_pro')
a=conn.cursor()
r=sr.Recognizer()
spc=""
flag=0
with sr.Microphone() as source:
	print('say something')
	audio=r.listen(source)
    #print('hello')
try:
	spc=r.recognize_google(audio)
	print('you said : \n' + spc)
except:
	print('operate in noise less environment')
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
	flag=1
if flag==1:
   print('do u want this question to be entered in database y or n') 
   an=input()
   if an=='y':
       sql="INSERT INTO mini3(que) VALUES(%s)"
       a.execute(sql,spc)
conn.commit()
       
       
   
	
        

