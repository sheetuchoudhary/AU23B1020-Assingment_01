'''
problem_4.2
'''
#importing the file name ice_cream
import ice_cream
s = input('scoop size (Small/Large)  :')
t= []
print('your fav ice-cream is here !!!')
print('ice cream with shake ')
#using the function name add_topping() and make_shake() from file ice_cream 
ice_cream.add_topping(s,t)
c= input('choose your shake (1.Nuts/2.Fruits):')
ice_cream.make_shake(c)



print('\nice cream without shake ')
#using only single function name make_shake of from file ice_cream
r=input('scoop size (Small/Large): ')
t=[]
ice_cream.add_topping(r,t)