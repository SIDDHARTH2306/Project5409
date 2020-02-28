import random

random_list=[]

with open('input.txt', 'w') as f:
    for i in range(100):
        f.write("%s\n" % random.randint(1,100))

