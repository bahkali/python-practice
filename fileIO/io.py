#my_file = open('text.txt')
#print(my_file.readlines())

#open is a function to help working with file


#with open('text.txt') as my_file:
 #   print(my_file.readlines())


with open('text.txt', mode='r') as my_file:
    # text = my_file.write('@P')
    # print(text)
    print(my_file.read())

#read r ; write w append a

#using path 
with open('../fileIO/text.txt', mode='r') as my_file:
    print(my_file.read())

# can use the pathlib library for both mac and windows
#Don't forget to always wrap it to try catch
try:
    with open('text.txt', mode='r') as my_file:
        print(my_file.read())
except FileExistsError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise
