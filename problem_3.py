'''
Problem_3
program for problem_3
'''
#funtion for list of customer orders
def get_order(c_order):
    l_order=[]
    #to print the orders as per indexing 
    for i in c_order:
        l_order.append(i)
        print('Preparing Your Order - ',i)

    print('\nThe following orders have been dispatched:')

    #to reverse the order of customer orders list 
    
    l_order.reverse()
    #to print the element in it's original sequence one by one 
    for j in l_order[::-1]:
        print(j)
       
#pre difined list of customer order
c_orders = ['Dal_Chawal','Sahhi Paneer','Chutney','Tandoori Roti']
#calling the function
get_order(c_orders)
    



