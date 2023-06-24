import smtplib
import datetime as dt
import random

my_email = "ashishkumar947140@gmail.com"
Password = "bpzppppaxovjzzfb"
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week in range(0, 6):
    # get a random quote
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()  # obtain a list of quotes
        quote = random.choice(all_quotes)

    # print(quote)
    # print(quote2)
    # sending mail

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=Password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="a_kumar1@mt.iitr.ac.in",
            msg=f"Subject:Quote of the Day\n\n{quote}"

        )
