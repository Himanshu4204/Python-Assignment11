# Q5. Write a python script to calculate the sum of first N Even natural Number ?
x=int(input("Enter a Number :"))
s=0
for a in range(1,x*2+1):
    if a%2==0:
        s=s+a
print(s)