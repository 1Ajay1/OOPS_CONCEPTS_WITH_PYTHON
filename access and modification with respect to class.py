class Cmethod:
             a=10
             b=20
             c=30
             def __init__(self,d,e,f):
                          self.d=d
                          self.e=e
                          self.f=f
             def display(self):
                          print(self.d,self.e,self.f)
             def ch_d(self,new):
                          self.d=new
             def ch_e(self,new):
                          self.e=new
             def ch_f(self,new):
                          self.f=new
             @classmethod
             def displayc(cls):
                          print(cls.a,cls.b,cls.c)
             @classmethod
             def ch_b(cls,new):
                          cls.b=new
             @classmethod
             def ch_c(cls,new):
                          cls.c=new
c1=Cmethod(12,34,45)
c1.display()
c1.displayc()
Cmethod.ch_b(13)
Cmethod.displayc()
