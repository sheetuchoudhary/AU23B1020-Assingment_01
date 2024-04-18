'''
Problem_4
Program for Problem_4
'''
#defining a function with two parameters
def add_topping(scoop_size,toppings): 

    print("select any three different items !!")
    print("1.Sprinkles\n2.Hot fudge\n3.Whipped cream\n4.Crushed nuts\nMake Your Choice !!") 
    n=1
    #to form user selection list for making ice_cream
    while (n<4):
        t= input('selected item : ')
        if t =='1':
            toppings.append('Sprinkles')   
        if t =='2':
            toppings.append('Hot fudge')
        if t =='3':
            toppings.append('Whipped Cream')
        if t =='4':
            toppings.append('Crushed Nuts')
        n+=1
    
    print("Nice Selection !!\nyour selection is here --")
    #the list of user choice for ice_cream is here!!!
    print('\nscoop size :',scoop_size)
    print('you choosed : ',toppings)

  


#defining a function with single parameter
def make_shake(choice):
    if choice=='1' or choice == 'nuts':
        print('your shake selection is of : Nuts')
    else :
        print('your shake selection is of : Fruits')


