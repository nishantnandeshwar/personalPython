print("0: Nishant,1:Dewanand,2:Nandeshwar,3:Kumud,4:punyai,5:exit")
switch={0:"Nishant",1:"Dewanand",2:"Nandeshwar",3:"Kumud",4:"punyai"}
while 1:
    x=int(input("enter no:"))
    print(switch.get(x))
    if(x==5):
        exit()
