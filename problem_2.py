'''
Problem_2
'''
#helper function
def get_name():
    U_name = input("User Name :")
    return U_name



#main function
def get_tshirt(brand_name,b_size=None):
    #helper function call
    User_name = get_name()
    #list of brand names
    b1='Raymond'
    b2='Puma'
    b3='Adidas'
    b4='Zara'
    brands = [b1 ,b2 ,b3,b4]
    if brand_name == b1.isupper or b1.islower:
        size = ['10','24','26','30']
        if size:
            for i in size:
                if i == b_size:
                    print("Hi",User_name, "the size of brand you are looking for is available in our store ")
            
            else:
                print("Hi",User_name, "the size of brand you are looking for is not available in our store ")
                
        else:
            print("Hi",User_name, "the brand you are looking for is available in our store ")

    elif brand_name == b2.isupper or b2.islower:
        size = ['20','26','30','36']
        if size :
            for i in size:
                if i == b_size:
                    print("Hi",User_name, "the size of brand you are looking for is available in our store ")
                  
            else:
                print("Hi",User_name, "the size of brand you are looking for is not available in our store ")
             
        else:
            print("Hi",User_name, "the brand you are looking for is available in our store ")

    elif brand_name == b3.isupper or b3.islower:
        size = ['26','34','36','40']
        if size:
            for i in size:
                if i == b_size:
                    print("Hi",User_name, "the size of brand you are looking for is available in our store ")
    
            else:
                print("Hi",User_name, "the size of brand you are looking for is not available in our store ")
               
        else:
            print("Hi",User_name, "the brand you are looking for is available in our store ")

    elif brand_name == b4.isupper or b4.islower:
        size = ['5','24','30','42'] 
        if size :   
            for i in size:
                if i == b_size:
                    print("Hi",User_name, "the size of brand you are looking for is available in our store ")
                
            else:
                print("Hi",User_name, "the size of brand you are looking for is not available in our store ")
             
        else:
            print("Hi",User_name, "the brand you are looking for is available in our store ")

    else:
        print("Hi",User_name, "Unfortunately the brand you are looking for is not available in our store ")
        
    
#taking brand name to be search 
b_name = input('Search for Brand : ')
b_size = input("Size (Optional) : " )
#calling function name get_tshirt
get_tshirt(b_name,b_size)