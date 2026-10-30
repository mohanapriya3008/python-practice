Length of a string
Take a string from the input and print the length of that string
Input:
OneCompiler
Output:
11
a=input()
print (len(a))

Join the strings
Take two strings from the input, join those two strings with a space and print the new string
Input:
Harry
Potter
Output:
Harry Potter
a=input()
b=input()
print(a+" "+b)

Compare the Strings
Take two strings from the input and print whether or not the strings are equal
Input(1):
Hello
Hi
Output(1):
false
Input(2):
Hello
Hello
Output(2):
true

First character of a string
Take a string from the input and print the first character of that string
Input:
World
Output:
W
a=input()
print(a[0])

Last character of a string
Take a string from the inPut and print the last character of that string
Input:
World
Output:
d
a=input()
print(a[-1])

Join first & last characters of a string
Take a string from the input and print the first character and last characters of the string together
Input:
Hello World
Output:
Hd
a=input()
print(a[0]+a[-1])

Alphanumeric strings
Take a string from the input and check whether or not it contains both letters and numerals
Input(1):
R2D2
Output(1):
true
Input(2):
OC
Output(2):
false
a=input()
le=num=False
for i in a:
  if i.isalpha():
    le=True
  elif i.isdigit():
    num=True
if le and num:
  print("true")
else:
  print("false")

Uppercase check
Take a string from the input and check all the letters in the string are of upper case
Input(1):
OC
Output(1):
true
Input(2):
oc
Output(2):
false
a=input()
if a.isupper():
  print("true")
else:
  print("false")

Lowercase check
Take a string from the input and check all the letters in the string are of lower case
Input:
OC
Output:
false
Input:
oc
Output:
true
a=input()
if a .islower():
  print("true")
else:
  print("false")

String lengths equal or not
Take two strings from the input and check the lengths of those strings equal or not
Input:
Peter
Griffin
Output:
false
a=input()
b=input()
if(len(a)==len(b)):
  print("true")
else:
  print("false")

Reverse a string
Take a string from the input and print it in reverse
Tom
Output:
moT
a=input()
print(a[::-1])

Split strings by comma
Take a string from the input and split the strings with comma. Print the new strings one per line
Input:
a,b,c,d
Output:
a
b
c
d
a=input()
b=a.split(",")
for i in b:
  print(i)

Remove vowels
Take a string from the input and remove the vowels and print it\
Input:
Harry
Output:
Hrry
a=input()
temp=""
for i in a:
  if i not in "aeiouAEIOU":
    temp=temp+i
print(temp)

Reverse the character case
Max Score: 7 | Difficulty: Not Specified

Take a string from the input and change lowercase characters to uppercase and uppercase characters to lowercase
Input:
Harry
Output:
hARRY
  
