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



value = "21"
print(f"{value} is {input_type(value)}")

----------------------------------------------------
# using dictionaries
def most_frequent_element(arr):
    dic = {}
    reverse_dic = {}
    result = {}
    for i in arr:
        dic[f"{i}"] = arr.count(i)

    count_max = str(max(dic.values()))

    for key, value in dic.items():
        reverse_dic[f"{value}"] = int(key)

    for key,value in reverse_dic.items():
        if key == count_max:
            result[key]=value
    list1 = list(result.values())
    return list1[0]
    
x = most_frequent_element([2,3,4,1,5,-5,-5,-5,-5,-5,6])
print(x)


# looping in the list
def most_frequent(List):
    frequent_num = List[0]
    count = 0
    for i in List:
        current_count = List.count(i)
        if (current_count > count):
            count = current_count
            frequent_num = i
    return str(frequent_num)


List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))
