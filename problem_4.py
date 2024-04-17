'''
Problem_4
Program for Problem_4
'''
def add_topping(scoop_size,toppings):
    
    for i in toppings :
        print(i)
scoop_size = input('1.Small\n.2.Medium\n3.Large\nscoop size :')
toppings = ['l','s','p']   
add_topping(scoop_size,toppings)