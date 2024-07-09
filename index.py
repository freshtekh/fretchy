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
# def add(num1, num2):
#     return num1 + num2

# def subtract(num1, num2):
#     return num1 - num2

# def multiply(num1, num2):
#     return num1 * num2

# def divide(num1, num2):
#     return num1 / num2

# print ("please select function \n"
#        "1. Add\n"
#        "2. Subtract\n"
#        "3. Multiply\n"
#        "4. Divide\n")

# select = int(input("select operation form 1,2,3,4:"))

# number_1 = int(input("enter first number:"))
# number_2 = int(input("enter second number:"))

# if select == 1:
#     print (number_1, "+", number_2, "=",
#            add(number_1, number_2))
    
# elif select == 2:
#     print (number_1, "-", number_2, "=",
#            subtract(number_1, number_2))
    
# elif select == 3:
#     print (number_1, "*", number_2, "=",
#            multiply(number_1, number_2))

# elif select == 4:
#     print (number_1, "/", number_2, "=",
#            divide(number_1, number_2))

# else:
#     print("selection has to be from 1 to 4")
# user = int(input("number"))

# if user % 2 == 0:
#     print('even')

# else:
#     print("odd")    

# binary operators

# val1 = 3
# val2 = 4

# print (f'{val1}  {bin(val1)}')

# print (f'{val2} {bin(val2)}')
code = (input('input code: '))
if code := "*312#":
    print('''1.Data Plans
          2.Get 112.5GB + 40 mins for N16000
          3.Social Bundles
          4.Business plans
          5.Roaming/intl
          6.Borrow Credit/Recharge
          0.Next''')

menu = int(input('select option: '))

if menu == 1:
    print(''' 
          Buy data plans
          1.Daily
          2.Weekly
          3.Monthly
          4.2-3Month
          5.Always ON
          6.Broadband
          7.Family Packs
          8.Hot Deals
          9.Free Youtube
          10.Manage Data
          0.Back''')
    option = int(input('choose bundle: '))
    if option == 1:
        print('''
              1.N50 for 50MB
              2.N100 for 100MB
              3.N100 for 350MB (IG/TT/YT)
              4.N200 for 200MB
              5.N350 for 1GB
              6.N800 for 3GB
              7.N500 for 2GB
              8.N600 for 2.5GB
              99.Next
              0.Back''')
        data = int(input('choose subscription: '))
        if data == 1:
            print('''
You will be charged N50 for the purchase of 40MB
                  daily plan. To proceed, select:
                  1.Auto renew
                  2.One-off
                  3.Buy for a friend
                  4.Redeem Promo code
                  0.Back''')
        if data == 2:
                print('''
You will be charged N100 for the purchase of 40MB
                  daily plan. To proceed, select:
                  1.Auto renew
                  2.One-off
                  3.Buy for a friend
                  4.Redeem Promo code
                  0.Back''')
        else:
                print("you have entered an incorrect value")
    