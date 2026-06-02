import random
while True : 
    c=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
    try :
        g=int(input("How long your password should be ?\n"))
        if g <=0 : 
            print("Password length must be greater than 0, please try again\n")
            continue 
        else : 
            break
    except:
        print("please put your answer in numbers") 
        continue 
       
password = ""
for i in range (g) : 
    password+=random.choice(c) 
print(f"your password is \n{password}")