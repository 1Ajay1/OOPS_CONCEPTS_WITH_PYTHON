class Bank:
             bname="SBI"
             BML="MYSORE"
             BROI=16
             def __init__(self,cname,cmb,cadd,cbbal):
                          self.cname=cname
                          self.cmb=cmb
                          self.cadd=cadd
                          self.cbbal=cbbal
             def ch_cname(self,new):
                          self.cname=new
             def ch_cadd(self,newa):
                          self.cadd=newa
             def display(self):
                          print(self.bname,self.BML,self.BROI,self.cname,self.cmb,self.cadd,self.cbbal)
                          
b1=Bank('ajay',8888324151,'hm',500)
b2=Bank('vijay',4352616712,'datia',1200)
b1.display()    #call with respect to object 
b2.display()    #call with respect to object
Bank.display(b1)      #call with respect to class
Bank.display(b2)     #call with respect to class
print(' *'*60)
b1.ch_cname('mohan') #change name with respect to object
b2.ch_cname("sohan")#change name with respect to object
b1.ch_cadd('hanuman Gadi datia') #change address with respect to object
b2.ch_cadd("Gwalior")#change address with respect to object
Bank.ch_cadd(b1,'Datia')
Bank.ch_cname(b2,'deepak')
b1.display()
b2.display() 

