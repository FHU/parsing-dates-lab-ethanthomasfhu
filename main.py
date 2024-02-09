def parse_month(month):
    month_values = {
        "January":"01",
        "February":"02",
        "March":"03",
        "April":"04",
        "May":"05",
        "June":"06",
        "July":"07",
        "August":"08",
        "September":"09",
        "October":"10",
        "November":"11",
        "December":"12"
    }
    month_number = month_values[month]
    return month_number

def day_place(day):
    day = day.replace(",","")
    new_value = "0"
    day_value = int(day)

    if day_value < 10:
        new_value += day
    else:
        new = day

    return new

def parse_date(user_string):
    date_string = ""
    all_together = user_string.split()
    month = all_together[0]
    day = all_together[1]
    year = all_together[2]

    month_value = parse_month(month)
    day_value = day_place(day)

    date_string = month_value + "/" + day_value + "/" + year

    return date_string
    
if __name__ == '__main__':
    user_date = input()

    while user_date != "-1":
        complete = parse_date(user_date)
        print(complete)
        user_date = input()