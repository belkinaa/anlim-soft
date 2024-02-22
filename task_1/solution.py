import datetime

make_str_date_to_datetime = lambda Ymd:  datetime.datetime.strptime(Ymd, "%Y-%m-%d")

for rental_date_range_film in [map(make_str_date_to_datetime, ("2020-1-1", "2020-1-7")),
                               map(make_str_date_to_datetime, ("2020-1-15", "2020-2-7"))]:
    start_rental, end_rental = rental_date_range_film
    date_rental = start_rental
    while date_rental <= end_rental:
        print(date_rental)
        date_rental += datetime.timedelta(days=1)