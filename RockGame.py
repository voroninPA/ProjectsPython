import random
numb=random.randint(4,30)
print("Hi, its rocks game")
while numb>1:
    print("number of rocks: ", numb)
    i=int(input("what number of rocks you want to take:"))
    numb=numb-i
    print("number of rocks: ", numb)
    comp=random.randint(1,3)
    print("computer take ",comp,"rocks")
    numb=numb-comp
if(numb==1):
    print("you lose")
else:
    print("you win")
print("HI")
