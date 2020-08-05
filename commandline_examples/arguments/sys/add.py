import sys

try:
    # using map() to 
    # perform conversion 
    sum_list = list(map(int, sys.argv[1:])) 

    sum_out = sum(sum_list)
    print(sum_out)
    
except ValueError:
    print('Invalid input. Please try again with only numbers.')