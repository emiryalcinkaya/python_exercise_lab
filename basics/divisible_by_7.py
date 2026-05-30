"""
Find all numbers between 2000 and 3200 that are divisible by 7
but not divisible by 5.
"""

l = []

for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
    
print(','.join(l))