class Bank:
             bname='HDFC'
             MBL='Banglore'
             LROI=12
             def __init__(self,name,phno,email,add,bbal=500):
                          self.name=name
                          self.phno=phno
                          self.email=email
                          self.add=add
                          self.bbal=bbal
             def display(self):
                          print(self.name,self.phno,self.email,self.add,self.bbal)
             def ch_name(self,new):
                          self.name=new
             def ch_email(self,email):
                          self.email=email
             def deposite(self,new):
                          self.bbal+=new
             def withdraw(self,new):
                          if self.bbal>=new:
                                       self.bbal-=new
                                       print("Successfull Transaction")
                          else:
                                       print("Balance Insufficient")
             @classmethod
             def displayc(cls):
                          print(cls.bname,cls.MBL,cls.LROI)
             @classmethod
             def ch_MBL(cls,mbl):
                          cls.MBL=mbl
             @classmethod
             def ch_bname(cls,new):
                          cls.bname=new
b1=Bank('ajay',8889941291,'ragh@gmail.com','hanuman',1000)
m=True
while m:
             c=int(input("Press 1 for display object value 2 for display class\
value 3 for deposite money 4 for withdrow money 5 for change \
location main branch 6 for exist        "))
             if c==1:
                          b1.display()
             if c==2:
                          Bank.displayc()
             if c==3:
                          b1.deposite(int(input()))
             if c==4:
                          b1.withdraw(int(input()))
             if c==5:
                          Bank.cn_MBL(input())
             if c==6:
                          m=False
             print("*"*56)
