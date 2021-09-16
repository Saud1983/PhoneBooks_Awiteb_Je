def input_type(value):
    try:
        int(value)
        return "integer"
    except ValueError:
        try:
            float(value)
            return "double"
        except ValueError:
            return "string"



value = "21"
print(f"{value} is {input_type(value)}")

# ------------------------------------------------------------------

# using dictionaries
def most_frequent_element(arr):
    dic = {} # A dictionary for all the list elemnts as a key and elemnt count as a value
    reverse_dic = {} # A reverse dictionary that uses values in original dic as keys and keys as values
    result = {} # A dictionary that has only one key/value pair after it has been built
    for i in arr: # Iterate throw the list
        dic[f"{i}"] = arr.count(i) # Add new elemnt as a key and elemnt count as a value each round

    count_max = str(max(dic.values())) # find the maximum element count from the dictionary values and convert it to string

    for key, value in dic.items(): # Iterate throw the dic dictionary
        reverse_dic[f"{value}"] = int(key) # Swap between the keys and values of the original dictionary

    for key,value in reverse_dic.items(): # Iterate throw the reversed dictionary
        if key == count_max: # To find the maximum value of all
            result[key]=value # Add that key/vaule pair to a new dictionary that will have only one pair

    list1 = list(result.values()) # Get only the values from the result dictionary and convert it to a list type
    return list1[0] # Unpack the list element witch only one elemnt in that list

x = most_frequent_element([2,3,4,1,5,-5,-5,-5,-5,-5,6])
print(x)


# looping in a list
def most_frequent(List):
    frequent_num = List[0] # Select the 1st element of the list
    count = 0 # Inital value of a counter
    for i in List: # Iterate throw a list
        current_count = List.count(i) # Use the count Function to find how many times that i element appears then give that number to a varible
        if (current_count > count): # Compair which has a bigger number to make sure that no smaller count value can pass this point
            count = current_count # Replace the counter value with a bigger value
            frequent_num = i # give the element which has the biggest number so far to a new varible to be used at the end of iteration
    return str(frequent_num) # convert that element to a string and return it


List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))

# ------------------------------------------------------------------
# Sort from minimum to maximum
def sort_array(array):
    list1 = []
    while array: # 1st loop that shrenks in every loop
        current_item = array[0] # To always select the 1st elemnt of the array after the previous 1st element has been removed
        for i in array: # To iterate throw array selecting all elemnts one by one
            if i < current_item: # compair the new selected element with the first elemnet of the array
                current_item = i # Update the cerrent_item with the smaller value when the condition is True
        list1.append(current_item) # Append the next smallest value to another list that will build up more and more until the while loop has stopped
        array.remove(current_item) # Remove the same smalledt value from the original list that shrenks more and more until it has no elements and that but an end to while loop
    return list1 # return the sorted list that starts elements from the smallest to biggest

# Sort from maimum to minimum just chane the "less than" operator < to "greater than" operator in if statement


# Or using conditional to use the sort both ways
def sort_array(array, type):
    list1 = []
    while array: # 1st loop that shrenks in every loop
        current_item = array[0] # To always select the 1st elemnt of the array after the previous 1st element has been removed
        for i in array: # To iterate throw array selecting all elemnts one by one
            if type == "S":
                if i < current_item: # compair the new selected element with the first elemnet of the array
                    current_item = i # Update the cerrent_item with the smaller value when the condition is True
            elif type == "B":
                if i > current_item: # compair the new selected element with the first elemnet of the array
                    current_item = i
        list1.append(current_item) # Append the next smallest value to another list that will build up more and more until the while loop has stopped
        array.remove(current_item) # Remove the same smalledt value from the original list that shrenks more and more until it has no elements and that but an end to while loop
    return list1 # return the sorted list that starts elements from the smallest to biggest

print(sort_array([99 , 314 , 8 , 200 , 23],"S"))

