import re

def normalize_phone(phone_number):
    
    p = r"[\+\d]+"
    
    norm_phone_number = ''.join(re.findall(p,phone_number))
    if(len(norm_phone_number) == 12):
        norm_phone_number = '+' + norm_phone_number
    elif(len(norm_phone_number) == 10):
        norm_phone_number = '+38' + norm_phone_number
    return norm_phone_number
    
print(normalize_phone('056-353-64-97'))