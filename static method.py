class Bank:
             bname='BOI'
             BMB='Mysore'
             FDROI=12
             def __init__(self,name,phno,email,add,bbal=500):
                          self.name=name
                          self.phno=phno
                          self.email=email
                          self.add=add
                          self.bbal=bbal
             def dis(self):
                          print(self.name,self.phno,self.email,self.add,self.bbal)
             def ch_name(self,new):
                          self.name=new
             def ch_add(self,new):
                          self.add=add
             def deposite(self,new):
                          self.bbal=self.add1(self.bbal,new)
                          self.mes()
             def withdraw(self,new):
                          if self.bbal>=new:
                                       self.bbal-=new
                                       self.mes()
                          else:
                                       print("Insufficient balance")
             @classmethod
             def disc(cls):
                          print(cls.bname,cls.BMB,cls.FDROI)
             @classmethod
             def ch_BMB(cls,new):
                          cls.BMB=new
             @classmethod
             def ch_bname(cls,new):
                          cls.bname=bname
             @staticmethod
             def add1(a,b):
                          return a+b
             @staticmethod
             def mes():
                          print("Transaction successfull")
b1=Bank('ajay',8889941291,'a@gmail.com','datia')
b1.dis()
b1.disc()
b1.deposite(400)
Bank.dis(b1)
b1.withdraw(100)
b1.dis()

             
