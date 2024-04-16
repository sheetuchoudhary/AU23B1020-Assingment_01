''' 
Problem_1
To Desgin a function with one parameter 
'''
def get_name():
    U_name = input("User Name :")
    return U_name



#main function
def get_tshirt(brand_name):
    #helper function
    User_name = get_name()
    #list of brand names
    brands = ['Raymond','Puma','Adidas','Zara']
    for i in brands:
        if i == brand_name.isupper or brand_name.islower:
            print("Hi",User_name, "the brand you are looking for is available in our store ")
            break
    else:
        print("Hi",User_name, "Unfortunately the brand you are looking for is not available in our store ")
brand_name = input('Search Or Brand : ')
get_tshirt(brand_name)

