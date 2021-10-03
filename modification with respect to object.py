class modiwrtom:
             a=10
             b=43
             c=34
ob=modiwrtom()
print(ob.a,ob.b,ob.c)
ob.b=12 #modification with respect to object only that object modify not change class member
print(ob.a,ob.b,ob.c)
print(modiwrtom.a,modiwrtom.b,modiwrtom.c)
