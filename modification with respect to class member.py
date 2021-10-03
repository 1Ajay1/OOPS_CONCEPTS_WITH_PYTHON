class modwrtcm:
             a=10
             b=20
             c=30
ob=modwrtcm()
print(ob.a,ob.b,ob.c)
modwrtcm.b=123#modification with respect to member class only that object modify class member
print(ob.a,ob.b,ob.c)
print(ob.a,ob.b,ob.c)
print(modwrtcm.a,modwrtcm.b,modwrtcm.c)
