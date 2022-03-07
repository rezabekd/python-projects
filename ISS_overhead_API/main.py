import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 49.746841
MY_LNG = 13.376990


def check_position():
    response_iss = requests.get("http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()
    longitude = float(data_iss["iss_position"]["longitude"])
    latitude = float(data_iss["iss_position"]["latitude"])

    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LNG - 5 <= longitude <= MY_LNG + 5:
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


position_collision = check_position()
is_night = is_dark()

while True:
    time.sleep(60)
    if position_collision and is_night:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="example@example.com", password="example_password")
            connection.sendmail(from_addr="example@example.com",
                                to_addrs="example@example.com",
                                msg="Subject:ISS checker\n\nLook up, ISS is over your head!")


