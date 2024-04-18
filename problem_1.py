''' 
Problem_1
Program for problem_1 
'''
#helper function
def get_name():
    U_name = input("User Name :")
    return U_name



#main function
def get_tshirt(brand_name):
    #helper function call
    User_name = get_name()
    #list of brand names
    brands = ['Raymond','Puma','Adidas','Zara']
    #checking the brand is available in list of name brands
   
    for i in brands:
        if i==brand_name:
            print("Hi",User_name, "the brand you are looking for is available in our store ")
            break
    else:
        print("Hi",User_name, "Unfortunately the brand you are looking for is not available in our store ")
         
   
#  print("Hi",User_name, "the brand you are looking for is available in our store ")          
 
 #print("Hi",User_name, "Unfortunately the brand you are looking for is not available in our store ")
    
      
#taking brand name to be search 
b_name = input('Search for Brand : ')
#calling function name get_tshirt
get_tshirt(b_name)