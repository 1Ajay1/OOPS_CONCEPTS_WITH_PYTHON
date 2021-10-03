class Bank:
             bname="SBI"
             BML="MYSORE"
             BROI=16
             def __init__(self,cname,cmb,cadd,cbbal):
                          self.cname=cname
                          self.cmb=cmb
                          self.cadd=cadd
                          self.cbbal=cbbal
b1=Bank('ajay',8888324151,'hm',500)
b2=Bank('vijay',4352616712,'datia',1200)
print(b1.cname)
print(b1.cmb)
print(b1.cadd)
print(b1.cbbal)
print(b2.cname)
print(b2.cmb)
print(b2.cadd)
print(b2.cbbal)
