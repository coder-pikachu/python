# Enter your code here. Read input from STDIN. Print output to STDOUT

raw_input()
y=map(int,raw_input().split())
print y
a=set(y)
print a
raw_input()
b=set(map(int,raw_input().split()))
z= set(a - b | b - a )
for x in z:
    print x