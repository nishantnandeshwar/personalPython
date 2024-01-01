tr1 = list(map(int, input("enter oxygen level of tr1:").split()))
tr2 = list(map(int, input("enter oxygen level of tr2:").split()))
tr3 = list(map(int, input("enter oxygen level of tr3:").split()))
#print(tr1)
#print(tr2)
#print(tr3)
sum=0
for i in tr1:
    if(i > 0 and i <= 100):
        sum = sum + i    
    else:
        print("entered value is invalid")

avg1=sum/3

sum=0    
for i in tr2:
    if(i > 0 and i <= 100):
        sum= sum + i     
    else:
        print("entered value is invalid")
avg2=sum/3

sum=0        
for i in tr3:
    if(i > 0 and i <= 100):
        sum = sum + i
    else:
        print("entered value is invalid")
avg3=sum/3

if(avg1 >= avg2 and avg1 >= avg3):
    print("tr1 is mostfit")
if(avg2 >= avg1 and avg2 >= avg3):
    print("tr2 is mostfit")
if(avg3 >= avg1 and avg3 >= avg2):
    print("tr3 is mostfit")

print(avg1,avg2,avg3)
