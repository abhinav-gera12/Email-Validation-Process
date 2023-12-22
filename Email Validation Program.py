# Email Validation Program
# a-z small letters
# 0-9 numeric digits
# use of . or _ 
# use of @ once 
# . 2nd or 3rd position from last (eg - .com or .in, .org )

email = input("Enter your email address: ")
space = 0
upper = 0
wrongly_inputed = 0

if len(email) >= 6:                                                     #1: Length should be greater or equal to six
    if email[0].isalpha():                                              #2: Checking the first alphabat 
        if "@" in email and email.count("@")==1:                        #3: checking @ and count of @ must be once
            if email[-4] == "." or email[-3] == ".":                    #4: checking dot(.) from the last postition 
                for i in email:                             #iterating single character from loop
                    if i==i.isspace():                                  #5: checking the spaces in between
                        space == 1
                    elif i.isalpha():                                   #5: checking character as an alphabet  
                        if i == i.upper():
                            upper == 1
                    elif i.isdigit():                                   #5: checking digit inside the email
                        continue
                    elif(i =="_") or (i ==".") or i =="@":              #5: checking _,.,@ is valid as per syntax of email address
                        continue
                    else:
                        wrongly_inputed = 1                          
                if space == 1 or upper == 1 or wrongly_inputed == 1:            #if spaces, upper case letter, or some other special symbol found in the user input then, it will throw the error no.5
                    print("Error 5: Invalid Email Address because there should neither contain any upper case letter nor the special symbols nor any spaces in between.")
                else:
                    print("Correct Email Address")
            else:
                print("Error 4: Invalid Email address becuase the dot(.) must be inside your email address before any suffix")                
        else:
            print("Error 3: Invalid Email address because it must contains the single '@'")
    else:
        print("Error 2: Invalid Email address because the email always starts from the alphabet")
else:
    print("Error 1: Invalid Email address because the length must be 6 or more")
