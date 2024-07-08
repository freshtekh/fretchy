# x=5
# # y=6

# # print(x+y)



# print(""" My name is Fred
#      gooner
#      learning data analysis
# """)

# print('''
#     ghedhu
#       uyeyd
#       uiedqy

#   ''')

# names='Fred','Bimbo','Deji'i
# print(names)

# apple = potato =carrot = "#2000"
# print(apple)

# x,y,z=2, 4, 5
# print(x)
# print(y)
# print(z)

# concatenation

# firstName = 'Fred'
# lastName = 'Uche'
# occupation = 'Data analyst'
# id = 8



# print('my name is '+firstName+' '+lastName+' i am a '+occupation+'. my id is '+str(id))

# print(f"my name is {firstName} {lastName} i am a {occupation}. my id is {id} ")

# # # number types

# # number= 23+2j
# # print(type(number))

# # var=True
# # print(type(var))

# # items = ['Pepper','Tomato','Fish']
# # print(type(items))

# # items = ('Pepper','Tomato','Fish')
# # print(type(items))

# # var= list(range(1,11,2))
# # print(var)

# # var={'Pepper','Tomato','Fish'}

# student1= {'Id':1, "Name":"Fred", "Occupation":"Data analyst"}
# # print()
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print ("please select function \n"
       "1. Add\n"
       "2. Subtract\n"
       "3. Multiply\n"
       "4. Divide\n")

select = int(input("select operation form 1,2,3,4:"))

number_1 = int(input("enter first number:"))
number_2 = int(input("enter second number:"))

if select == 1:
    print (number_1, "+", number_2, "=",
           add(number_1, number_2))
    
elif select == 2:
    print (number_1, "-", number_2, "=",
           subtract(number_1, number_2))
    
elif select == 3:
    print (number_1, "*", number_2, "=",
           multiply(number_1, number_2))

elif select == 4:
    print (number_1, "/", number_2, "=",
           divde(number_1, number_2))

else:
    print("selection has to be from 1 to 4")