# ------------------------------------------------------------------

def factorial(number):
  list1 = [] # New list to add all the factorial numbers
  result=1 # Inital Value to be used at the end with value 1 that doesn't affect the multiplication

  for i in range(number): # Iterate Throw a range with length of a givin number
      list1.append(i+1) # Append all number to the list after adding 1 because the range starts from 0

  for n in list1: # Iterate throw the new list to get one element at a time
      result = result * n # make the math with new element, remember that the result has a value of 1 in the first round
  return result # return the result

# ------------------------------------------------------------------
# Prime numbers

"""
Note that you can squreroot a givin number ex(100) then divide that givin
number by only those prime numbers less than the result of squareroot of that
givin number 100**0.5 = 10 -> (2, 3, 5, 7) if that givin number (100) not
divisable by any number of those prime numbers (2, 3, 5, 7) then the givin
number is a prime without havig to divide it by all number less than that givin
number

"""
def primes_nums(array):
    primes_list = [] # A list that will contain all the prime numbers
    for i in array: # Iterate throw the original list
        pr = True # Set Inital value to be used later

        # need to make sure is it enough t use i or we have add +1
        for x in range(2, i+1): # Loop throw a range from 2 to that element value in the original list
        # for x in range(2, i**0.5): # It's better to use the squareroot to reduse the numbers that givin number Should be devided by.
            if i % x == 0: # This conditional tests the element throw out the whole range.
                pr = False # It's enough to find one number that has False becase 1 and the number it self are not included in the range.
        if pr == True : # This only allow prime numbers to go inside
            primes_list.append(i) # Building up the new list with prime numbers
    return primes_list # return the list that contains prime numbers

# One line ways
def prime_num_one_line(array):
    return [ i for i in array if all ( i%j != 0 for j in range(2,int(i**0.5) + 1))]

array = [i for i in range(100)]
print(array)

print(prime_num_one_line(array))

# ------------------------------------------------------------------
# To return a sequence numbers from 0 to that number as string
def numbers_range(number):
    asstring = "0"
    for i in range(1,number+1):
            asstring = asstring + " " + str(i)
    return asstring

# ------------------------------------------------------------------
# Date reformat

def date_format(date):
    whole = date.split("/")  # Split a string to multi elements in a list based on "/"
    hy, sl, cl = "-", "/", ' | '  # Initial symbols to use in formatting
    for i in range(1):  # Only one time iteration that needed
        str_hy = whole[i] + hy + whole[i+1] + hy + whole[i+2]  # Formatting YYYY-M(M)-D(D) with hyphen, (M),(D) optional
        str_sl = whole[i+1] + sl + whole[i+2] + sl + whole[i-i]  # Formatting M(M)-D(D)-YYYY with hyphen, (M),(D) optional
        return date + cl + str_hy + cl + str_sl  # Final Format 2019/2/14 | 2019-2-14 | 2/14/2019

print(f"{date_format('2019/2/14')}")
# ------------------------------------------------------------------
# Count Down
# Wrong way
def countDownX(number):
    strs = ""
    for _ in range(number+1):
        strs += str(_) + " "
    strs1 = strs[::-1]
    return strs1[1::]

print(countDownX(15))

#output
# Should be 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
# the result 51 41 31 21 11 01 9 8 7 6 5 4 3 2 1 0

# correct way
def countDown1(number):
    strs = ""
    for _ in range(number+1)[::-1]: # to start the range backwards
#   for i in range(number,-1,-1) start from number upto but not included -1, and -1 for going backwards
        strs += str(_) + " "
    return strs.strip() # strip() is to Remove spaces at the beginning and at the end of the string

print(countDown1(15))

# result without strip() "15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 "
# result with    strip() "15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0"

# Another correct ways
def countDown2(number):
    strs = []
    for _ in range(number,-1,-1):
        strs.append(str(_))
    return " ".join(strs) # join reads all string elemnts incide a list and joint them together with what ever inside " ".join(list), but If the elemen are not string type then the for loop is a must to use "".join

