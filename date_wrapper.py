months = {3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August"}
days = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
test = "7 May 2020"
def wrapper(date, month_index):
    date = date.split()
    cut_date = date[:3]

    for zero_in_day in days:
        if cut_date[0] == zero_in_day:
            cut_date[0] = "0"+cut_date[0]

    if cut_date[2] != "2020":
        cut_date[2] = "2020"
    for pattern in cut_date:
        for keys, vals in months.items():
            if pattern == vals:
                cut_date[month_index] = "0"+str(keys)
                return "/".join(cut_date)


