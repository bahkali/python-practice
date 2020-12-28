import re

#can use website like regular expression 101 to help you generate it
#No need to memorize it
string = "search this inside of this text please! Kaly"
parttern = re.compile(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
string2 ='kalimamadougmail.com'
a= parttern.search(string2)
b= parttern.fullmatch(string2)
print(a)
print(a)