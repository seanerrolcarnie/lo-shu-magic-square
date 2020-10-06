#Sean Carnie (CASEC171). Assignment submission for CSP1150D. 01/01/2019
#-----------------------------------------------------------------------------



#This program is used to allow a user to enter a square consisting of 9 numbers.
#The program determines whether the square is either a regular square, a magic
#square, or a lo shu magic square.


#A simple magic square is where all the numbers in the square add to the same
#value across the rows, columns and diagonal.

#A Lo Shu magic square is a magic square that uses only the digits 1 to 9,
#without repeating a digit.


#The program is formatted for compact view,  contains many functions all built
#around allowing a user to input their own square, and determining what type of
#square out of the 3 mentioned was input by the user.





#MAIN FUNCTION
#===============================================================================
def main():
#This is the main function.
    
    #Simple while loop used if usser desires to re-enter square.   
    again = 'y' 
    while again == 'y':
        
        #The user inputs the square here.       
        user_square = get_user_input()

      
#----------------------------------------------------------------------------
        #All the highlighted variables below are needed in order to carry
        #out the ifstatement below in order to determine if the square is lo shu,
        #and so their respective functions are called in order to do this.
        
        number_of_rows, number_of_columns = get_rows_and_columns()

        number_of_rows_or_columns = number_of_columns

        first_row_sum = get_first_row_sum(user_square, number_of_columns)
#----------------------------------------------------------------------------

        #This function solely decides whether the user input square is a
        #magic square.
        check_magic_square(user_square)
        
        #Three functions are used together with multiple AND statements to
        #allow the program to validate all the features a lo shu square
        #must contain.
        if check_lo_shu_magic_square(user_square, first_row_sum, \
                               number_of_rows, number_of_columns,\
                               number_of_rows_or_columns) and \
                               repeat_test(user_square) and \
                               range_test(user_square):
            
            print("\nIs Lo Shu Square: True")
        else:
            print("\nIs Lo Shu Square: False")
            
        print('\nDo you want to enter a new square?')
        again = input('\ny = yes, anything else = no: ')

#===============================================================================
        









#ESSENTIAL FUNCTIONS: SQUARE SIZE AND USER INPUT
#===============================================================================   

def get_rows_and_columns():
    #Since the square is static in size, variables were set as such:

    #'number_of_rows_or_columns' variable was created purely to make
    #the code makes more sense when reading later on.
    number_of_rows_or_columns = 3
    number_of_rows = 3
    number_of_columns = 3

    return number_of_rows, number_of_columns



  
def get_user_input():

    #Two-dimentional list was used to gather user input to create square.
    
    number_of_rows_or_columns = 3
    number_of_rows = 3
    number_of_columns = 3
    count = 0

    user_square =  [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]

    for rows in range(number_of_rows):
        for columns in range(number_of_columns):

    #Count converted to string in order to display user input on same line.
            user_square[rows][columns] = int(input('\nEnter number ' +\
                                              str(count + 1) + ': '))
            count += 1
            
    print()
    #Asterix used to remove brackets in output display.   
    print(*(user_square[0]))
    print(*(user_square[1]))
    print(*(user_square[2]))
        
 
    #The two - dimentional list elements are taken directly from this function
    #for other functions to use.
    
    return user_square
#===============================================================================








#FUNCTIONS TO GATHER SQUARE ROW, COLUMN, AND DIAGONAL SUM VALUES.     
#===============================================================================


def get_first_row_sum(user_square, number_of_columns):
    
#This function is used as a starting point in which other functions
#will compare values with. Since if a the sum of any row, column or
#diagonal does not match with the first row sum the square is not
#lo shu, or magic.

    
    
    first_row_sum = 0

    #The iteration works to scan each element in the first row of the square.
    #Since the current_row_index is 0 and iterates once(1), the row being
    #scanned will remain the first one. The current_column_index, however
    #iterates 3 times (number of columns), raising the current_column_index
    #each time and scanning all 3 elements on the first row, and adding them
    #to the first_row_sum variable in this manner.

    #This is essentially how the rest of the sum checking functions work >
    
    for current_row_index in range(1):
        for current_column_index in range(number_of_columns):
            first_row_sum = first_row_sum + user_square[current_row_index]\
                            [current_column_index]
            
    return first_row_sum






def check_equal_row_sums(user_square, first_row_sum, number_of_rows,\
                         number_of_columns):
    
#The rest of the row sums are scanned and compared to the first row sum.
    
#Unlike get_first_row_sum( above ) all other functions in this section
#will output a true or false value which is returned for a later function.
    
    row_sum = 0

    for current_row_index in range(number_of_rows):
        for current_column_index in range(number_of_columns):
            row_sum = row_sum + user_square[current_row_index]\
                      [current_column_index]

            
        if row_sum != first_row_sum:
            return False
        
        #Row sum set to 0 as the function continues to add elements
        #and function becomes inaccurate.
        
        row_sum = 0    

    return True





def check_equal_column_sums(user_square, first_row_sum,\
                            number_of_rows, number_of_columns):
    
