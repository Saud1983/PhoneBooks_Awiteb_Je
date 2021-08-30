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
        for i in array: # To iterate throw array
            if i < current_item:
                current_item = i # Update the cerrent_item with the smaller value when the condition is True
        list1.append(current_item) # Append the next smallest value to another list that will build up more and more until the while loop has stopped
        array.remove(current_item) # Remove the same smalledt value from the original list that shrenks more and more until it has no elements and that but an end to while loop
    return list1 # return the sorted list that starts elements from the smallest to biggest
