ls =['0','0','0','0','0','0','0','0']
for x in range(0,8) :
    bit=input(f"Please Enter Bit {x} Mode :")
    if bit== "in" :               
        ls[x]='0'
    elif bit=="out":              
        ls[x]='1'    

bit = "".join(ls)
f=open("embeddedavr.c","w") 
#Writing to the file
script="void Init_Port_DDRA(void);{\nDDRA=0b"+bit+"\n}"
f.write(script)
f.close()