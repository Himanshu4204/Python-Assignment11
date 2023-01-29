# Q4. Write a python script to calculate sum of first N odd natural Number ?
x=int(input("Enter a Number :"))
s=0
for a in range(1,x*2):
    if a%2!=0:
        s=s+a
print(s)
