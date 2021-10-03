class Student:
             cname='PYSPIDER'
             cml='BANGLORE'
             Cadd='banasabnagudi banglore'
             cdirector='akshay'
             def __init__(self,sname,sid,smb,sem,sbtime):
                          self.sname=sname
                          self.sid=sid
                          self.smb=smb
                          self.sem=sem
                          self.sbtime=sbtime
             def display(self):
                          print(self.sname,self.sid,self.smb,self.sem,self.sbtime)
             def ch_sname(self,new):
                          self.sname=new
             def ch_mb(self,new):
                          self.smb=new
             def ch_sem(self,new):
                          self.sem=new
             
b1=Student('ajay','QS12ajay',8889941291,'a@g.com','10-12 PM')
b2=Student('deepak','QS12deepak',9555445091,'d@g.com','10-12 PM')
b1.display()
Student.display(b2)
print('*'*80)
b1.ch_sname('Mohan')
b2.ch_sem('Y@gmail.com')
b1.display()
b2.display()

