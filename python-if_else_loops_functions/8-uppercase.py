#!/usr/bin/python3
def uppercase(str):
    result = ""
   for c in str:
       if 97 <= ord(c) <= 122:
           result += c(ord(c)-32)
           print(result)
       else:
           result+=c
           print(c)
