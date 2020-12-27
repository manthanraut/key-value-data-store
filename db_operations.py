import threading
from threading import*
import time

#'d' is the dictionary in which we will store the data
d={}
#for create operation we can use create use syntax--> create(key_name,value,timeout)
# NOTE: timeout is optional we can continue by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in d:
        #checking if key passed is already present or not
        print("Error : this key cannot be used because it already exists") #error message1
    else:
        #if key is unique we check for its validation to be only alphabetic key
        if(key.isalpha()):
            # Here 1 GB is 1024^3 bytes (i.e., 1 GiB) and 16KB is 16x1024^2
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and JSON object value less than 16KB
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
            else:
                print("Error: Memory limit exceeded!") #error message2
        else:
            print("Error: Invalid key! Key name must only contain alphabets. No special symbols or numbers are allowed.") #error message3

#for read operation use syntax--> read(key_name)
            
def read(key):
    if key not in d:
        print("Error: Given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                ans=str(key)+":"+str(b[0]) #to return the value in the format of JSONObject i.e.,"key_name:value"
                return ans
            else:
                print("Error: Time-To-Live of",key,"has expired") #error message5
        else:
            ans=str(key)+":"+str(b[0])
            return ans

#for delete operation use syntax--> delete(key_name)

def delete(key):
    if key not in d:
        print("Error: given key does not exist in database. Please enter a valid key") #error message6
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("Key is successfully deleted.")
            else:
                print("Error: Time-To-Live of",key,"has expired") #error message7
        else:
            del d[key]
            print("Key is successfully deleted.")

#we can even add an additional operation to modify in order to change the value of key before its expiry time if provided
#for modify operation use syntax--> modify(key_name,new_value)

def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("Error: Given key does not exist in database. Please enter a valid key") #error message8
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("Error: Time-To-Live of",key,"has expired") #error message9
    else:
        if key not in d:
            print("Error: Given key does not exist in database. Please enter a valid key") #error message10
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l
