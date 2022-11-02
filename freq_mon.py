from datetime import date,timedelta

type_bot = "xdotool key "
year = 2022

month=int(input("Mês: "))

weekdays="STQQSSD"
mday=date(year, month, 1)
while mday.month == month:
    print(type_bot, weekdays[mday.weekday()])
    print(type_bot, "Tab")
    mday=mday+timedelta(days=1)
