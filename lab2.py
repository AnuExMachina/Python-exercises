# zadanie 1
string = input("Please pass a string:\n")
srcsep = input("Please pass a separator:\n")
sep = input("Please pass a separator:\n")


result = string.split(srcsep)
print(result)
print(sep.join(result))

# zadanie 2

string = input("Please pass a string:\n")
res_first = string[0:len(string)//2] 
res_second = string[len(string)//2:]
print(f"first string: {res_first}, second string: {res_second}")

print(string[::-2])

# zadanie 3

print(string.title())
print(string.capitalize())
print(string.zfill(20))
print(string.upper())
print(string.count('a'))
print(string.center(20))

# zadanie 4


wejscie = input() 
print(f"Łańcuch {wejscie} isdecimal: {wejscie.isdecimal()}")
print(f"Łańcuch {wejscie} isalpha: {wejscie.isalpha()}")
print(f"Łańcuch {wejscie} isascii: {wejscie.isascii()}")
print(f"Łańcuch {wejscie} isprintable: {wejscie.isprintable()}")
print(f"Łańcuch {wejscie} istitle: {wejscie.istitle()}")
print(f"Łańcuch {wejscie} isupper: {wejscie.isupper()}")


#zadanie 5 w pliku lab21.py

#zadanie 6

print(chr(35))
print(chr(58))
print(chr(59))
print(chr(62))
print(chr(34))

