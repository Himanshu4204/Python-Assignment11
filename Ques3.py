# Q3. write a python script to calculate sum of cubes of first N natural number?
x=int(input("Enter a Number :"))
s=0
for a in range(1,x+1):
    a=a**3
    s=s+a
print(s)