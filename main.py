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
