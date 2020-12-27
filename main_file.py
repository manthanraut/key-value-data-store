#here are the commands to demonstrate how to access and perform operations on a main file

#run mail_file.py and import db_operations.py as a library
from db_operations import create,delete,read,modify
#importing the main file("db_operations" is the name of the file I have used) as a library

create("information",45)
#creating a key with key_name,value given and with no time-to-live property

create("informationsync",80,3600)
#creating a key with key_name,value given and with time-to-live property value given(number of seconds)

read("info")
#it may return error
read("information")
#it returns the value of the respective key in JSONobject format 'key_name:value'

read("informationsync")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR

create("information",20)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it

modify("information",50)
#it replaces the initial value of the respective key with new value 

delete("information")
#it deletes the respective key and its value from the database(memory is also freed)

create("info123",35)
#return invalid key error

create("info_$",35)
#returns invalid key error

create("info",35)
#adds new key to database

#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB

