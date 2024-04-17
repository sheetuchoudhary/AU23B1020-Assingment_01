'''
problem_4.2
'''
import ice_cream
s = input('scoop size  :')
t= []
print('your fav ice-cream is here !!!')
print('ice cream with shake ')
ice_cream.add_topping(s,t)
c= input('choose your shake :')
ice_cream.make_shake(c)



print('ice cream without shake ')
r=input('scoop size : ')
t=[]
ice_cream.add_topping(r,t)