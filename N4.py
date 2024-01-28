import datetime as dt
from datetime import datetime as dtdt

import re

def get_upcoming_birthdays(users):
    today_date = dtdt.today()
    today_year = str(dtdt.today().year)
    
    list_congr_users = []
    
    for user in users:
        user_birthday = user['birthday']
        this_year_user_birthday = today_year + user_birthday[4:] #change first 4 charackters
        this_year_user_birthday = dtdt.strptime(this_year_user_birthday,'%Y.%m.%d').date() #to date
        weak_day = this_year_user_birthday.isoweekday() #get num weakday
        
        if(0 <= (this_year_user_birthday-today_date.date()).days < 7 ):
            #saturday
            if(weak_day == 6):
                this_year_user_birthday = this_year_user_birthday + dt.timedelta(days=2)
            #sunday
            elif(weak_day == 7):
                this_year_user_birthday = this_year_user_birthday + dt.timedelta(days=1)    
            
            list_congr_users.append({'name': user['name'], 'birthday': this_year_user_birthday.strftime('%Y,%m,%d')})
    
    return list_congr_users


users = [
    {"name": "John Doe", "birthday": "1985.01.31"},
    {"name": "Jane Smith", "birthday": "1990.01.28"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
