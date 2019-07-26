import smtplib
import configparser
import re

config = configparser.ConfigParser()
config.read('email_properties.ini')
gmail_user = config['EMAIL']['user']
gmail_password = config['EMAIL']['password']

def send_alert_of_price_reduction(product_title = '',original_price = '',latest_price = ''):
    # product_title = re.sub('\W+','', product_title)
    sent_from = gmail_user
    to = ['vincentkernn@gmail.com']
    subject = 'Alert: your product price is reduced'
    body = 'Alert for reduce in price from %s to %s' % (original_price,latest_price)


    email_text = """
    From: %s
    To: %s
    
    %s
    %s
    """ % (sent_from,to,subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except Exception as e:
        print(e)
        print ('Something went wrong...')