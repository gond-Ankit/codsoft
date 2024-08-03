import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    
    s2 = string.ascii_uppercase
   
    s3 = string.punctuation
    
    s4 = string.digits    
    plen = int(input("ENTER THE LENGTH OF THE DESIRED PASSWORD :\n")) 
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    print("YOUR PASSWORD IS : ")
    print("".join(random.sample(s, plen)))
    
    