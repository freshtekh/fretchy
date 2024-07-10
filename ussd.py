user = input('input code')
if user == "*312#":
    print('welcome to the ussd appliation')
    option = input('''
                   1.Data plans
                   2.Check balance
                   3.Exit
                   
                   choose option:-''')
    if option == '1':
        print('''1.Daily plans
                 2.weekly plans
              ''')
        plan= input('Choose plans: ')
        if plan == 1:
            print('Daily plan')
        elif plan==2:
            print('weekly plans')
        else:
            print('invalid option')