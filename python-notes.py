"""
error - mo matter and spacing in python code

note:     - everything in python is an object or function
          - there are two types of number in python integers and float
          - python start always in 0
          - inig human nimo og input adto mag start sa top ang pag read sa code
          - ang pag overrinde sa variable kay padulong sa ubos

          - class - declare variable or object
          - instance - is where the value provide
          - mehtod -  where you access the data to print

^Z - like clear in cmd
cmd/type 'python' - this will create a shell na pwede ka mag code og python diri
run python file - python filename.py
function
integer
float
division returns float value 5 / 5  output: 1.5
division returns integer value - 5 // 5  output: 5
to the power - 5 ** 5 //meaning 5*5*5*5*5 = 3125
modulo - 10 % 3
order of operation - 5 + 5 * 3  //5*3=15+5 = 20
                   - use BIDMAS or dali ang pagamit sa order of operation like
                         B - bracket
                         I - indices like + - * / or // ** % etc.
                         D - division
                         M - multiplication
                         A - addition
                         S - subtraction

                         example: (5 + 5) * 3
variable
strings
methods
lists like arrays
    - list inside list
    - list comprehension - long and short way code
input   - input data to editor and display to console
comment - #
typecasting - changing string to integer 
if statements
for loops
while loops
ranges    - meaning range og number like print 1-5, 3-10
functions - you can call the code whenever you need
          - yo can also pass the function to function #---sample6---
variable scope - global variable - naa sa "gawas" sa function ang variable
               - local variable - naa sa "sulod" sa function ang variable
dict or distionaries - same siya og array pero maka search ka og data sa list
sorting - sorting number or letter
sets - this will remove duplicate data
classes - can check what data inside
init funtion or the constructors
methods and attributes
     - printing global variable
     - @classmethod - maka access siya og data weather in class or method
     - @staticmethod - meaning wla siyay restrictions method siya na pwede ma access bisan unsa
modules - you can import a class
bar tab calculator
shuffle letter in words using map and comprehension code style
filter
lambdas - is like anonymous function no name function
decorators - is a wrapper function
reading and closing files
writing files - write data of txt file
themed lorem ipsum generator - input number of paragraph and display to txt file
downloading images - input number of paragraph and display to txt file




function
********
type(5)  //type is the function in python with integer value
type(3.142)  //float value

variable
********
---sample1---
age = 25    //ingon ani-on pag declare og variable
age         //display the variable
age + 5
30
age         //note: but if you type age again it will display the 25 value to update do like this
age = age + 5 or age += 5
age

---sample2---
wages = 1000
bills = 200
rent = 500
food = 200
savings = wages - bills - rent - food
savings

strings
*******
sample1 - "hello" or 'hello'
sample2 - "he's a mad man" or 'he\'s a mad man' (if single qoute)
sample3 - greet = 'hello'
          greet[0]  //this will display 'h'
          greet[-0]  //this will display 'o'
          greet[0:3]  //this will display 'hel'
          greet[2:-1]  //this will display 'll'
sample4 - str1 = 'dudes'
          str2 = 'duddies'
          str1 + ' ' + str2  //display dudes duddies
sample5 - dudes * 3  //display dudesdudesdudes

methods
*******
sample1 - greet = 'hello'
          greet.upper()     //display HELLO
sample2 - greet = greet.upper()
sample3 - chesses = "brie, chedder, stilton"
          chesses.split(',')  //display ['brie', 'chedder', 'stilton']
sample4 - len(greet)  //display 5

lists like arrays
*****************
sample1 - fib1 = [1, 1, 2, 3, 5, 8, 13]
          fib1   //display [1, 1, 2, 3, 5, 8, 13]
          fib1[4]   //display 5
          fib1[-1]   //display 13
          fib1[0:4]   //display [1, 1, 2, 3]
sample2 - fib1 = [1, 1, 2, 3, 5, 8, 13]
          fib2 = [21, 34, 55]
          fib1 + fib2  //[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
sample3 - fib1[0] = 9
          fib1 = [9, 1, 2, 3, 5, 8, 13]  //change 0 to 9 in sample2
sample4 - fib1 = [1, 1, 2, 3, 5, 8, 13]
          fib2 = [21, 34, 55]
          fib1 + fib2  //[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
          fib.append(89)
          fib  //display [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
          fib.pop()  //display [1, 1, 2, 3, 5, 8, 13, 21, 34, 55] "remove" 89 because 89 is the newly append or inserted data
          fib.remove(89)  //this will only remove one 89 in array
          del(fib[10])  //this will delete all 89 in array
sample5 - chars = ['mario', 'luigi', 'bowser']
          chars.append(5)  //displays ['mario', 'luigi', 'bowser', 5]

list inside list
****************
sample6 - nums = [chars, fib1, [1,2,3,4]]  //display [['mario', 'luigi', 'bowser', 5], [1, 1, 2, 3, 5, 8, 13], [1,2,3,4]]
          nums[0]  //displays ['mario', 'luigi', 'bowser', 5]
          nums[2][1]  //display 2

input
*****
sample1 - input('Tell me your name punk: ')
          cmd: python filename.py

sample2 - name = input('Tell me your name punk: ')
          print('hello' + name)

sample3 - name = input('Tell me your name punk: ')
          age = input('Tell me your age punk: ')
          print(name, 'you are', age)



list comprehension - long and short way code
******************
#-----sample1-----
# prizes = [5, 10, 50, 100, 1000]

# dbl_prizes = []  #empty list or array assing to dbl_prizes 
# for prize in prizes:
#    dbl_prizes.append(prize*2)  #add data on dbl_prizes and times with 2

# print(dbl_prizes)

# output: [10, 20, 100, 200, 2000]


#-----sample2-----
# prizes = [5, 10, 50, 100, 1000]

# # ex1
# dbl_prizes = []  #empty list or array assing to dbl_prizes 
# for prize in prizes:
#    dbl_prizes.append(prize*2)  #add data on dbl_prizes and times with 2
# print(dbl_prizes)

# #or

# # ex2
# dbl_prizes = [prize*2 for prize in prizes]
# print(dbl_prizes)


# note:  ex1 and ex2 are the same result


#-----sample3-----
prizes = [5, 10, 50, 100, 1000]

# ex1 long way
dbl_prizes = []  #empty list or array assing to dbl_prizes 
for prize in prizes:
     dbl_prizes.append(prize*2)  #add data on dbl_prizes and times with 2
print(dbl_prizes)

# ex1 short way
dbl_prizes = [prize*2 for prize in prizes]
print(dbl_prizes)

# note:  ex1 are the same result

#-----------------------------------------

nums = [1,2,3,4,5,6,7,8,9,10]

# ex2 long way
squared_even_nums = []
for num in nums:
     if (num ** 2) % 2 == 0:  #if number is even
          squared_even_nums.append(num ** 2)
print(squared_even_nums)

# output:      [4, 16, 36, 64, 100]

# ex2 short way
squared_even_nums = [num ** 2 for num in nums if (num ** 2) % 2 == 0]
print(squared_even_nums)

# note:  ex2 are the same result



typecasting
***********
sample4 - radius = input('Enter the radius of your circle(m): ')
          area = 3.142*int(radius)**2  //01. int(radius) is string and change it to integer
          print('The area of your circle: ', area)

sample5 - num1 = 3.1425467389
          num2 = 10.2903948

          #print('num 1 is' num1, 'and num 2 is', num2)
          #or
          #print('num1 is {0} and num2 is {1}'.format(num1, num2))   # 0 is the num1 and 1 is the num2
          #or
          #print('num1 is {0:.3} and num2 is {1:.3}'.format(num1, num2))   # output: num1 is 3.14 and num2 is 10.3 or the (round of)
                                                                                          # 1:.3 this is called 1 is the percession of 3 or the (round of)
          #or
          #print('num1 is {0:.3f} and num2 is {1:.3f}'.format(num1, num2)) # output: num1 is 3.143 and num2 is 10.290 (3 decimal number like .143)
                                                                                               # 3f or float
          #or
          #print(f'num1 is {num1} and num2 is {num2}') # output: num1 is 3.1425467389 and num2 is 10.2903948 (same with first)
          #or
          print(f'num1 is {num1:.4f} and num2 is {num2:.4f}')    # output: num1 is 3.1425 and num2 is 10.2904 (4f is 4 decimal)


if statements
*************
sample1 - age = int(input('Enter your age: '))

          if age < 10:
               print('You are young, strange one')
          elif age < 40:
               print('The fire is so strong, strange one')
          else:
               print('You are wise beyond doubt')

sample2 - meaty = input(input('Do you eat meat? (y/n): ')

          if meaty == 'y':
               print('here is the meaty menu...')
          else:
               print('here is the veggie menu...')


for loops
*********
ninjas = ['ryu', 'crystal', 'yoshi', 'ken']

# for ninja in ninjas:   # display all
#    print(ninja)
#or
# for ninja in ninjas[1:3]:   # display only crystal and yoshi
#    print(ninja)
#or
for ninja in ninjas:     # display only crystal and yoshi
     if ninja == 'yoshi':
          print(f'{ninja} - black belt')
          break
     else:
          print(ninja)


while loops
***********
sample1 - age = 25
          num = 0
          while num < age:
               print(num)     //output: 25 zeros

sample2 - age = 25
          num = 0
          while num < age:
               print(num)
               num += 1  //output: 1 to 25

sample2 - age = 25
          num = 0
          while num < age:
               if num % 2 == 0:    //num modulo by 2 if asnwer is equal to 0 then its true
               print(num)
               num += 1  //output: 1 to 25

sample3 - age = 25
          num = 0
          while num < age:
               if num % 2 == 0:    //num modulo by 2 if asnwer is equal to 0 then its true
                    print(num)
               if num > 10:   //if num kay greater na sa 10 then stop
                    break
               num += 1  //output: 1 to 25

sample4 - age = 25
          num = 0
          while num < age:
               if num == 0:
                    continue
               if num % 2 == 0:    //num modulo by 2 if asnwer is equal to 0 then its true
                    print(num)
               if num > 10:   //if num kay greater na sa 10 then stop
                    break
               num += 1  //output: 1 to 25

sample5 - age = 25
          num = 0
          while num < age:
               if num == 0:
                    num += 1
                    continue
               if num % 2 == 0:    //num modulo by 2 if asnwer is equal to 0 then its true
                    print(num)
               if num > 10:   //if num kay greater na sa 10 then stop
                    break
               num += 1  //output: 1 to 25


ranges
******
---sample1---
#for n in range(5): #or range(3,10) or ranges(0,20,4) meaning range by 4
#    print(n)

---sample2---
# burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']
# for n in range(len(burgers)):
#    print(n, burgers[n])

# output: 0 beef
#           1 chicken
#           2 veg
#           3 supreme
#           4 double

---sample3---
burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']
for n in range(len(burgers)-1,-1,-1):
     print(n, burgers[n])

# output: 4 double       //display backward
#           3 supreme
#           2 veg
#           1 chicken
#           0 beef


functions
*********
#---sample1---
# def greet():  # def or define or the function
#    print('hello world')

# greet()  # you can call the code many times
# greet()
# greet()


#---sample2---
# def greet(name, time):
#    print(f'Good {time} {name}, hope you are well')

# greet('shaun', 'morning')


#---sample3---
# def greet(name, time):
#    print(f'Good {time} {name}, hope you are well')

#    name = input('enter your name: ')
#    time = input('enter your time of day: ')

# greet(name, time)


#---sample4---
# def greet(name = 'ryu', time = 'morning'):
#    print(f'Good {time} {name}, hope you are well')

# greet()


#---sample4---
# def greet(name = 'ryu', time = 'morning'):
#    print(f'Good {time} {name}, hope you are well')

# greet('shaun', 'afternoon')  # this code will override this def greet(name = 'ryu', time = 'morning'): data
#or
# greet(name = 'shaun')  # override name = 'ryu'


#---sample5---
# def area(radius):
#    print(3.142 * radius * radius)

# area(5)


#---sample6---
#def area(radius):

     # 7 * 3.142 * 7 = 153.958
     #return 3.142 * radius * radius  #02. get the inputed radius and calculate here

#def vol(area, length):

     # 153.958 * 8 = 1231.664
     #print(area * length)  #03. get the total of radius and multiply to inputed lenght 

#radius = int(input('Enter a radius: '))  #01. input number
#length = int(input('Enter a lenght: '))

#area_calc = area(radius)  #04. get the data of radius in function area() and assign to area_calc
#vol(area_calc, length)  #05. display data in the function vol()
#or
#vol(area(radius), lenght)  #pass the function to function

# output: Enter a radius: 7
#           Enter a lenght: 8
#           1231.664


variable scope
**************
#---sample1---
#my_name = 'ryu'  #this is a global variable because the variable kay naa sa gawas sa function

#def print_name();
#    print('The name inside the function is ', my_name)

# first print the function print_name() then print the function print()
#print_name()
#print('outside the function the name is ', my_name)


#---sample2---
#my_name = 'ryu'

#def print_name();

#    my_name = 'yoshi'  #meaning si ryu na variable gi ilisdan nimo og yoshi and sulod

#    print('The name inside the function is ', my_name)

#print_name()
#print('outside the function the name is ', my_name)


#---sample3---
my_name = 'ryu'

def print_name();
     
     global my_name  #this is use para ma global variable si my_name = 'yoshi' para ma access siya outside the function
     my_name = 'yoshi'

     print('The name inside the function is ', my_name)

print_name()
print('outside the function the name is ', my_name)


dict or dictionaries (cmd)
**************************
ninja_belts = {"crystal": "red", "ryu": "black"}  #"crystal": and "ryu": are called keys meaning pwede nimo i search sa dictionaries or dict
                                                              # red and blackare the values in the distionaries
ninja_belts  # this will display all
#or
ninja_belts['crystal']  #displays red
#or
ninja_belts['ryu']  #displays black
#or
'yoshi' in ninja_belts #displays False because yoshi is not on the list
#or
'ryu' in ninja_belts #displays True because yoshi is in the list
#or
ninja_belts.keys() #displays dict_keys(['crystal', 'ryu'])
#or
list(ninja_belts.keys()) #displays ['crystal', 'ryu']
#or
ninja_belts.values() #displays dict_values(['red', 'black'])
#or
vals = list(ninja_belts.values())
vals  #displays ['red', 'black']
#or
vals.count('black')  #displays 1 kong ika pila siya sa list or display 0 if data is not on the list
#or
ninja_belts['yoshi'] = 'red'
ninja_belts  #this will add new data on the list like {'crystal': 'red', 'ryu': 'black', 'yoshi': 'red'}
#or
person = dict(name="shaun", age=27, height="6ft")
person  #displays {'name': 'shaun', 'age': 27, 'height': '6ft'}


dict or dictionaries (index.py)
*******************************
def ninja_intro(dictionary):
     for key, val in dictionary.items():
          print(f'I am {key} and I am a {val} belt')

ninja_belts = {}

while True:
     ninja_name = input('enter a ninja nama: ')
     ninja_belt = input('enter a belt colour: ')
     ninja_belts[ninja_name] = ninja_belt

     another = input('add another? (y/n)')
     if another == 'y':  #if enter y the continue input
          continue
     else:
          break  #if enter n display inputed data

ninja_intro(ninja_belts)

# output:      enter a ninja nama: yoshi
#              enter a belt colour: black
#              add another? (y/n)y
#              enter a ninja nama: crystal
#              enter a belt colour: red
#              add another? (y/n)y
#              enter a ninja nama: ryu
#              enter a belt colour: green
#              add another? (y/n)n
#              I am yoshi and I am a black belt
#              I am crystal and I am a red belt
#              I am ryu and I am a green belt


sorting
*******
#---sample1---
#nums = [1,4,2,7,3,8,3,4,8,1]
#sorted(nums)  #this will sort the number from smaller to large

#---sample2---
names = ['shaun', 'ryu', 'abe', 'Apple', 'Brian', 'shaun']
sorted(names)  #sort string but capital letter display display first than small letter


sets
****
#---sample1---
#nums = [1,4,2,7,3,8,3,4,8,1]
#set(nums)  #this will remove duplicate number

#---sample2---
names = ['shaun', 'ryu', 'abe', 'Apple', 'Brian', 'shaun']
set(nums)  #this will remove duplicate number but not in-order

#---sample3---
ninjas = {'ryu': 'black','yoshi': 'red', 'crystal': 'black'}
ninjas.values()  #displays dict_values(['black', 'red', 'black'])
set(ninjas.values())  #displays {'red', 'black'} - remove duplicate

#---sample4---
def belt_count(dictionary):
     belts = list(dictionary.values())
     for belt in sets(belts):
          num = belts.count(belt)
          print(f'There are {num} {belt} belts')

ninja_belts = {}

while True:
     ninja_name = input('enter a ninja nama: ')
     ninja_belt = input('enter a belt colour: ')
     ninja_belts[ninja_name] = ninja_belt

     another = input('add another? (y/n)')
     if another == 'y':  #if enter y the continue input
          continue
     else:
          break  #if enter n display inputed data

belt_count(ninja_belts)


classes
*******
---sample1---
>>> name = 'shaun'
>>> age = 20
>>> nums = [1,2,3,4]
>>> type(name)
<class 'str'>
>>> type(age)
<class 'int'>
>>> type(nums)
<class 'list'>

---sample2---
class Planet:  #class

     def __init__(self):  #constructor
          self.name = 'Hoth'
          self.radius = 200000
          self.gravity = 5.5
          self.system = 'Hoth System'

hoth = Planet()  #instance
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'The gravity is: {hoth.gravity}')

output:   Name is: Hoth
          Radius is: 200000
          The gravity is: 5.5

---sample3---
class Planet:  #class

     def __init__(self):  #constructor
          self.name = 'Hoth'
          self.radius = 200000
          self.gravity = 5.5
          self.system = 'Hoth System'

     def orbit(self):
          return f'{self.name} is orbiting in the {self.system}'

hoth = Planet()  #instance
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'The gravity is: {hoth.gravity}')

print(hoth.orbit())

output:   Name is: Hoth
          Radius is: 200000
          The gravity is: 5.5
          Hoth is orbiting in the Hoth System


init funtion or the constructors
********************************
---sample1---
#note:    - self.name - self is the same of $this->

class Planet:  #class

     # constructor
     def __init__(self, name, radius, gravity, system):  #01. create constructors
          # you can assign any variable of self
          self.name = name  #02. assign constructors variable like self.name
          self.radius = radius
          self.gravity = gravity
          self.system = system

     # method
     def orbit(self):
          return f'{self.name} is orbiting in the {self.system}'

# first object or instance
hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')  #03. create instance and object and print data
print(f'Name is: {hoth.name}')  #hoth.name same of self.name
print(f'Radius is: {hoth.radius}')
print(f'The gravity is: {hoth.gravity}')
print(hoth.orbit()) # this will call def orbit(self):

# second object
naboo = Planet('Naboo', 300000, 8, 'Naboo System')
print(f'Name: {naboo.name}')
print(f'Radius: {naboo.radius}')
print(f'Gravity: {naboo.gravity}')
print(naboo.orbit()) # this will call def orbit(self):

# output: Name is: Hoth
#         Radius is: 200000
#         The gravity is: 5.5
#         Hoth is orbiting in the Hoth System

#         Name: Naboo
#         Radius: 300000
#         Gravity: 8
#         Naboo is orbiting in the Naboo System


---sample2---
# printing global variable

class Planet:

     shape = 'round'  #01

     # constructor
     def __init__(self, name, radius, gravity, system): 
          self.name = name  #
          self.radius = radius
          self.gravity = gravity
          self.system = system

     # method
     def orbit(self):
          return f'{self.name} is orbiting in the {self.system}'


# first object or instance
hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')  
print(f'Name is: {hoth.name}') 
print(f'Radius is: {hoth.radius}')
print(f'The gravity is: {hoth.gravity}')
print(hoth.orbit()) 

# second object
naboo = Planet('Naboo', 300000, 8, 'Naboo System')
print(f'Name: {naboo.name}')
print(f'Radius: {naboo.radius}')
print(f'Gravity: {naboo.gravity}')
print(naboo.orbit())

print(Planet.shape)  #02


---sample3---
# using classmethod - classmethod can access data both in class or method

class Planet:

     shape = 'round'  #01

     # constructor
     def __init__(self, name, radius, gravity, system): 
          self.name = name  
          self.radius = radius
          self.gravity = gravity
          self.system = system

     # method
     def orbit(self):
          return f'{self.name} is orbiting in the {self.system}'

     # this classmethod can access class data or method right away
     @classmethod  #02
     def commons(cls):
          return f'All planets are {cls.shape} because of gravity'



naboo = Planet('Naboo', 300000, 8, 'Naboo System')

# commons() function can access anything in the class
print(Planet.commons())  #03 accessing class data
print(naboo.commons())    #    accessing class data


---sample4---
# @staticmethod - meaning wla siyay restrictions method siya na pwede ma access bisan unsa

class Planet:

     shape = 'round' 

     # constructor
     def __init__(self, name, radius, gravity, system): 
          self.name = name  
          self.radius = radius
          self.gravity = gravity
          self.system = system

     # method
     def orbit(self):
          return f'{self.name} is orbiting in the {self.system}'

     # this classmethod can access class data or method right away
     @classmethod  #02
     def commons(cls):
          return f'All planets are {cls.shape} because of gravity'

     # @staticmethod meaning wla siyay restrictions method siya na pwede ma access bisan unsa
     @staticmethod  #01
     def spin(speed = '2000 miles per hour'):
          return f'The planet spins and spins a {speed}'


naboo = Planet('Naboo', 300000, 8, 'Naboo System')
print(Planet.spin())  #02


modules - you can import a class
*******
--sample1--
index.py       class Planet:

               shape = 'round' 

               # constructor
               def __init__(self, name, radius, gravity, system): 
                    self.name = name  
                    self.radius = radius
                    self.gravity = gravity
                    self.system = system

               # method
               def orbit(self):
                    return f'{self.name} is orbiting in the {self.system}'

               # this classmethod can access class data or method right away
               @classmethod  #02
               def commons(cls):
                    return f'All planets are {cls.shape} because of gravity'

               # @staticmethod meaning wla siyay restrictions method siya na pwede ma access bisan unsa
               @staticmethod  #01
               def spin(speed = '2000 miles per hour'):
                    return f'The planet spins and spins a {speed}'

text.py        from classes import Planet    #Planet is the planet.py file

               naboo = Planet('Naboo', 300000, 8, 'Naboo System')
               print(f'Name: {naboo.name}')
               print(naboo.spin('a very high speed'))


--sample2--
planet.py      class Planet:

               shape = 'round' 

               # constructor
               def __init__(self, name, radius, gravity, system): 
                    self.name = name  
                    self.radius = radius
                    self.gravity = gravity
                    self.system = system

               # method
               def orbit(self):
                    return f'{self.name} is orbiting in the {self.system}'

               # this classmethod can access class data or method right away
               @classmethod  #02
               def commons(cls):
                    return f'All planets are {cls.shape} because of gravity'

               # @staticmethod meaning wla siyay restrictions method siya na pwede ma access bisan unsa
               @staticmethod  #01
               def spin(speed = '2000 miles per hour'):
                    return f'The planet spins and spins a {speed}'


calc.py        def planet_mass(gravity, radius):

                    mass = (gravity*radius**2) / (6.67*10**-11)
                    return mass

               def planet_vol(radius):
                    vol = (4*3.142*radius**2)/3
                    return vol


classes.py     from space.planet import Planet    #space/planet.py space is the folder and planet.py is the file
               #from space.calc import planet_mass     #space/calc.py space is the folder and calc.py is the file planet_mass is the method in calc.py like def planet_mass(gravity, radius):
               #or
               from space.calc import planet_mass, planet_vol  #space/calc.py call the method planet_mass and planet_vol

               naboo = Planet('Naboo', 300000, 8, 'Naboo System')
               naboo_mass = planet_mass(naboo.gravity, naboo.radius)
               naboo_vol = planet_vol(naboo.radius)

               print(f'{naboo.name} has a mass of {naboo_mass} and a volume of {naboo_vol}')


bar tab calculator
******************
-----samle1-----
class Tab:

     menu = {  #dict
          'wine': 5,
          'beer': 3,
          'soft_drink': 2,
          'chicken': 10,
          'beef': 15,
          'veggie': 12,
          'desert':6
     }

     def __init__(self):
          self.total = 0
          self.items = []  #empty list masudlan siya basta naay i add na data

     def add(self,item):
          self.items.append(item)  #add item here
          self.total += self.menu[item]

     def print_bill(self, tax, service):
          tax = (tax/100)*self.total
          service = (service/100)*self.total
          total = self.total+tax+service

          for item in self.items:
               print(f'{item} P{self.menu[item]}')

               print(f'{"Total"} P{total:.2f}')  #2f is 2 decimal


# note:   - type this on cmd

#         1. python
#         2. from bar_tab import Tab         # bar_tab.py is a file and Tab is the class
#         3. table1 = Tab()                  # instance of class Tab
#         4. table1                          # run
#         5. table1.add('soft_drink')   # adding item on the list
#            table1.add('chicken')
#            table1.add('desert')
#            table1.print_bill(10,10)

# output: soft_drink P2
#              Total P21.60
#              chicken P10
#              Total P21.60
#              desert P6
#              Total P21.60


-----sample2-----
class Tab:

     menu = {  #01 this is the item na pwede nimo i add sa order list
          'wine': 5,
          'beer': 3,
          'soft_drink': 2,
          'chicken': 10,
          'beef': 15,
          'veggie': 12,
          'desert':6
     }

     def __init__(self):
          self.total = 0  #02 declare bariable na mahimo nimong sudlanan
          self.items = []

     def add(self,item):  #03 kapila ka mo add item to the list
          self.items.append(item)
          self.total += self.menu[item]

     def print_bill(self, tax, service):  #04 calculate the item
          tax = (tax/100)*self.total
          service = (service/100)*self.total
          total = self.total+tax+service

          for item in self.items:  #display the item
               print(f'{item:20} P{self.menu[item]}')  #01 :20 will add 10 space
               print(f'{"Total":20} P{total:.2f}')  #02 :20 will add 10 space


# note:   - type this on cmd

#         1. python
#         2. from bar_tab import Tab         # bar_tab.py is a file and Tab is the class
#         3. table1 = Tab()                  # instance of class Tab
#         4. table1                          # run
#         5. table1.add('soft_drink')   # adding item on the list
#            table1.add('chicken')
#            table1.add('desert')
#            table1.print_bill(10,10)        #10(tax) and 10(service charge)

# output:      soft_drink           P2
#              Total                P21.60
#              chicken              P10
#              Total                P21.60
#              desert               P6
#              Total                P21.60



shuffle letter in words using map and comprehension code style
**************
#-----sample1-----
# shuffle letter in a word

# from random import shuffle

# def jumble(word):
#    anagram = list(word)
#    shuffle(anagram)
#    return '-'.join(anagram)

# words = ['beetroot', 'carrots', 'potatoes']
# anagrams = []

# for word in words:
#    anagrams.append(jumble(word))
# print(anagrams)


#-----sample2-----
# using map

# from random import shuffle

# def jumble(word):
#    anagram = list(word)
#    shuffle(anagram)
#    return '-'.join(anagram)

# words = ['beetroot', 'carrots', 'potatoes']
# anagrams = []

# print(list(map(jumble, words)))


#-----sample3-----
# using comprehension or pinamobo na code

from random import shuffle

def jumble(word):
     anagram = list(word)
     shuffle(anagram)
     return '-'.join(anagram)

words = ['beetroot', 'carrots', 'potatoes']
anagrams = []

print([jumble(word) for word in words])


# note: sample 1,2 and 3 has the same result but different of code



filter
******
#-----sample1-----
# grades = ['A','B','F','C','F','A']

# def remove_fails(grade):
#    return grade != 'F'

# print(list(filter(remove_fails, grades)))

# output:  ['A', 'B', 'C', 'A']


#-----sample2-----
# grades = ['A','B','F','C','F','A']

# def remove_fails(grade):
#    return grade != 'F'

# filtered_grades = []
# for grade in grades:
#    if grade != 'F':
#         filtered_grades.append(grade)
# print(filtered_grades)

# output:  ['A', 'B', 'C', 'A']


#-----sample3-----
# comprehension code style

grades = ['A','B','F','C','F','A']

def remove_fails(grade):
     return grade != 'F'

print([grade for grade in grades if grades != 'F'])



lambdas - is like anonymous function no name function
*******
# lambas - is like anonymous function no name function

#-----sanple1-----
# nums = [1,2,3,4,5,6]

# normal function
# def square(n):
#    return n * n

# lambda function
# lambda n: n * n

# print(list(map(square, nums)))

# output:      [1, 4, 9, 16, 25, 36]


#-----sanple2-----
# comprehension lambda

nums = [1,2,3,4,5,6]

print(list(map(lambda n: n * n , nums)))

# output:      [1, 4, 9, 16, 25, 36]



# decorators - is a wrapper function
************

#-----sample1-----
# def cough_dec(func):

#    def func_wrapper():

          # code before the function
          # print('*cough*')
          # func()

          # code after the function
     #    print('*cough*')

     # return func_wrapper

# this is the decorators
# @cough_dec
# def question():
#    print('can you give me a discount on that?')

# question()

# output:      *cough*
#              can you give me a discount on that?
#              *cough*


#-----sample2-----
def cough_dec(func):

     def func_wrapper():

          # code before the function
          print('*cough*')
          func()

          # code after the function
          print('*cough*')

     return func_wrapper

# this is the decorators
@cough_dec
def question():
     print('can you give me a discount on that?')

@cough_dec
def answer():
     print("it's only 50p you cheapskate")

question()
answer()

# output: *cough*
#              can you give me a discount on that?
#              *cough*
#              *cough*
#              it's only 50p you cheapskate
#              *cough*



# reading and closing files
#**************************
# note: dont forget to open and close the file like

# sample:      ipsum_file = open('files/ipsum.txt')  # open file
#                   data goes here . . . . .
#              ipsum_file.close()  # close the file



#-----sample1-----
# ipsum_file = open('files/ipsum.txt')  #files(folder)/ipsum.txt

# for line in ipsum_file:
#    print(line)

# run in cmd:  python index.py


#-----sample2-----
# ipsum_file = open('files/ipsum.txt')  #files(folder)/ipsum.txt

# for line in ipsum_file:
#    print(line.rstrip())

# run in cmd:  python index.py


#-----sample3-----
# ipsum_file = open('files/ipsum.txt')  #files(folder)/ipsum.txt

# for line in ipsum_file:
#    print(line.rstrip())

# lines = ipsum_file.readlines()
# print(lines)

# run in cmd:  python index.py


#-----sample4-----
# ipsum_file = open('files/ipsum.txt')  #files(folder)/ipsum.txt

# for line in ipsum_file:
#    print(line.rstrip())

#    ipsum_file.seek(0)  #this will find the character you want to search

# lines = ipsum_file.readlines()
# print(lines)

# run in cmd:  python index.py


#-----sample5-----
# ipsum_file = open('files/ipsum.txt')  #files(folder)/ipsum.txt

# ipsum_file.seek(50)  # mag start siya sa ika 50 na letter or character
# file_text = ipsum_file.read(100)  # display 100 letter or character sugod sa 50
# print(file_text)

# ipsum_file.close()

# run in cmd:  python index.py

# note: dont forget to open and close the file like

# sample:      ipsum_file = open('files/ipsum.txt')  # open file
#                   data goes here . . . . .
#              ipsum_file.close()  # close the file


#-----sample6-----
# other way of reading or (open) and closing the file

# note: when data exist open the file and if not stay it close the file

def sequence_filter(line):
     return '>' not in line  #if data is not in the line or in the file

with open('files/dna_sequence.txt') as dna_file:
     lines = dna_file.readlines()
     print(list(filter(sequence_filter, lines)))



# writing files - write data of txt file
#**************

#-----sample1-----
# with open('files/write.txt', 'w') as write_file:
#    write_file.write('Hey there ninjas, python is awesome')
#    write_file.write('\nI love it so much, I dream in python')

# output:      write.txt
#              Hey there ninjas, python is awesome
#              I love it so much, I dream in python


#-----sample2-----
# with open('files/write.txt', 'w') as write_file:
#    write_file.write('Hey there ninjas, python is awesome')

# with open('files/write.txt', 'a') as write_file:
#    write_file.write('\nI love it so much, I dream in python')

# note: 'a' means amend para dili ma override ni first code si second code


#-----sample3-----
with open('files/write.txt', 'w') as write_file:
     write_file.write('Hey there ninjas, python is awesome')

with open('files/write.txt', 'a') as write_file:
     write_file.write('\nI love it so much, I dream in python')

qoutes = [
     '\nI can resist everything except temptation',
     '\nWe are all in the gutter, but some of us are looking as the stars',
     '\nAlways forgive your enemies - nothing annoys them so much'
]

with open('files/write.txt', 'a') as write_file:
     write_file.writelines(qoutes)  # writing more lines



# themed lorem ipsum generator - input number of paragraph and display to txt file
#*****************************

from random import randint

ninja_words = [
    'Aiki', 'Buyu', 'Chimonjutsu', 'Cho sen', 'Dojo', 'Gakusei', 'Haiboku',
    'Jin', 'Kenshi', 'Obake ken', 'Rakusha', 'Sanmaru', 'Tekkon', 'Yoko'
]

def ninjarize(word):
    random_pos = randint(0, len(ninja_words) - 1)  # - 1 para ang ninha_words kay 0-13 ra
    return f'{word} {ninja_words[random_pos]}'

paragraphs = int(input('How many paragraphs of ninja ipsum: '))  #01. enter number of paragraph

with open('ipsum.txt') as ipsum_original:  #02. open txt file to save inputed paragraph
    items = ipsum_original.read().split()

    for n in range(paragraphs):  #03. loop
        ninja_text = list( map(ninjarize, items) )
        with open('ninja_ipsum.txt', 'a') as ipsum_ninja:
            ipsum_ninja.write(' '.join(ninja_text) + '\n\n')



# downloading images - input number of paragraph and display to txt file
#*******************

import urllib.request

def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

url = input('Enter image URL to download: ')
file_name = input('Enter file name to save as: ')

dl_jpg(url, 'images/', file_name)

"""
