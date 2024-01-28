import random 

def get_numbers_ticket(min, max, quantity):
    
    lotery_list = []
    
    if(type(min) != int or min < 1 or min >= max):
        return f'min must be "int", between 1 and {max}'
    elif(type(max) != int or max > 1000):
        return f'max must be "int", between {min} and 1001'
    elif(type(quantity) != int or quantity > (max-min+1)):
        return f'quantity must be "int", less or equal then {(max-min+1)}'
    else:
    
        while len(lotery_list) < quantity:
            random_num = random.randint(min,max)
            if random_num not in lotery_list:
                lotery_list.append(random_num)
    
    return lotery_list

print(get_numbers_ticket(1, 36, 5))
    