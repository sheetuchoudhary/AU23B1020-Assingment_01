'''
Problem_4
Program for Problem_4
'''
def add_topping(scoop_size,toppings):
    your_icecream =[]
    if scoop_size =='2':
        size = 'Large'
    else :
        size = 'Small' 

    your_icecream.append(size)

    print("select any three different items !!")
    print("1.Sprinkles\n2.Hot fudge\n3.Whipped cream\n4.Crushed nuts\nyour choice :") 
    n=1
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
    print('scoop size : ',size)
    print(toppings)

  
scoop_size = input('1.small\n2.large\nscoop size :')
toppings =[]
add_topping(scoop_size,toppings)