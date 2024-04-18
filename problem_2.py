'''
Problem_2
'''
#helper function
def get_name():
    U_name = input("User Name :")
    return U_name



#main function
def get_tshirt(brand_name,size = None):
    #helper function call
    User_name = get_name()
    #list of brand names
    brands = ['Raymond','Puma','Adidas','Zara']
    #list of size
    b_size = ['m','l','x','xl','xxl']
    for i in brands:
        #checking the brand is available in list of name brands
        if i == brand_name:
            #if user given to check for size_____if size =True
            if size: 
                for i in b_size:
                    #if  brand  and size both are available
                    if i == size :
                        print("Hi",User_name, "the ",size," size of ",brand_name," brand you are looking for is available in our store ")
                        break
                #if there is no search for size ____if size = False
                else:
                    print("Hi",User_name, "the ",brand_name," brand you are looking for is available in our store ")
            break
        else:
            if size:
                for i in b_size:
                    #size is true but not available of that size
                    if i!= size :
                        print("Hi",User_name, "Unfortunately the ",size," size of ",brand_name," brand you are looking for is not available in our store ")
                        break              
            #if no command for size
            else:     
                print("Hi",User_name, "Unfortunately the ",brand_name," brand you are looking for is not available in our store ")
                break

#taking brand name to be search 
b_name = input('Search for Brand : ')
b_size = input("Size (Optional) : " )
#calling function name get_tshirt
get_tshirt(b_name,b_size)