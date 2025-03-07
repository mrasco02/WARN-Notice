import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scraper import WARNNoticeScraper

EMAIL_ADDRESS = "warnnoticenewsletter@gmail.com"
EMAIL_PASSWORD = os.environ["WARN_NOTICE_EMAIL_PASSWORD"] #App password on local machine

msg = MIMEMultipart()
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS #For testing
msg['Subject'] = 'WARN Notice Newsletter'

scraper = WARNNoticeScraper("Megan")  # Instantiate the scraper class
msg.attach(MIMEText(scraper.get_email_body(), "html"))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

try:
    mailserver.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,msg.as_string())
    print("Email sent successfully")
    print(EMAIL_ADDRESS)
    print(EMAIL_PASSWORD)
    print(msg.as_string())
except Exception as e:
    print(f"Error sending email: {e}")

mailserver.quit()