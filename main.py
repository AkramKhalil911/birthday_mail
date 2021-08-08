import smtplib
import pandas
import datetime as dt
import random

MY_EMAIL = "EMAIL"
PASSWORD = "PASSWORD"

birth_file = pandas.read_csv("birthdays.csv")
birt_dict = birth_file.to_dict(orient="records")

now = dt.datetime.now()
current_month = now.month
current_day = now.day

for birt_count in range(len(birt_dict)):
    birth_month = birt_dict[birt_count]["month"]
    birth_day = birt_dict[birt_count]["day"]
    birt_name = birt_dict[birt_count]["name"]
    birth_email = birt_dict[birt_count]["email"]
    if birth_month == current_month and birth_day == current_day:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
            replace_letter = letter_file.read()
            replace_letter = replace_letter.replace("[NAME]", birt_name)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birth_email,
                                msg=f"subject:Happy birthday\n\n{replace_letter}")