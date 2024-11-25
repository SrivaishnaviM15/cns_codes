#keyexchange algo diffiehellman
import math
n,g,x,y = map(int,input("Enter the values of n,g,x,y : ").split())
A = (math.pow(g,x)) % n
B = (math.pow(g,y)) % n
k1 = (math.pow(B,x)) % n
k2 = (math.pow(A,y)) % n
if k1 == k2:
    print("Keys are correct")
else:
    print("some error has occuered")
