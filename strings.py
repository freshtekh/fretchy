name = 'FRESHTEKH is a programmer'
# print(len(name))
# print(name[5])
# print(name[0:5])

# function or method of a string
# print(name.lower())
# print(name.upper())
# print(name.capitalize())
# print(name.title())

# user = input('YES OR NO: ')
# print(user)
# if user.upper().strip() == 'YES':
#     print('YES')
# elif user.lower().strip() == 'no':
#     print('NO')
# else:
#     print('Invalid option')
# print (name.replace("programmer",'barber',1)) replace works with old, new and count
# print(name.index('programmer'))
# print(name.find('programmers'))
# print(name.startswith('F'))
# print(name.endswith('programmer'))
# email=input('Enter your email: ').strip()
# if '@' in email and '.' in email:
#     print('valid email')
# else:
#     print('invalid email')

# if email.find('@')!=-1 and email.find('.') != -1:
#     print('valid email')
# else:
#     print('invalid email')
# converting string to an array
# splitted=name.split()
# print(splitted)
# converting an array to a string
# print(' + '.join(splitted))
# essay = "Certainly! Here’s a concise 100-word essay on computers  Computers have become an integral part of our daily lives. From offices to homes, their usage has surged over the last decade. These electronic devices follow a three-step cycle: input, process, and output. They’ve revolutionized fields like medicine, research, and defense. In medicine, computers aid in diagnosis and finding cures. Research benefits from their ability to explore space and monitor the environment. For defense, computers help detect threats. Whether it’s a supercomputer or a mobile phone, these versatile machines continue to shape our world"
# splitted=essay.split()
# print(len(splitted))

# escape characters
\
# \n next line
# \t tab
# \r return
# \b delete spaces 
# \f
# \\ escapes paths thats has escape 

# path = r'C:\freshthon\index.py'

# print(path)

# r here means raw strings
# def is_palindrome(t):
#     return s == s[::-1]

# # Example usage:
# s = "boa"
# if is_palindrome(s):
#     print("Yes")
# else:
#     print("No")

# python collection
# 1. list
# 2. tuple
# 3. set
# 4. dictionary

# list: ordered, changeable/mutable, accept duplicate values, can be indexed

# e.g
# array = ['Fred','Abimbola','Tobi','deji', 'Fred']
# print(array)
# print(array[0]) indexing
# print(array [0:2]) slicing
# print(array[::-1]) reverse

# array[-1]=['Benz', 'G-wagon']
# print(array)
# print(array[-1][-1]) to get G-wagon

# method / function of list
# functions that adds to the array
# array.append('Yemi')
# array.extend('')
# array.insert(0, 'Benz') overtakes position

# functions that removes from the index
# array.pop(1) pops out 
# arr.remove()
# array.clear()

# print(array.count['Fred'])
# print(array.index['Fred'])
# print(array)

# other natural functions that can be used on  list
# print(len(array))
# scores = [2, 5, 6, 3]
# print(sum(scores))
# # mean of scores
# mean = sum(scores)/len(scores)
# print(mean)

# Python loop
# students = ['Fred', 'Abimbola','Tobi', 'Ade']

# for student in students:
#     # print(f'{student}, you are welcome to class')
#     if student== students[-1]:
#         print(f'{student}, he no need money')
#     else:
#         print(f'{student}, collect your money')

# all_students = []
# for i in range(5):

#     user = input(f'Enter student{1} name: ')
#     all_students.append(user)
#     print(all_students)

# all_students = []

# for i in range(slot):

#     user = input(f'Enter student{i+1} name: ')
#     all_students.append(user)
#     print(all_students)

students = []

# user = int(input('how many students are taking the test: '))

# for i in range(user):
#     name = input(f'Enter student{i+1} name: ')
#     students.append(name)

# print(students)
# for student in students:
#     print(f'{student}, you are welcome to take the test!')

#     score = 0
#     print('what is the capital of Nigeria a.) Abuja b.) Tokyo')
#     ans=input('Answer: ').strip().lower()
#     if ans == 'a':
#         print('Correct!')
#     else:
#         print('wrong')
#     score += 1

all_questions = ['what is the capital of Nigeria a.) Abuja b.) Tokyo',
                 'what is the capital of Japan a.) Abuja b.) Tokyo'

]

all_answers =['a', 'b']

# user = int(input('how many students are taking the test: '))
# for i in range(user):
#     name = input(f'Enter student{i+1} name: ')
#     students.append(name)

# print(students)
# for student in students:
#     print(f'{student}, you are welcome to take the test')
#     score = 0
#     x=1
#     for question, ans in zip(all_questions,all_answers):
#         print(f"\n{x}. {question}\n")
#         x+=1
#         user = input('Enter your answer: ').lower().strip()
#         if user == ans:
#          print('correct!')
#          score+=1
#         else:
#            print('wrong!')
#     print(f'{student}, your total score is {score}')


# list comprehension

# all_students = [input(f'name of student{i+1}: ') for i in range(int(input('no of students: ')))]
# print(all_students)


# 2.TUPLE

# myItems=('gold', 'dollars', 'diamond','Nigerian politician')
# print(type(myItems))
# print(len(myItems))
# print(myItems[:: -1])
# functions that wont work
# myItems[0] = 'Gold'
# print(myItems[::-1]) 

# functions and method

# print(myItems.index('diamond'))
# print(myItems.count('Nigerian politician'))

# unpacking

# a, b, c, d=myItems

# *_new, = myItems
# print(_new)
# _new=list(myItems)
# print(_new)
# _new[0]='gold'

# Assignment

# 1. record the scores of each students that took the test
# 2. print out the scoresheet

# print out student with the maximum score and student with minimum score
# print student with average
# create a todo

# myItems=tuple(_new)
# print(myItems)

# Sets
# 1. Unchangeable/ immuteable
# 2. Cannot be indexed
# 3. Does not accept duplicate value
# 4. It is unordered

# cars = {'Benz', 'Toyota', 'Audi', 'Tesla', 'BYD',"Lexus"}
# colors = {'red', 'green', 'yellow'}
# print(cars[0]) wont work
# print(len(cars)) will work

# cars.add("Nissan")
# cars.update(colors) equivalent of extend in list
# cars.remove('Benz')
# cars.discard('benz')
# cars.pop()
# print(cars)

setA= {1,3,4,5,7,8,9,10}
setB= {2,1,3,6,10}

# setC= setA.union(setB)
# setA.intersection(setB)
# print(setA.intersection_update(setB))
# print(setA.isdisjoint(setB))
# print(setA.issubset(setB))
# print(setA.issuperset(setB))
# print(setC)

import random as rd
# num = rd.randint(8130000000, 8139999999)
# print(num)
while True:
    cars = ['Benz', 'Toyota', 'Audi', 'Tesla', 'BYD',"Lexus"]
    my_choice= rd.choice(cars)
    myGuess=input('')

    print(my_choice)

    if myGuess==my_choice:
        print('bingo')

# x=10
# while x>=0:
#     print(f'welcome {x}')
#     x-=1

# read up on while loop

# guess app using while loop
# create a dummy balance
# have a stake account
# as long as balance is greater than stake keep staking

