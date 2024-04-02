import requests
import smtplib

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "12b6b81f268797034abd656d620bf4ee"

weather_params = {
    "lat": 6.9319,
    "lon": 79.8478,
    "appid": API_KEY,
}

response = requests.get(url=OWM_Endpoint, params=weather_params)

# print(response.status_code)
response.raise_for_status()
weather_data = response.json()

# print(weather_data)

will_rain = False

weather_slice = weather_data["list"][:8]
# print(weather_slice)
for three_hour_data in weather_slice:
    condition_code = three_hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:

    my_email = "pythontesting0032@gmail.com"
    password = "rowxuvkbrjchmign"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="kanthiwijesinghe71@gmail.com",
                            msg="subject:Take an Umbrella\n\n"
                                "It is going to rain in 24 hours.Take the umbrella with you.")
        connection.close()

# Send SMS using twilio

# from twilio.rest import Client
# To run in pythonanywhere
# from twilio.http.http_client import TwilioHttpClient
# import os

# account_sid = "ACc3ca1785171fd3ff27a63d815533f7f6"
# auth_token = "f683bb2b7cabdaffc268fbaf5a4d64b5"

# if will_rain:
    # # To run in pythonanywhere
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {"http": os.environ["https_proxy"]}
    # client = Client(account_sid, auth_token, http_client=proxy_client)

    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body="It's going to rain today. Remember to bring an umbrella.",
    #     from="564235645684",
    #     to="+9471087511"
    # )
    # print(message.sid)
    # print(message.status)

