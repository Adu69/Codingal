from datetime import date, time, datetime
today = date.today()
now = datetime.now()
print("The date today is",today)
print("The time is",now)
print("\n Date components: ",today.year, today.month, today.day)