def fibonacci_generator(n:int)->list:
    """This function will return a list as fibonacci pattern"""
    result = []
    for _ in range(n):
        if len(result) == 0:
            result.append(0)
        elif len(result) == 1:
            result.append(1)
        else:
            result.append(result[len(result)-2] + result[len(result)-1])
    return result


number = None
while True:
    ask_user=input("Please pick a number: ")
    if ask_user.isdigit():
        number = int(ask_user)
        break
    else:
        print(f"{ask_user} is not a valid number!!!")

print(fibonacci_generator(number))
