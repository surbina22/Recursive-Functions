'''
Created on Nov 9, 2021

@author: cmotoyoshi22
'''

def main():
    
    a = input("please put in the first lower number")
    b = input("please put in the second higher number")
    a= int(a)
    b= int(b)
    print("sum of all of the numbers between the first and second number")
    print(sum_of_numbers_in_a_range(a, b))
    print("the product of the first and second number")
    print(product_of_2_whole_numbers(a, b))
    print("the sum of all of the numbers from 1 to the first lower number")
    print(summation_of_numbers (a))
    

def sum_of_numbers_in_a_range (a,b):
    if a==b:
        return (a)
    else:
        return(a+ sum_of_numbers_in_a_range(a+1,b))

 
def product_of_2_whole_numbers (a,b):

    if b==0:
        return (0)
    else:
        return (a+ product_of_2_whole_numbers(a, b-1)) 
    
def summation_of_numbers (n):
    if n == 0:
        return (0)
    else:
        return (summation_of_numbers(n-1)+n) 
    


if __name__ == '__main__':
    main()
    