import pyperclip
SYMBOLs="ABCDEFGHIJKLMNOPQRSTUVWXYZ"


while True:
    asking=input("DO you want to encrypt or decrypt?")
    if asking=='encrypt':
        mode="e"
        break
    elif asking=='decrypt':
        mode='d'
        break
    else:
        print("PLease Enter whether you want to encrypt or decrypt")
        continue
while True:
    maximum_key=len(SYMBOLs)-1
    key_input=input("Enter the key you want:")
    try:
        if key_input.isdecimal():
            if 0< int(key_input) < len(SYMBOLs):
                key=int(key_input)
                break
    except:
        print("Enter the numbers only as a key:")
        continue


message=input("Enter the message you want to e or d:")

translated=''

for letter in message:
    if letter in SYMBOLs:
        pos=SYMBOLs.find(letter)
        if mode=='e':
            pos=pos+key
        else:
            pos=pos-key
        
        if pos > len(SYMBOLs):
            pos=pos=len(SYMBOLs)
        if pos<0:
            pos=pos+len(SYMBOLs)
        translated=translated + SYMBOLs[pos]
       

    else:
        translated=translated+letter
        print(translated) 
      
print(translated)       


