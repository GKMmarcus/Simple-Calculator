def welcome():
    print('Simple Calculator')
    print('__________________________')
welcome()
while True:
    print('1.Add (+)\n2.Subtract (-)\n3.Multiply (*)\n4.Divide (/)\nType -1 to Quit')
    print('__________________________')
    user=int(input('Chose a Operation (1-4):'))
    print('__________________________')
    
    if user == 1:
        x = float(input('Enter your Number:'))
        print(x,'+ _ = _')
        y = float(input('Enter your Number:'))
        def add(x,y):
            return x+y
        print(x,'+',y,'=',add(x,y))
        user2 = int(input('Do you want continue?(Type 1 for yes / Type 2 for no):'))
        print('__________________________')
    elif user == 2:
        x = float(input('Enter a Number:'))
        print (x,'- _ = _')
        y = float(input('Enter a Number:'))
        def subtract(x,y):
            return x-y
        print (x,'-',y,'=',subtract(x,y))
        user2 = int(input('Do you want continue?(Type 1 for yes / Type 2 for no):'))
        print('__________________________')
    elif user == 3:
        x = float(input('Enter a Number:'))
        print (x,'* _ = _')
        y = float(input('Enter a Number:'))
        def multiply(x,y):
            return x*y
        print (x,'*',y,'=',multiply(x,y))
        user2 = int(input('Do you want continue?(Type 1 for yes / Type 2 for no):'))
        print('__________________________')
    elif user == 4:
        x = float(input('Enter a Number:'))
        print (x,'/ _ = _')
        y = float(input('Enter a Number:'))
        def divide(x,y):
            return x/y
        print (x,'/',y,'=',divide(x,y))
        user2 = int(input('Do you want continue?(Type 1 for yes / Type 2 for no):'))
        print('__________________________')
    elif user == -1:
        print ('Goodbye')
        break
    else:
        print('Not an Valid Operation')
        continue
    
    if user2 == 1:
        continue
    elif user2 == 2:
        print ('Goodbye')
        break
    else:
        print ('Not valid option')
        user2 = int(input('Do you want continue?(Type 1 for yes / Type 2 for no):'))















































