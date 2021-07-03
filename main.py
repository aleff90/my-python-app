print("Hello Amigoscode")

name, age = "Jamila", 20
pi = 3.14
number = [1, 2, 3, 4]

print(name)
print(age)
print(pi)
print(number)

print("---")
brand = "Amigoscode"
age = 2
pi = 3.14
numbers = []
isAdult = True
print(type(brand))
print(type(age))
print(type(numbers))
print(type(pi))
print(type(isAdult))

print("---")
otherBrand: str = "Amigoscode2"
otherIsAdult: bool = False
print(type(otherBrand))
print(type(otherIsAdult))

#method
def hello():
    return "hello"

#I am a comment
#print("hello")

"""
I am a comment
a second comment
third comment
print("hello")
"""

print("---")
anotherBrand = 'Amigoscode'
#print(anotherBrand.upper())
#print(anotherBrand.replace('A','a'))
#print(anotherBrand.replace('A','33'))
print(len(anotherBrand))
print(anotherBrand == "amigoscode")
print(anotherBrand != "amigoscode")
print("code" in anotherBrand)
print("code" not in anotherBrand)

#print in one line
print("---")
comment = "da asd dammoda " \
          "dasdasnk" \
          "dasnjnasd" \
          "da"
print(comment)

#print in each line
print("---")
otherComment = """
asdhgjeeijkj
sdfsdf
gds
gdsgsd
"""
print(otherComment)

print("---")
#name = "Kamilla"
#email = """
#hello {},
#how are you?
#It was nice talking to you
#"""
#print(email.format(name))
name = "Kamilla"
email = f"""
hello {name},
how are you?
It was nice talking to you
age {4+4}
"""
print(email)














