# Random Password Genrator in Terminal
import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit = '0123456789'
symbol = '~`!@#$%^&*()_-+<>|'

String = lower+upper+digit+symbol
length = 12
password = "".join(random.sample(String,length))
print("Your Password Is : ",password)