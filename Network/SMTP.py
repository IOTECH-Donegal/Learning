import smtplib
import getpass

def send_email(user, password, to, _from, subject, text):
    print("Sending E-Mail")
    try:
        with smtplib.SMTP("mail.tu-harburg.de", 587) as smtpserver:
            smtpserver.starttls()
            smtpserver.login(user, password)
            header  = 'To:' + to + '\n'
            header += 'From:' + _from + '\n'
            header += 'Subject:' + subject + '\n'
            print(header)
            msg = header + '\n' + text + '\n\n'
            smtpserver.sendmail(user, to, msg)
    except Exception as error:
        print(error)
        return False
    return True

user = 'john.oraw@iotech.ie'
_from = 'john.oraw@iotech.ie'
to = 'john.oraw@lyit.ie'
subject = 'SMTP TEST'
text = """SMTP Test
This is a test email.
You can delete it.
"""

pwd  = getpass.getpass(prompt='Enter your password: ')
print(send_email(user, pwd, to, _from, subject, text))