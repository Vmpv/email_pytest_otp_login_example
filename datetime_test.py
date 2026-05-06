import datetime as dtm
import os
from dotenv import load_dotenv
from playwright.sync_api import Page, expect
from mailosauros_test import get_otp_passcode, generate_email_address

load_dotenv()
server_domain = os.getenv("MAILOSAUR_SERVER_ID")
if server_domain is None:
	raise EnvironmentError("MAILOSAUR_SERVER_ID environment variable is not set.")

print("this is the generated email", generate_email_address(server_domain))

print (dtm.datetime.today())
print(dtm.timedelta(hours=1))

#datetime = (datetime.today() - timedelta(hours=1)),

print ("today minus timedetla = ", dtm.datetime.today() - dtm.timedelta(hours=1,minutes=15) )

email_account_timestamp = dtm.datetime.now()

print ("this is the formated date" , dtm.datetime.strftime(dtm.datetime.now(), "%d%m%H%M%S"))

print ("this is the formated date using the timestamp" , dtm.datetime.strftime(email_account_timestamp, "%d%m%H%M%S"))