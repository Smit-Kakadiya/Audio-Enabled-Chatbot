from subprocess import Popen
p = Popen("abc.bat",cwd=r"C:\Users\Admin\__chatbot")
stdout, stderr = p.communicate()