print(countDown2(15))

def countDown3(number):
    return " ".join(str(i) for i in range(number,-1,-1))

# ------------------------------------------------------------------
# Sum Even numbers
def sum_even(arr):
    total = 0 # initial value for some to be used later
    for i in arr: # Iterate throw the list
        if i % 2 == 0: # If the selected element divisable by 2 then it's even number
            total = total + i # Add this number to the total
    return total    # return the total of sum

# ------------------------------------------------------------------

def reverse_words(str1, str2):
    return str2 +", "+ str1

print((reverse_words("Weekend","fianlly")))

"fianlly, Weekend"
"finally, Weekend"

# ------------------------------------------------------------------

def match_arrays(array1, array2):
    if len(array1) == len(array2): # Check to make sure that the second array is not bigger than the 1st array
        for i in array1: # Loop throw the list and select an element
            if i in array2: # Find out if that element is in the 2nd array
                continue # Continue looping selecting another elements without doing anything
            else: # If the selected element is not in the second array
                return False # Stop the process and return False
        return True # return True after all elements passed the test
    return False # return False when the count of the first array does not match the count of the other array

print(match_arrays(["word1", "wo", "word2"],["word2", "word1", "wo"]))

# ------------------------------------------------------------------

def number_sum(num):
    total = 0
    for i in range(num+1):
        total = total + i
    return total

print(number_sum(7))

# ------------------------------------------------------------------

def elements_math(lis: list) -> int:  # The expected passed value is a list and the expected return is an integer
    u = 0  # Initial value for the sum of all 1st elemnets
    d = 0  # Initial value for the sum of all 2nd elemnets
    for i, o in lis:  # Iterate throw the list selecting the elements inside the 1st list element
        u += i  # adding the list[0][i]
        d += o  # adding the list[0][o]
    return u - d

print(elements_math([[10,0],[3,5],[5,8]]))

# ------------------------------------------------------------------

def swap_cases(value):
    new_str = ""
    for i in value:
        # if i.isalpha():  # Use if you want to only accept alphabet chars
        new_str += i.swapcase() # Use this line or hashtag it and use the code underneath
        # Or
        #     if i == i.lower():
        #         new_str += i.upper()
        #     else:
        #         new_str += i.lower()
    return new_str

print(Swap_cases("AbCdEfG1@s"))

# ------------------------------------------------------------------

# The idea is to check the selected element, if it's in the new_lis pass otherwise adding it
def remove_duplicate(arr):
  new_lis = []
  for i in arr:
    if i not in new_lis:
      new_lis.append(i)
  return new_lis

print(remove_duplicate([1,2,3,3]))

# ------------------------------------------------------------------
# The idea is to check the selected element, if it's in the unique_elem list then it's duplicateed

def get_duplicate_elements(arr):
    unique_elem = []
    dupl_elem = []

    for i in arr:
        if i not in unique_elem:  # Add the selected element to unique_elem so it can be tested again for duplicated values
            unique_elem.append(i)
        elif i in unique_elem and i not in dupl_elem:  # To make sure that the selected element has faild in the first conditional but not yet added in the second one
            dupl_elem.append(i)
    return dupl_elem

print(get_duplicate_elements([10,3,10,3,3]))

# ------------------------------------------------------------------

def logical_and(a, b):
    if a and b:
        return True
    else:
        return False


print(logical_and(False,False))

# ------------------------------------------------------------------

# Clear the list if it's contains a null values
def clean_array(arr):
    new_lis = []
    for i in arr:
        if i is not None:  # Here is how to find a null value
            new_lis.append(i)
    return new_lis

print(clean_array([None,None,3]))

# ------------------------------------------------------------------

def stringCheck(value):
    for i in value:
        for x in value:
            if i != x:
                return False  # It's enough to find one element not matched to stop the code
            else:
                continue
    return True

