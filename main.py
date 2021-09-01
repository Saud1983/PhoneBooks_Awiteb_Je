def input_type(value):
    try:
        number = int(value)
        message = "integer"
        return message
    except ValueError:
        try:
            number = float(value)
            message = "double"
            return message
        except ValueError:
            number = value
            message = "string"
            return message

    # Shorten the code
    # try:
    #     int(value)
    #     return "integer"
    # except ValueError:
    #     try:
    #         return "double"
    #     except ValueError:
    #         return "string"



value = "21"
print(f"{value} is {input_type(value)}")

----------------------------------------------------
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

------------------------------------------------------------------
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

------------------------------------------------------------------

def factorial(number):
  list1 = [] # New list to add all the factorial numbers
  result=1 # Inital Value to be used at the end with value 1 that doesn't affect the multiplication

  for i in range(number): # Iterate Throw a range with length of a givin number
      list1.append(i+1) # Append all number to the list after adding 1 because the range starts from 0

  for n in list1: # Iterate throw the new list to get one element at a time
      result = result * n # make the math with new element, remember that the result has a value of 1 in the first round
  return result # return the result

------------------------------------------------------------------

def primes_nums(array):
    primes_list = [] # A list that will contain all the prime numbers
    for i in array: # Iterate throw the original list
        pr = True # Set Inital value to be used later

        # need to make sure is it enough t use i or we have add +1
        for x in range(2, i+1): # Loop throw a range from 2 to that element value in the original list
            if i % x == 0: # This conditional tests the element throw out the whole range.
                pr = False # It's enough to find one number that has False becase 1 and the number it self are not included in the range.
        if pr == True : # This only allow prime numbers to go inside
            primes_list.append(i) # Building up the new list with prime numbers
    return primes_list # return the list that contains prime numbers

------------------------------------------------------------------
# To return a sequence numbers from 0 to that number as string
def numbers_range(number):
    asstring = "0"
    for i in range(1,number+1):
            asstring = asstring + " " + str(i)
    return asstring
