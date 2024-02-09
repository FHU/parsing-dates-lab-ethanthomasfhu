def parse_month(month):
    months = {"January": "01", "February": "02", "March": "03", "April": "04", 
              "May": "05", "June": "06", "July": "07", "August": "08", 
              "September": "09", "October": "10", "November": "11", 
              "December": "12" }
    month_numeric = months[month]
    return month_numeric

def parse_day(day):
    day = day.replace(",","")
    new= "0"
    day_number = int(day)

    if day_number < 10:
        new += day 
    else:
        new = day

    return new
    pass

def parse_date(user_string):
    parsed_date = ""
    comps = user_string.split()
    month = comps[0]
    day = comps[1]
    year = comps[2]

    month_str = parse_month(month)
    day_str = parse_day(day)

    parsed_date = month_str + "/" + day_str + "/" + year

    return parsed_date

    pass

if __name__ == '__main__':
    user_input = input("Enter a date: ")

    while user_input != "-1":
        parsed = parse_date(user_input)
        print(parsed)
        user_input = input("Enter a date: ")