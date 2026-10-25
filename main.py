import os
import smtplib

import requests


OPENWEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"


def required_env(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def main():
    api_key = required_env("OPENWEATHER_API_KEY")
    latitude = float(required_env("WEATHER_LATITUDE"))
    longitude = float(required_env("WEATHER_LONGITUDE"))
    smtp_user = required_env("SMTP_USER")
    smtp_password = required_env("SMTP_PASSWORD")
    notification_recipient = required_env("NOTIFICATION_RECIPIENT")

    weather_params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
    }
    response = requests.get(url=OPENWEATHER_ENDPOINT, params=weather_params, timeout=30)
    response.raise_for_status()
    weather_slice = response.json()["list"][:8]
    will_rain = any(int(period["weather"][0]["id"]) < 700 for period in weather_slice)

    if will_rain:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=smtp_user, password=smtp_password)
            connection.sendmail(
                from_addr=smtp_user,
                to_addrs=notification_recipient,
                msg=("Subject: Take an Umbrella\n\n"
                     "It is going to rain in the next 24 hours. Take an umbrella with you."),
            )


if __name__ == "__main__":
    main()
