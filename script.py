import os
from selenium import webdriver
from time import sleep
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.headless = True

d = webdriver.Firefox(options=fireFoxOptions)


def get_text():
    d.get(
        "https://middlebury.datacenter.adirondacksolutions.com/MIDDLEBURY_THDSS_PROD/"
    )
    sleep(2)
    d.find_element(by="xpath", value="//*[@id='i0116']").send_keys(
        "ballanrahill@middlebury.edu"
    )
    d.find_element(by="xpath", value="//*[@id='idSIButton9']").click()
    sleep(1)
    d.find_element(by="xpath", value="//*[@id='i0118']").send_keys("4Alphabeta!")
    d.find_element(by="xpath", value="//*[@id='idSIButton9']").click()
    sleep(1)
    d.find_element(by="xpath", value="//*[@id='idSIButton9']").click()
    sleep(8)

    return d.find_element(
        by="xpath",
        value="/html/body/app-root/app-navigation/mat-sidenav-container/mat-sidenav-content/div/mat-card/div/div[1]/app-student/app-my-screen/div/div[3]/div/mat-card/mat-card-content/p",
    ).text


text = get_text()
numbers = ["+12079495767", "+19176089652"]
if text != "There are no room selections to display":
    # send email
    print(text)
    for number in numbers:
        message = client.messages.create(
            body=f"There is an update: {text}", from_="+13186665866", to=number
        )

d.quit()
