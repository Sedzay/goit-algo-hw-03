import re

def normalize_phone(phone_number):
    
    p = r"[\+\d]+"
    
    norm_phone_number = ''.join(re.findall(p,phone_number))
    if(len(norm_phone_number) == 12):
        norm_phone_number = '+' + norm_phone_number
    elif(len(norm_phone_number) == 10):
        norm_phone_number = '+38' + norm_phone_number
    return norm_phone_number
    
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)