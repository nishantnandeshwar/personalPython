text="Nishant DEwanand Nandeshwar Nishant nandeshwar"
sample=[]
new=''
for i in range(1):
    sample.append(text)
sample1 =[i.split() for i in sample]

#print("sample1=",sample1)
for j in sample1:
    #print("j=",j)
    for x in j:
        #print("x=",x)
        for c in range(0,len(x)):
            #print("c=",c)
            #print(x[c])
            if (x[c].isupper())== True:
                new+=x[c].lower()
            else:
                new+=x[c].lower()
            print("new=",new)

        
   






