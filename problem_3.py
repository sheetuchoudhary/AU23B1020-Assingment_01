'''
Problem_3
program for problem_3
'''
def get_order(order):
    for i in order:
        print('Preparing Your Order - ',i)
    print('The following orders have been dispatched:')
    
    order.reverse()
    print(order)
c_orders = ['Dal_Chawal','Sahhi Paneer','Chutney','Tandoori Roti']
get_order(c_orders)
    



