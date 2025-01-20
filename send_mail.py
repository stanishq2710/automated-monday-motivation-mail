import smtplib
import datetime as dt
import random as r
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

my_email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

# Check if today is Monday
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:  # Monday
    try:
        # Read quotes from file
        with open("quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = r.choice(all_quotes).strip()

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Monday Motivation\n\n{quote}"
            )
        print(f"Email sent successfully on {now.strftime('%Y-%m-%d %H:%M:%S')}")
    except FileNotFoundError:
        print("Error: quotes.txt file not found.")
    except Exception as e:
        print(f"Failed to send email: {e}")