print(stringCheck([ "&&", "&&&", "&&", "&&"]))
print(stringCheck([ "a", "A", "a"]))

# ------------------------------------------------------------------

def convertPercent(percentage):
    p = percentage.split("%")
    return float(p[0]) / 100

print(convertPercent("288%"))

# ------------------------------------------------------------------

def search(word, character):
    for index, char in enumerate(word):
        # If char.lower() == character.lower(): # In case that the character has been givin in different lettercase
        if char == character:
            return index
    return -1

print(search("python","n"))

# ------------------------------------------------------------------

# Cone Volume
def cone_volume(radius, height):
    return (1/3)*3.142*float(radius)**2*float(height)

print(cone_volume(2.0,4.0))

# ------------------------------------------------------------------
def hashtag_it(array):
    stri=""
    for i in array:
        stri += "#"+i+" "
    return stri.strip()  # Strip() is used to remove the prefix and suffix spaces
print(hashtag_it(["SAFCSP", "entrepreneur"]))

# Result "#SAFCSP #entrepreneur"

# ------------------------------------------------------------------
def filp_even_odd(array):
    result = []
    for i in array:
      if i % 2 == 0:
        i += 1
        result.append(i)
      else:
        i -= 1
        result.append(i)
    return result

print(filp_even_odd([24, 13, 14, 18]))

# ------------------------------------------------------------------

def countWords(txt):
    lis = txt.split(" ")
    return len(lis)


print(f"{countWords('Good Morning')}")

# ------------------------------------------------------------------
# To find the match for the last two characters from both words
def compare_two_words(s1, s2):
    s1_len, s2_len = len(s1), len(s2) # To use the length for having a correct indexing

    s11 = s1[s1_len-2:] # The last to characters
    s22 = s2[s2_len-2:] # The last to characters
    if s11 == s22:
        print(f"s1 = {s11} s2 = {s22}")
        return True
    else:
        print(f"s1 = {s11} s2 = {s22}")
        return False

print(f"{compare_two_words('persona' ,'person')}")

# ------------------------------------------------------------------
# Replace the word 'the' with a correct a or an based on the next word

def replaceThe(txt):
    lis = txt.split()
    str1 = ""
    for index, value in enumerate(lis):
        if value == 'the':
            if lis[index+1][0] in "aeoiu":
                lis[index] = 'an'
            else:
                lis[index] = 'a'
    for i in lis:
        str1 += i+" "
    return str1.strip()

print(f"{replaceThe('Get the idea')}")

# ------------------------------------------------------------------
# Get the first character that can be converted as integer

def left_digit(str):
    for i in str:
        try:
            num = int(i)
            break
        except ValueError:
            continue
    return num


print(f"{left_digit('I want 2 be programmer 2030')}")

# ------------------------------------------------------------------

def missingLetter(txt):
    str1 = 'abcdefghijklmnopqrstuvwxyz'
    txt_len = len(txt)
    for index, value in enumerate(str1):
        if value == txt[0]:
            str1 = str1[index:(index+txt_len)]
            counter = 0
            for i in str1:
                if i == txt[counter]:
                    counter +=1
                else:
                    return i
    return "No Missing Letter"

print(f"{missingLetter('klnop')}")

# ------------------------------------------------------------------
# To return the longest string of zeros or return " " if there is no zeros
def longestZero(str):
    str1 = ""
    result = ""
    counter = 0
    if "0" in str: # To make sure that there is a zero in str before doing anything else
        for i in str: # Loop throw the str
            if i == "0": # Start using the code underneath when found any 0
                str1 = str1 + i
                counter += 1
            else:
                if counter > len(result):
                    result = str1
                    str1 = ""
                    counter = 0

    else:
        result = '" "'

    return result

print(f"{longestZero('000110000011001110101')}")

