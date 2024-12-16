name=input("what is your name?")
age=int(input("how old are you?"))
math=float(input("what is your mark"))
english=float(input("what is your mark"))
science=float(input("what is your mark"))
total=math+english+science
average=total/3
print("my name is",name)
print("i am",age)
print("my total mark is",total)
print("my average mark is",average)

if age>=20:
    print("you're an adult")
elif age>=13:
    print("you're a teenager")
elif age>0:
    print("you are a kid")
else:
    print("invalide age intered!")