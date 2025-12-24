s1="python is fun"
print(s1[0])
print(s1[-1])
print(len(s1))
print("------------------------------")

# * ---> strings repetition operator
s2="Python"
print(s2*5)
print("------------------------------")

#in ---> membership operation
s3="Python is fun"
print("Python" in s3)
print("z" in s3)
print("python" in s3)
print("------------------------------")

#not in ---> membership operation
print("Python" not in s3)
print("z" not in s3)
print("python" not in s3)
print("------------------------------")

#comparision of strings
print("python" == "python")
print("python" == " python")
print("python" == "Python")
print("------------------------------")

# strip - remove spaces in string
s4="Python    "
s5=s4.strip()
print(s4=="Python")
print(s5=="Python")
print("------------------------------")

# replace
s6="I am learning Java"
print(s6.replace("Java","Python")) #returns new string
print("------------------------------")

#count - to count of substring in main string
s7="Python is fun. Python also a programming language"
print(s1.count("Python"))
print(s1.count(" "))
print("------------------------------")

#change in cases
s8="Python is fun"
print(s8.upper())
print(s8.lower())
print(s8.isupper())
print(s8.islower())
print(s8.title()) #first letter of each word changes
print(s8.capitalize()) ##first letter of entire string changes
print("------------------------------")

#starting and ending of strings
s9="we are learning python"
print(s9.startswith("python"))
print(s9.endswith("python"))







