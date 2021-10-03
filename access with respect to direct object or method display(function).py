class Bank:
             bname="SBI"
             BML="MYSORE"
             BROI=16
             def __init__(self,cname,cmb,cadd,cbbal):
                          self.cname=cname
                          self.cmb=cmb
                          self.cadd=cadd
                          self.cbbal=cbbal
             def display(self):
                          print(self.bname,self.BML,self.BROI,self.cname,self.cmb,self.cadd,self.cbbal)
                          
b1=Bank('ajay',8888324151,'hm',500)
b2=Bank('vijay',4352616712,'datia',1200)
print(b1.cname,b1.cmb,b1.cadd,b1.cname)  #direct call
print(b2.cname,b2.cmb,b2.cadd,b2.cname)  #direct call
b1.display()    #call with respect to object 
b2.display()    #call with respect to object
Bank.display(b1)      #call with respect to class
Bank.display(b2)     #call with respect to class

