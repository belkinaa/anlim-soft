import datetime
def make_date(val):
    format_date = "%Y-%m-%d"
    return datetime.datetime.strptime(val, format_date)

for rental_date_range_film in [(make_date("2020-1-1"), make_date("2020-1-7")),
                               (make_date("2020-1-15"), make_date("2020-2-7"))]:
    start_rental, end_rental = rental_date_range_film
    date_rental = start_rental
    while date_rental <= end_rental:
        print(date_rental)
        date_rental += datetime.timedelta(days=1)