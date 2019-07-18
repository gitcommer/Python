# 1 Input / Variables types / Output
# Using the variable age, ask the user to input his or her age
# Calculate how many years until retirement (age 65)
# Print the results like the following: You can retire 23 years from now in 2038.

age = input("Please enter your age: ")	#01 input 31
age = int(age)							#02 assign 31 to int variable

years_to_retirement = 65 - age			#03 65 - 31 = 34
year_of_retirement = 2019 + years_to_retirement		#04 2019 + 34

print("You can retire %s years from now in %s." %(years_to_retirement, year_of_retirement))

# output:	Please enter your age. > 31
# 			You can retire 34 years from now in 2050.

# ---------------------------------------------------

# 2 Conditionals
# Using the variable name, ask the user to input his or her name
# Check to see if the first letter of the name is the same as the last letter.
# Print the results like the following:
# The name Anjana starts and ends with the same letter
# The name Giulia does not start and end with the same letter.

name = input("Please enter your name: ")
first = name[0]  #01 count the letter of input Cinco
last = name[-1]

if first.upper() == last.upper():
	print("The name %s starts and ends with the same letter. " %name)
else:
	print("The name %s does not start and end with the same letter. " %name)

# output: 	Please enter your name: Cinco
# 			The name Cinco does not start and end with the same letter.

# ---------------------------------------------------

# 3 Loops
# using the variable i, ask the user to input a number between 1 to 100
# Calculate the sum of all the numbers from 1 to i (include)
# You must use a loop

i = input("Please enter a number from 1 to 100: ")
i = int(i)

sum = 0

for i in range(1, i + 1):  # loop 1,2,6,10,15
	sum += i

print (sum)

# output: 	Please enter a number from 1 to 100: 5
# 			15

# ---------------------------------------------------

# 4 Functions
# Create a function called squaroot that accepts an integer
# Have the function return the square of the integer that is sent
# Ask the user to input a number and use the function you created to square it
# Print the results like the following
# The square of 4 is 16

def squaroot(value):
	square = value ** 2
	return square

number = input("Please enter a number: ")
number = int(number)

result = squaroot(number)

print("The square of %s is %s. " %(number, result))

# output: 	Please enter a number: 4
# 			The square of 4 is 16.

# ---------------------------------------------------

# 5 Lists
# Create a list of students in out class that is not in alphabetical order
# Put the list into alphabetical order
# Using a loop, print the list like the following:
# Anchal is in our class.
# Hae-Rang is in our class.
# Kazuki is in our class.

students = ["hae-Rang", "Kazuki", "Anchal"]
students.sort()

for student in students:
	print("%s is in our class." %student)

# output: 	Anchal is in our class.
# 			Kazuki is in our class.
# 			hae-Rang is in our class.

# ---------------------------------------------------

# 6 Dictionaries
# Create a dictionary called words that maps the following vocabulary words
# hello: buna
# goodbye: la revedere
# thank you: multumesc
# Ask the user to enter an english word (from this list)
# Check to see id the word is in the dictionary. if it is print the result like the following
# The word hello is buna in Romanian.
# If the word is not in the dictionary, please print the following:
# Sorry, that word is not in the dictionary.

words = {"hello":"buna", "goodbye":"la revedere", "thank you":"multumesc"}

english = input("Please enter an english word: ")

if english in words:
	romanian = words[english]
	print("This word %s is %s in Romanian." %(english, romanian))
else:
	print("Sorry, that word is not in the dictionary.")

# output: 	Please enter an english word: hello
# 			This word hello is buna in Romanian.

# ---------------------------------------------------

# 7 Classes
# Create a class called student
# Give the student the following attributes:
# Name
# Grade
# nationality
# Create a class method to change the grade called changeGrade.
# Create a student instance with your name and define the name, grade, and nationality
# Print the information like the following:
# Christian is in grade 11.
# Christian is American.
# Using the class mehtod changeGrade, change the grade to 12 and print "Christian is in grade 12."

class Student:
	def __int__(self, name, grade, nationality):
		self.name = name
		self.grade = grade
		self.nationality = nationality

	def changeGrade(self, grade):
		if grade > 0 and grade < 13:
			self.grade = grade

christian = Student("Christian", 11, "American")

print("%s is in grade %s" %(christian.name, christian.grade))
print("%s is %s." %(christian.name, christian.nationality))

christian.changeGrade(12)
print("%s is in grade %s" %(christian.name, christian.grade))

# output: 	Christian is in grade 11
# 			Christian is American
# 			Christian is in grade 12