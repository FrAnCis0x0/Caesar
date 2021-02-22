#! /usr/bin/python3
import sys,os,time

#this function is to remove all none ascii characters and takes one argument
def convert_to_Caesar(msg):
    
    #all character in msg are converted to uppercase
    msg = msg.upper()
    
    #msg is turned into a list of characters
    msg = msg.split()
    
    #msg is turn into one string
    msg = ''.join(msg)
    
    #clean_msg is store filtered characters
    clean_msg=''
    
    #allowed_characters will store characters a user is permited to use.
    allowed_characters=[]
    
    #a for loop to generate A-Z and append them to allow_characters
    for i in range(65,91):
        allowed_characters.append(chr(i))
        
    #this for loop will check weather each character in msg if true.
    #its appended to clean_msg esle its ignored
    #also it checks if each character is equal to ' . ' and if true it replaces it with ' X '
    #then it returns clean_msg when done.
    for j in msg:
        if j == '.':
            j = 'X'
        if j in allowed_characters:
            clean_msg += str(j)
    return clean_msg

#this function will display the logo everytime its called
def logo():
    print('\033[96m'+'\033[1m'+"""
  ____           ____            
 / ___|__ _  ___/ ___|  ___ _ __ 
| |   / _` |/ _ \___ \ / _ \ '__|
| |__| (_| |  __/___) |  __/ |   
 \____\__,_|\___|____/ \___|_|   
    """+'\033[0m')


#this function takes two arguments this function encrypts strings from clean_msg
def encrypt_result(word, num):
    #varaible string will store encrypted characters
    string = ''

    
    #for loop to loop for the length of variable word
    #j stores ascii code for each character in word plus num 
    for i in range(0,len(word)):                 
        j = ord(word[i]) + num%26
        
        #if statement to check if j is greater than 90
        #offset stores whatever j - 90 is
        #charNum stores the value of 64 + offset
        #varaible l  will keep the letter after its converted to a string
        #this appends value is l to string
        if j > 90:            
            offset = j-90                        
            charNum = 64 + offset            
            l = chr(charNum)                        
            string += l
            
        #else is to convert j in str then append j to string
        #if j is not greater than 90 and then returns string
        else:
            j = chr(j)
            string += j
    return string

#this may cause trouble when using windows or ide
def clear_screen():
	os.system('clear')

#function takes two and decrypts values from encrypt_result() function
def decrypt_result(word, num):
    #varaible string will store encrypted characters
    string = ''

    #for loop to loop for the length of variable word
    #j stores ascii code for each character in word minus num
    for i in range(0,len(word)):                  
        j = ord(word[i]) - num%26
        
        #if statement to check if j is less than or equal to 64 if true then
        #offset stores whatever 64 - j is
        #charNum stores the value of 90 - offset
        #varaible l  will keep the letter after its converted to a string
        #this appends value is l to string
        if j <= 64:
            offset =  64 - j
            charNum = 90 - offset
            l = chr(charNum)
            string += l
            
        #else is to convert j in str then append j to string
        #if j is not greater than 90 and then returns string
        else:
            j = chr(j)
            string += j
    return string

keeper = True
# this store 0 to 3
firstNumbers = [x for x in range(1, 6)]

#This function asks the user shift number and text to encrypt  
def Encrypt():
    print("[ENCRYPT]")
    try:
        rotation = abs(int(input("Enter the number of rotations: ")))
        text = input("Type your text: ")
        while text == ""or text == " ":
            clear_screen()
            text = input('\033[91m'+"Please Type Some Thing:  "'\033[0m')
        c_text = convert_to_Caesar(text)
        result = encrypt_result(c_text, rotation)
        print('\33[32m'+"ROT:"+'\33[0m'+f" {rotation}")
        print('\33[32m'+"Encrypted text:"+'\33[0m'+f" {result}")
        input('\33[6m'+"Press Enter To Continue..."+'\33[0m')
    except ValueError:
        clear_screen()
        print('\033[91m'+"Only numbers allowed!\n"+'\033[0m')
        Encrypt()
    
#This function asks the user shift number and text to decrypt   
def Decrypt():
    print("[DECRYPT]")
    try:
        rotation = abs(int(input("Enter the number of rotations: ")))
        text = input("Type your text: ")
        
        #this will check wether there is anything in text if not keep asking
        while text == ""or text == " ":
            clear_screen()
            text = input('\033[91m'+"Please Type Some Thing:  "+'\033[0m')
        #this will clean text from the user and then decrypt it.    
        c_text = convert_to_Caesar(text)
        result = decrypt_result(c_text, rotation)
        print('\33[32m'+"Decrypted text:"+'\33[0m'+f" {result}")
        input('\33[6m'+"Press Enter To Continue..."+'\33[0m')
        
    #this will run when a user enters anything other than a number.    
    except ValueError:
        clear_screen()
        print('\033[91m'+"Only numbers allowed!\n"+'\033[0m')
        Decrypt()
    
#funtion to ask user for an input        
def askUser():
    #this will loop until the user exits
    while keeper:
        #printing the logo and 
        logo()
        
        print("Select Your Option")
        print('''[1] - Manual
[2] - Encrypt
[3] - Decrypt
[4] - Exit()
''')
        try:
            choice = int(input('~$ '))
            if choice not in firstNumbers:
                askUser()
            elif choice == 1:
                Manual()
                clear_screen()
            elif choice == 2:
                Encrypt()
                clear_screen()
            elif choice == 3:
                Decrypt()
                clear_screen()
            elif choice == 4:             
                print("Bye!")
                sys.exit()
        except ValueError:
            clear_screen()
            print('\033[91m'+"Please use numbers [1-4]"+'\33[0m')
            askUser()
        

def Manual():
    clear_screen()
    print('\33[1m'+"""
                    [Description]"""+'\33[0m'+"""
                
"""+'\33[96m'+'\33[1m'+"""Caesar"""+'\33[0m'+'\33[32m'+""" is an encryption cipher that uses the 26 uppercase letters of the English alphabet.
Anything other than [A-Z]|[a-z] will be deleted.

[Encryption] - This ls altering data so that it appears random.

[Decryption] - This is taking encoded or encrypted text
               and converting it back into text you can
               understand.

[Rotation]   - This is the number of shift for
               each character to move.

[Text]       - This should be the text you want to encrypt of Decrypt.

"""+'\33[0m'+ '\033[93m' + '\033[1m' +"""NOTE: """ + '\033[0m' + '\33[32m'+"""Always use the some number of rotations used to Encrypt when Decrypting

BUGS: Currently there are no bugs in this project and if found feel free to point them out.

ENJOY! :)
             
        """+'\33[0m')
    input('\33[6m'+"Press Enter To Continue..."+'\33[0m')
    
  
if __name__ == "__main__":
    askUser()            
    
            

