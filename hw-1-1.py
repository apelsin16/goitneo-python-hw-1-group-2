from datetime import datetime
import collections

def default_value():
    return 'No birthdays this week'

def get_birthdays_per_week (users):
    birthday_people = collections.defaultdict(default_value)
    
    
    current_date = datetime.today().date()
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=current_date.year)
        if birthday_this_year < current_date:
            birthday_this_year = birthday.replace(year=birthday_this_year.year + 1)
        delta_days = (birthday_this_year - current_date).days
        if delta_days < 7:
            birthday_weekday = birthday_this_year.weekday()
            if birthday_weekday == 1:
                birthday_people["Monday: "] = birthday_people.get('Monday: ', []) + [name]
            if birthday_weekday == 2:
                birthday_people["Tuesday: "] = birthday_people.get('Tuesday: ', []) + [name]
            if birthday_weekday == 3:
                birthday_people["Wednesday: "] = birthday_people.get('Wednesday: ', []) + [name]
            if birthday_weekday == 4:
                birthday_people["Thursday: "] = birthday_people.get('Thursday: ', []) + [name]
            if birthday_weekday == 5:
                birthday_people["Friday: "] = birthday_people.get('Friday: ', []) + [name]
            
            elif birthday_weekday == 6 or birthday_weekday == 7:
                birthday_people["Next week birthday person"] = birthday_people.get('Next week birthday person', []) + [name]
    for day, names in birthday_people.items():
        birthday_people[day] = ', '.join(names)
    print(birthday_people)
