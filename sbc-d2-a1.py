#index
#text = "hello world"
#        01234567891011
#      - 12110987654321
#word = input ("word: ")
#print(text[9])
# -3 -2 -1 0 1 2 3 4 5 6 7 8 9
#print(word[len(word)-1])
#a l p e c h e 
#0 1 2 3 4 5 6

#slicing
#text = "hello world"
#       01234567891011
#     - 121110987654321
#print(text[0:2], text[6:8])
#print ("{0} {1}".format(text[0:2], text[6:8]))
#print(f"{text[0:2]} {text[6:8]}")

#stringmethod
#word = "helloworld"

#print(word.upper()) #if gsuto nimo i uppercase ang string
#print(word.lower()) #if gusto nimo i lowercase ang string
#print(word.capitalize()) #if gusto nimo capitalize ang first character
#print(word.title()) #tanan character is capitalize good for title 
#print(word.replace("h", "x")) #if gusto nimo mag replace og character
#print(word.find("h")) #finding the length of the character sample starting with "0" 0123456789
#print(word.isalpha()) #checking if its only character space is not character but social char which may result of false when applying space
#print(word.isnumeric()) #check if its only numbers
#print(word.isalnum()) #will return true if all are characters/alphabet and numbers/numeric

#word =  #summer bootcamp

#Summer Bootcamp
#Summer bootcamP
#Loot
#camE
#AR
#True = Alpha

word = "summer bootcamp"
       #01234567891011121314

#print(word.capitalize())
#print(word[len(word)0:14]).capitalize())
#print(word[0:14]).capitalize()

#print(word.replace("s", "S"))

print(word.title())
print(word.capitalize().replace("p", "P"))
print(word[7:11].replace("b", "L"))
print(word[11:15]. replace("p", "E"))
print(word[12].capitalize() +word[5].capitalize())
print(word.replace(" ","hiddenspace").isalpha())

#print(word[12].upper() + word[5]())
