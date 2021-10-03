class bank:
             bname='SBI'
             mbl='Mysore'
             LROI=16
c1=bank()
c2=bank()
def imo(obj,cname,cph,cadd,cbbal):
             obj.cname=cname
             obj.cph=cph
             obj.cadd=cadd
             obj.cbbal=cbbal
imo(c1,'ajay',8000000000,'datia',500)
imo(c2,'vijay',9544332243,'mp',4000)
print(c1.cname)
print(c2.mbl)