#All column elements are scanned, summed and compared
#to the first row sum.
    
    column_sum = 0
    
    for current_column_index in range(number_of_columns):
        for current_row_index in range(number_of_rows):
            column_sum = column_sum + user_square[current_row_index]\
                         [current_column_index]

            
        if column_sum != first_row_sum:
            return False
        
        #Column sum set to 0 for the same reason found
        #in the function above for row_sum.
        
        column_sum = 0
        
    return True




def check_equal_row_and_column_sums(user_square, first_row_sum,\
                                    number_of_rows, number_of_columns):

#The sums of both all rows and all columns are compared to each other
#and True is returned if they both return true in their own functions
#respectively.
    
    if check_equal_row_sums(user_square, first_row_sum,\
                            number_of_rows, number_of_columns) and\
       check_equal_column_sums(user_square, first_row_sum,\
                            number_of_rows, number_of_columns):
        return True
    else:
        return False




    
#Both left and right diagonals of the square undergo the same process as the above functions.
       
def check_equal_diagonal__sums_left(user_square, number_of_rows_or_columns,\
                                    first_row_sum):

    left_diagonal_sum = 0
    
    for current_diagonal_index in range(number_of_rows_or_columns):
        left_diagonal_sum = left_diagonal_sum + user_square\
                            [current_diagonal_index][current_diagonal_index]
        
    if left_diagonal_sum != first_row_sum:
        return False
    else:
        return True
                               

   
       
def check_equal_diagonal__sums_right(user_square, number_of_rows_or_columns,\
                                     first_row_sum):
    
    right_diagonal_sum = 0
    current_diagonal_column_index = number_of_rows_or_columns - 1

    for current_diagonal_row_index in range(number_of_rows_or_columns):
        right_diagonal_sum = right_diagonal_sum + user_square\
                             [current_diagonal_row_index]\
                             [current_diagonal_column_index]
        current_diagonal_column_index = current_diagonal_column_index - 1
        
    if right_diagonal_sum != first_row_sum:
        return False
    else:
        return True
    

        
        
def check_equal_diagonal_sums_left_and_right(user_square,\
                                number_of_rows_or_columns,\
                                            first_row_sum):
    
#Compares left and right diagonal sums and if both return true so does this function.    
    
    if check_equal_diagonal__sums_left(user_square, \
                                  number_of_rows_or_columns,\
                                  first_row_sum) and\
                                  check_equal_diagonal__sums_right\
                                  (user_square,\
                                  number_of_rows_or_columns,\
                                  first_row_sum):
        return True
    else:
        return False

#===============================================================================










#FINAL SQUARE TEST FUNCTIONS
#===============================================================================
def check_magic_square(user_square):
    
#Same code reused from main() minus repeated digits test and range(1-9)test.   

    number_of_rows, number_of_columns = get_rows_and_columns()

    number_of_rows_or_columns = number_of_columns

    first_row_sum = get_first_row_sum(user_square, number_of_columns)

    if check_lo_shu_magic_square(user_square, first_row_sum, \
                           number_of_rows, number_of_columns,\
                           number_of_rows_or_columns):


        print("\nMagic Square: True")
    else:
        print("\nIs Magic Square: False")
        
            



    
def check_lo_shu_magic_square(user_square, first_row_sum, number_of_rows,\
                           number_of_columns, number_of_rows_or_columns ):

#This function confirms that all rows, columns, and all diagonals add up to the
#same value. If all of the above functions in this section return True then
#this function does as well and confirms to the main() function that the square
#entered is a lo shu square.   
    
    if check_equal_row_and_column_sums(user_square,\
                   first_row_sum, number_of_rows, number_of_columns) and \
                   check_equal_diagonal_sums_left_and_right(user_square, \
                   number_of_rows_or_columns, first_row_sum):
        return True
    else:
        return False
    
#===============================================================================    



    







#LO SHU SQUARE VALIDATION TESTS
#===============================================================================    
def repeat_test(user_square):
    
    #This function serves the purpose of validating whether values in the user
    #inputted square are repeated or not, to determine whether the square is 
    #lo shu



    
    #Had to convert two dimentional list into one dimentional list in order for
    #repeating values function 'repeat_test()' to work correctly.
    
    user_square_v2 = [x for y in  user_square for x in y]

    #Simple set created as it cannot contain duplicate elements and is
    #easy to compare to main list using for loop and count to identify
    #repeated elements.
    unique = set(user_square_v2)  
    for each in unique:  
        count = user_square_v2.count(each)  
        if count > 1:  
            return False  
    return True  


def range_test(user_square):
    
    #Mostly reused code from above function, however the code is altered so\
    #the function serves the purpose of validating whether values in two\
    #dimentional list are in range 1 - 9 for Lo Shu square test.
    
    user_square_v2 = [x for y in  user_square for x in y]

    
    in_range = set(user_square_v2)  
    for each in in_range:   
        if each > 9:  
            return False  
    return True  
#===============================================================================

    
main()        

 




      
    

    
