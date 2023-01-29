# Q10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
decimal=int(input("Enter number :"))
octal=0
ctr=0
temp=decimal
while(temp>0):
    octal=((temp%8)*(10**ctr))+octal
    temp=int(temp/8)
    ctr+=1
print("Octal of {x} is: {y}".format(x=decimal,y=octal))