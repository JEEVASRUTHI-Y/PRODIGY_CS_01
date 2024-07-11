#Implement Caser Cipher
'''Create a Python program that can encrypt
 and decrypt text using the Caesar Cipher
 algorithm. Allow users to input a message 
 and a shift value to perform encryption and 
 decryption'''
 
c="YES"
#Initialising the value of c

while(c=="YES"):
    
    coded_word=""
    
    text=input("Enter the Actual text:")
    
    #Getting input of the actual text
    
    shift=int(input("Enter the shift value:"))
    
    #Getting input of shift value
    
    for i in range(len(text)):
        
        #for loop for iterating each character of the text 
        
        char=text[i]
        
        if char==" ":
            
#if the character is a space
            
            coded_word=coded_word+" "
            

        elif char.islower():
        
#else the character is in lowercase
            
            sb=chr((ord(char)+shift-97)%26+97)
            
            coded_word=coded_word+sb
            
        elif char.isupper():
            
#else the character is in uppercase
            
            sb=chr((ord(char)+shift-65)%26+65)
            
            coded_word=coded_word+sb
            
    print("The Cipher Text is:",coded_word)
    
    c=input("Do you want to again input a message to convert to Cipher text?")