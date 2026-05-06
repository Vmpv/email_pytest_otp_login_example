from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria
from dotenv import load_dotenv
import os
import datetime as dtm
import re
import time

load_dotenv()
MAILSAUROS_API_KEY = os.getenv("MAILOSAUR_API_KEY")
MAILOSAUR_SERVER_ID = os.getenv("MAILOSAUR_SERVER_ID")
mailosaur = MailosaurClient(MAILSAUROS_API_KEY)

server_domain = os.getenv("MAILOSAUR_SERVER_ID")

def generate_email_address(server_domain:str):
    email_account_timestamp = dtm.datetime.now()
    current_address = f"OTP_{dtm.datetime.strftime(email_account_timestamp, '%d%m%H%M%S')}@{server_domain}.mailosaur.net"
    #print (current_address)
    return str(current_address)

#generate_email_address(server_domain)
#my current email

#search for emails to to the address above
### TO DO : This method servers its purpose butreturns only the most recent email,
#  find the method that returns more than one
def get_otp_passcode(current_address:str):
    search_start_time = time.time()
    max_wait_seconds = 30

    while time.time() - search_start_time < max_wait_seconds: 
        try:
    #search for emails sent to the previous defined address for 30 secs 
    #only emails sent within the last 15 min are searched
            criteria = SearchCriteria()
            criteria.sent_to = current_address
            max_valid_time = dtm.datetime.today() - dtm.timedelta(hours=1,minutes=15)#we need to pass 1h because the get method is weird
            email = mailosaur.messages.get(MAILOSAUR_SERVER_ID, criteria, received_after=max_valid_time)
            #print (email.subject)
            match = re.search("([0-9]{6})", email.subject)
            OTP_PASSCODE = match.group()
            #print("pass code is =", OTP_PASSCODE)
            return OTP_PASSCODE
        except Exception as e:
            print ("Error retrieving passcode: ", e)


#get_otp_passcode("otp_0105224751@zcsrr9zc.mailosaur.net")
