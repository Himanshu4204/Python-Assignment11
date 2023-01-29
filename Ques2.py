# Q2. write apython script to calculate sum of squares of first N natural Number ?
x=int(input("Enter a Number :"))
s=0
for a in range(1,x+1):
    a=a**2
    s=s+a
print(s)
