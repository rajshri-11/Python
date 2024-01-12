# given string
s = "assassa"
reverse_string = ""
for i in s:
    reverse_string = i + reverse_string  
if(s == reverse_string):
   print("The string",s,"is a Palindrome.")  
else:
   print("The string",s,"is NOT a Palindrome.")
