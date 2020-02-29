import time
import random
import pandas as pd
import csv

file = open("input.txt","r")

line=file.readlines()

timelist=[]

for i in line:
    
    N = int(i)
    
    n1, n2 = 0, 1
    count = 0

    if(N<=0):
        print("Enter a non-negative integer")
    elif(N== 1):
        print("Fibonacci sequence upto",N,":")
        print(n1)
    else:
        #print("Fibonacci sequence:")
        start = time.time() * 1000
        while count < N:
           #print(n1)
           nth = n1 + n2
           # update values
           n1 = n2
           n2 = nth
           count += 1
        end = time.time() * 1000
        t = end-start
        print("Request ID: ",random.randint(1,100),"Time: ",t,"N: ",N)
        timelist.append(t)

df = pd.DataFrame({'Request Time':timelist})
df.to_csv('Request Time.csv',index=False)
