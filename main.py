import string
import random
if __name__ == '__main__':
    s1=string.ascii_lowercase
   # print(s1)
    s2=string.ascii_uppercase
    s3=string.digits
    #s4=string.punctuation
    plength=int(input("enter the lenght of the password"))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
   # s.extend(list(s4))
    random.shuffle(s) 
    print(s)    
    print("Your password is  ")
    print("".join(s[0:plength]))
    #print("".join(sample.shuffle(s,plength))