# ------------------------------------------------------------------
# To sum each elemnt with all previous elements in array
def cumulative_sum(arr):
    lis1=[]
    for i,v in enumerate(arr):
        if i > 0:
            m = sum(arr[:i]) + v
            lis1.append(m)
        else:
            lis1.append(v)
    return lis1

print(f"{cumulative_sum([5,-5])}")


# ------------------------------------------------------------------
# It works well in Pycharm but didn't pass the challenge
def removeSpecialCharacters(str):
    str1 = '.-_ '
    str2 = ""
    for i in str:
        if i.isalnum() or i in str1:
            str2 = str2 + i
        else:
            str2 = str2.strip()
    return str2

print(f"{removeSpecialCharacters('He good @ tennis!')}")

# ------------------------------------------------------------------
# Replace space ' ' with '#'
def hasSpace(str):
    str1=""
    for i in str:
        if i != " ":
            str1 = str1 + i
        else:
            str1 = str1 + "#"
    return str1

print(f"{hasSpace('I love challenges')}")

# ------------------------------------------------------------------
# counts characters in each elemnt
def word_length(arr):
    lis1 = []
    for i in arr:
        lis1.append(len(i))
    return lis1

print(f"{word_length(['wait' ,'Go' , 'run'])}")

# ------------------------------------------------------------------
# return one list with all elemnts from both lists that are sorted
def merge_sort(node1, node2):
    for i in node2:
        node1.append(i)
    node1.sort()
    return node1

print(f"{merge_sort([20,10],[-11,10])}")

# ------------------------------------------------------------------
# return only the unique values
def unique(arr):
    lis1 = []
    dup_lis =[]
    for index, value in enumerate(arr):
        if value in arr[index+1:]:
            dup_lis.append(value)
        elif value not in dup_lis:
            lis1.append(value)
    return lis1

print(f"{unique([ 4 ,3 ,-5 ,4 ])}")

# ------------------------------------------------------------------
# return a sting that has been sorted by length of words from smallest to largest
def sortByLength(txt):
    lis = txt.split()  # Split the sting into a multi elements list
    max= 0  # Initial value of the maximum word length that will be used later
    for l in lis:  # Loop throw the list to find the element that has maximum lenth
        if len(l) > max:
            max = len(l)

    lis_sort='' # Initial value of a string that would be returned from the function
    for i in range(0,max+1):  # Loop throw a range starts from 0 to the number that represent the largest word length that has been found eralier +1
        for x in lis:  # loop throw the same list again testing each elemnt to find all words with a length that matches the upper selected value, starts from length 0 then 1 then 2 .. until the maximum length that has been found before
            if len(x) == i:  # Select each element from the list and check its length compared with the selected number of the range that represent the length that need to be found in the list elements
                lis_sort = lis_sort + " " + x
    return lis_sort.strip()


print(f"{sortByLength('Have a nice day')}")

# ------------------------------------------------------------------
#
def add_five(arr):
    if len(arr) > 0:
        for index, value in enumerate(arr):
            value = value + "5"
            arr[index] = value
    else:
        return arr
    return arr

print(f"{add_five([ 'hi', 'G', 'welcome' ])}")
# output = ['hi5', 'G5', 'welcome5']

# ------------------------------------------------------------------
# This function is to make sure the passed in string can be a math operation or not
def math_expr(expr):
    operators = ['+', '-', '*', '/', '//', '**', '%','(',')','.']
    str1=""
    for v in expr:
        if v not in operators:
            str1 = str1 + v
    # print(str1)
    try:
        int(str1)
        return True
    except ValueError:
        return False

print(f"{math_expr('7.12*(14/2)+4**2.1')}")

# ------------------------------------------------------------------
# Do the math if possible or return -1 as str
def addStrNums(num1, num2):
    try:
        n1, n2 =int(num1), int(num2)
        return str(n1 + n2)
    except ValueError:
        return str(-1)

