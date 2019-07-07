"""
error - mo matter and spacing in python code

note:     - everything in python is an object or function
          - there are two types of number in python integers and float
          - python start always in 0
          - inig human nimo og input adto mag start sa top ang pag read sa code
          - ang pag overrinde sa variable kay padulong sa ubos

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






16






"""
