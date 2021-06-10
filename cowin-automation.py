import json
import requests
import smtplib, ssl
from datetime import date


def call_api(dated, dist_id):
    api_uri = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" + dist_id + "&date=" + dated
    result = requests.get(api_uri)
    result_json = json.loads(result.text)
    centers = result_json["centers"]
    for center in centers:
        sessions = center["sessions"]
        for session in sessions:
            if session["min_age_limit"] == 18:
                print(session["available_capacity"])
                print(center)
                sms_text = "name of center=" + center["name"] + " address=" + center["address"] + " slots available=" + str(session["available_capacity"]) + " vaccine_name=" + session["vaccine"]
                if session["available_capacity"] == 0:
                    send_email(sms_text, "diptendu.chakraborty.2012@gmail.com")
                    send_email(sms_text, "priyankachoudhury93@gmail.com")


def send_email(message, receiver_email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "diptendu.chakraborty.2012@gmail.com"  # Enter your address
    receiver_email = receiver_email # Enter receiver address
    password = "Krishna@166"
    message = message
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


if __name__ == '__main__':
    today = date.today()
    call_api(str(today.strftime("%d-%m-%Y")), "247")