print(f"{addStrNums('2a','3')}")

# ------------------------------------------------------------------
# Is to convert from octal to dicemal, from decimal to binary.
# Note: this function accepted 8 and 9 that they are not allowed because no octal number has 8 or 9 value in it

def oct_to_bin(octal):
    result = 0
    length_of_digits = len(str(octal))  # To determine how many digits in the octal number
    octal_str = str(octal)  # To use indexing property after converting the octal from integer type to string type
    for exponent in range(0,length_of_digits):  # Iterate to get exponent series from zero up to the length of that octal number - 1
        digit = int(octal_str[length_of_digits-1])  # To select and convert one digit in each loop
        result = result + (8 ** exponent) * digit  # Use mathematical formula
        length_of_digits -= 1  # Change the indexing to select another digit in the next loop
    decimal = result

    str1 = ""  # This variable to add zeros and ones to it
    digit_count = len(str(decimal))  # this varibale is to count how many digits in the passed in num
    category = int(
        "9" * digit_count)  # This variable is to get the maximum number that has the same number of digits, it should be 9 or 99 or 999 or 9999 etc.
    for x in range(digit_count * 3 + 1, -1,
                   -1):  # This is reversed range stops in zero, and digit_count*3+1 formula is to give the power that base 2 needed to reach the maximum number less than category or at least only one exponent that  exceeds category so the loop will not use useless powers for the base 2 and save memory and time
        if 2 ** x > category + 1:  # using the above formula digit_count*3+1 will make this line False all the time or at least True one time only
            pass
        else:
            if 2 ** x <= decimal:  # by using this, the function starts build the string str1 with ones and zeros and removing substracting the 2**x from the giving num
                str1 = str1 + "1"
                decimal = decimal - 2 ** x
            # If you want to see the actual binary number, uncomment the code below and comment the last line
            else:
                str1 = str1 + "0"

    return str(int(str1))

print(oct_to_bin(776215676))


# ------------------------------------------------------------------
# Is to return a string of vowels that has less than or equal the value n
def first_n_vowels(phrase, n):
    vowels = 'aeiou'
    str1 = ""
    for i in phrase:
        if i.lower() in vowels:
            str1 = str1 + i

    if n <= len(str1):
        return str1[:n]
    else:
        return "invalid"

print(first_n_vowels('ProgrAmmEr',3))

