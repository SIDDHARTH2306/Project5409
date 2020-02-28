import datetime
import random
import time

def factorial(n):
    if(n == 0):
        return 1
    else:
        return n * factorial(n-1)

timelist=[]

f = open("input.txt", "r")
list1=f.readlines()

for i in list1:
    N=i
    start_time = time.time()
    result = factorial(int(i))
    end_time = time.time()
    requestID = random.randint(1,10)
    time_taken = (end_time-start_time)
    timelist.append(time_taken)
    print("Request ID : ", requestID ,"Time : ",time_taken,"Result : ",result,"N :",N)
