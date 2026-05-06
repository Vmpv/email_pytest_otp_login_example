
import os
from dotenv import load_dotenv
from playwright.sync_api import Page, expect
from mailosauros_test import get_otp_passcode, generate_email_address

load_dotenv()
server_domain = os.getenv("MAILOSAUR_SERVER_ID")


def test_full_flow(page: Page) -> None:
    page.goto("https://lastbottlewines.com/")
    page.get_by_role("button", name="YES").click()
    page.get_by_role("link", name="Log In / Sign Up").click()
#Generate an email addres and fill the email field
    gen_email_address = generate_email_address(server_domain)
    page.get_by_role("textbox", name="Email").fill(gen_email_address)
#small wait then click continue to send the emails
    page.get_by_role("button", name="Continue", exact=True).click()
#go to the email address, get the passcode and submit
    email_otp_passcode = get_otp_passcode(gen_email_address)
    page.get_by_role("textbox", name="-digit code").fill(email_otp_passcode)
    page.get_by_role("button", name="Submit").click()
#Check that we are logged    
    expect(page.get_by_role("link", name="Log Out")).to_be_visible()
    expect(page.get_by_role("link", name="YOU HAVE $ 0 IN CREDIT")).to_be_visible()
    page.wait_for_timeout(3000)