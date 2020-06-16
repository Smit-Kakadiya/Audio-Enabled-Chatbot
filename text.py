import pymysql 
import sys
import speech_recognition as sr
r = sr.Recognizer()
conn=pymysql.connect(host='localhost',user='root',password='',db='mini_pro')
a=conn.cursor()
sql="""select Question from mini_table where Answer is null"""
a.execute(sql)
data=a.fetchall()
aa=""
i=0
print(len(data))
for row in data:
   print('null ques :')
   print(row[0])
   with sr.Microphone() as source:
       print('give ans')
       audio=r.listen(source)
   try:
       aa=r.recognize_google(audio)
       print(aa)
   except:
       print('operate in noise less environment')
       sys.exit()
   sql="""update mini_table set Answer=%s where Question=%s"""
   a.execute(sql,(aa,row[0]))
   conn.commit()