# ------------------------------------------------------------------
# Is to return 12 hours format to 24 hours and vice versa
def convert_time(time):
    checker = 'apm '  # To check if there is any am, pm, or space and remove them later
    time1 = ''  # Initial value to build up a new string without am, pm, or spaces
    am_pm = ''  # Initial value to be used in conditional and to add am, pm to a 24 format or remove them from a 12 format
    for i in time:  # Iterate throw the time
        if 'm' in time:  # This conditional to check whether or not it's a 12 format
            if i not in checker:  # Only allow numbers for the next line without am, pm, or spaces
                time1 = time1 + i
            elif i == 'a':  # To give a value am if the time contains am, that would be used later converting from a 12 to a 24 format
                am_pm = 'am'
            elif i == 'p':  # To give a value pm if the time contains pm, that would be used later converting from a 12 to a 24 format
                am_pm = 'pm'
        else:  # This works only if the time is in 24 format
            if i not in checker:  # Only allow numbers for the next line without spaces
                time1 = time1 + i

    lis = time1.split(':')

    if int(lis[0]) == 12 and am_pm == 'am':  # from 12 to 24 This works converting only ( 12:00 - 12:59 am to 0:00 - 0:59 )
        lis[0] = '0'
        am_pm = ''
        print('( 12:00 - 12:59 am to 0:00 - 0:59 )')
    elif int(lis[0]) < 12 and am_pm == 'am':  # from 12 to 24 This works converting the range ( 01:00 - 11:59 am to 01:00-11:59 )
        lis[0] = int(lis[0])
        am_pm = ''
        print('( 01:00 - 11:59 am to 01:00-11:59 )')
    elif int(lis[0]) == 12 and am_pm == 'pm':  # from 12 to 24 This works converting the range ( 12:00 - 12:59 pm to 12:00-12:59 )
        lis[0] = int(lis[0])
        am_pm = ''
        print('( 12:00 - 12:59 pm to 12:00-12:59 )')
    elif am_pm == 'pm':  # from 12 to 24 This works converting the range ( 01:00 - 11:59 pm to 13:00 - 23:59 )
        lis[0] = int(lis[0]) + 12
        am_pm = ''
        print('( 01:00 - 11:59 pm to 13:00 - 23:59 )')
    else:
        if int(lis[0]) == 12:  # from 24 to 12 This works converting only ( 12:00 - 12:59 to  12:00 - 12:59 pm)
            am_pm = 'pm'
            print('( 12:00 - 12:59 to  12:00 - 12:59 pm)')
        elif int(lis[0]) == 00:  # from 24 to 12 This works converting only ( 00:00 - 00:59 to  12:00 - 12:59 am)
            lis[0] = int(lis[0]) + 12
            am_pm = 'am'
            print('( 00:00 - 00:59 to  12:00 - 12:59 am)')
        elif int(lis[0]) < 12:  # from 24 to 12 This works converting only ( 01:00 - 11:59 to  01:00 - 11:59 am)
            am_pm = 'am'
            print('( 01:00 - 11:59 to  01:00 - 11:59 am)')
        else:                   # from 24 to 12 This works converting only ( 13:00 - 23:59 to  01:00 - 11:59 pm)
            lis[0] = int(lis[0]) - 12
            am_pm = 'pm'
            print('( 13:00 - 23:59 to  01:00 - 11:59 pm)')

    result = str(lis[0]) + ':' + str(lis[1]) + ' ' + am_pm
    return result

print(convert_time('21:25'))

# ------------------------------------------------------------------
# postfix expressions
def postFix(expr):
    lis = expr.split() # Remove the spaces and this is good to distinguish the difference between 6 55 23 1 and 6 5 5 2 3 1
    stack = []  # Initial value for stack that will be used for push/pop operations
    for i in lis: # Iterate and select one element from the lis list
        if i.isnumeric(): # It only allows integers not floating point
            stack.append(int(i)) # Push only the numbers
        else:  # If it's +, -, *, /, or any other symbols
            right = stack.pop() # Pop the last elemnt of the stack
            left = stack.pop() # Pop the last elemnt of the stack again!

            # Make sure that the 1st pop goes to the right side of operator and the 2nd pop goes to the left side.
            if i == '+':
                result = left + right
            elif i == '-':
                result = left - right
            elif i == '*':
                result = left * right
            elif i == '/':
                result = left / right
            elif i == '^':
                result = left ** right
            else: # It's not allowed to have any other symbols than +, -, *, /, **
                return 'Invalid'
            stack.append(int(result))
    return int(result) # Return the result in integer type


print(postFix('4 1 - 2 *'))
# ------------------------------------------------------------------
# Je Code

info = {
    'Amal' : '1111111111' ,
    'Mohammed' : '2222222222' ,
    'Khadija'  : '3333333333' ,
    'Abdullah'  : '4444444444' ,
    'Rawan'  : '5555555555',        # تم عمل  dic
    'Faisal' : '6666666666' ,
    'Layla' : '7777777777'
}

def getOwner(dic , number):
    if number.isdigit() and len(number) == 10:    #  اذا كان طول الرقم يساوي 10
        for name, number in dic.items():
            if user_input == number:
                print(name)
                break                             #اذا تحقق الشرط راح توقف
        else:
            print("Sorry the number is not found!") # اذا لم يتحقق الشرط راح يطبع هذه الرساله
    else:
        print("This is invalid number")             #  اذا الرقم لم يساوي 10 راح يطبع هذه الرساله


