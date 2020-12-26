import sys
import utility
import random
#from utility import divide
import shopping.shopping_cart
from shopping.shopping_cart import buy

print(utility.divide(180, 20))
print(shopping.shopping_cart.buy('apple'))
print(buy('Banana'))

my_list= [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)
first = sys.argv[1]
last = sys.argv[2]

print(f'Hello {first} {last}')
