import smtplib

gmail_user = '<input your gmail user. No need to use @gmail.com>'
gmail_password = '<input your gmail password>'

def send_alert_of_price_reduction(product_title = '',original_price = '',latest_price = ''):
    sent_from = gmail_user
    to = ['vincentkernn@gmail.com']
    subject = 'Alert: your product price for %s is reduced' % (product_title)
    body = 'Alert for reduce in price from %s to %s' % (original_price,latest_price)

    email_text = """\
    From: %s
    To: %s
    Subject: %s
    
    %s
    """ % (sent_from, ", ".join(to), subject, body)

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