import requests
import smtplib

endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key="9ecd3d37b09781c1f91da414b6ccb0a8"

parameters={
    "lat":13.406948,
    "lon":80.110298,
    "appid":api_key
}

response=requests.get(url=endpoint,params=parameters)
response.raise_for_status()
#print(response.status_code)
data=(response.json())
#print(data)
lst=(data["list"])
#print(lst)
will_rain=False
for i in lst:
    weather=i["weather"][0]
    # print(weather)
    ID=weather["id"]
    # print(ID)
    if ID<700:
        # print("Bring an Umbrella.")
        will_rain=True
if will_rain:
    my_mail="20d3725bathrinath@gmail.com"
    password="kzkjwppvxdmsyysh"

    with smtplib.SMTP("smtp.gmail.com") as message:
        message.starttls()
        message.login(user=my_mail,password=password)
        message.sendmail(from_addr="my_mail",to_addrs="bitbatbathri0608@gmail.com",msg="Subject:It's rainy today!!!\n\n\nBring an Umbrella")