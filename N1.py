import datetime as dt
from datetime import datetime as dtdt

def get_days_from_today(date):
    try:
        date_p = dtdt.strptime(date,"%Y-%m-%d")
    except ValueError:
        return 'date must be "YYYY-MM-DD" format'
        
    date_now = dtdt.today()
    return (date_now-date_p).days
    
print(get_days_from_today("2025-12-19"))