def getNumber(dic , name):
    for name, number in dic.items():
        if user_input == name:                      # اذا المستخدم ادخل الاسم وكان يساوي الاسم
            print(number)                             # راح يطبع له الرقم الخاص بالاسم المدخل
            break                                   #اذا تحقق الشرط راح توقف
    else:
        print("Sorry the name is bot found!")   # اذا الاسم المدخل غير موجود راح يطبع هذه الرساله



def addNewUser(dic):                                # انشاء داله لاضافة اسم ورقم جديد
    name = input("Enter the name of the new user: ") # انشاء متغير يتم ادخال اسم الشخص الغير موجود ب القاموس
    number = input("Enter the number of the new user: ") # انشاء متغير يتم ادخال رقم الشخص الغير موجود ب القاموس
    dic[name] = number

    return dic


i = int(input(
    'Welcome to the phone book.\nTo search using the phone number please enter the number: 1 \nTo search using the name please enter the number: 2 \nTo add a new name and number to the phone book please enter the number: 3 \nTo exit press 4: '))
while i != 4:                                                          # اذا لوب لا يساوي 4 انتقل للي بعده اذا يساوي 4 يتم اغلاق التطبيق
    if i == 1:                                                          # اذا يساوي 1 نفذ لي الشرط اللي بعده
        user_input = input('Enter the number of user: ')                    #  متغير يدخل المستخدم رقم اللي يبي بحثت عنه
        getOwner(info, user_input)
    elif i == 2:                                                          # اذا يساوي 2 نفذ لي الشرط اللي بعده
        user_input = input('Enter the name of user: ')                          #  متغير يدخل المستخدم اسم اللي يبي بحثت عنه
        getNumber(info, user_input)
    elif i == 3:                                                             # اذا يساوي 3 نفذ لي الشرط اللي بعده
        print(addNewUser(info))                                                 # dic يتم اضافه اسم جديد ورقم جديد في  addNewUser استناد الى داله

    else:
        print(" You must choose one of '1-2-3-4' ")
        break

    i = int(input(
        'Welcome to the phone book.\nTo search using the phone number please enter the number: 1 \nTo search using the name please enter the number: 2 \nTo add a new name and number to the phone book please enter the number: 3 \nTo exit press 4: '))



# ------------------------------------------------------------------
#Awiteb Code
import re
from typing import Union

class Telephone_book:
    telephones_lst = []
    def name_checker(self, new_name: str) -> bool:
        checker = lambda name: not not re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name)
        if type(new_name) == str:
            if len(new_name) >= 3 and checker(new_name):
                return True
            else:
                raise ValueError(f"Invalid name, '{new_name}' is incorrect name.")
        else:
            raise ValueError(f"Invalid name, '{new_name} muts be string'")

    def phone_checker(self, new_phone: int) -> bool:
        if len(str(new_phone)) == 9:
            return True
        else:
            raise ValueError(f"Invalid phone number, '{new_phone}' length must be equal 9.")

    def add_new(self, name: str, phone: int) -> None:
        if self.name_checker(name) and self.phone_checker(phone):
            phone_dct = {"name": name,
                                                                    "phone_number":phone}
            Telephone_book.telephones_lst.append(phone_dct)
        else:
            pass

    def _find(self, value, key: str):
        filter_lst = filter(lambda dct: dct[key] == value, Telephone_book.telephones_lst)
        if filter_lst:
            return list(filter_lst)
        else:
            raise Exception(f"'{value}' was not found in the phone book")

    def _by_name(self, name: str) -> dict:
        return self._find(name, 'name')

    def _by_phone(self, phone: int) -> dict:
        return self._find(phone, 'phone_number')

    def get(self, value: Union[int, str]) -> Union[int, str]:
        if type(value) == str:
            return self._by_name(value)
        else:
            return self._by_phone(value)
