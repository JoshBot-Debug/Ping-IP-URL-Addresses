import smtplib
from email.message import EmailMessage

class SendEmail:

    def __init__(self):
        '''
        This class sends emails, nothing special to see here.
        '''
        self.msg = EmailMessage()
        self.msg.add_header


    def set_body(self,content):
        self.msg.set_content(content)


    def set_subject(self,subject):
        self.msg['Subject'] = subject


    def set_from(self,email):
        self.msg['From'] = email
        self.SENDER_EMAIL = email


    def set_from_pwd(self,password):
        self.SENDER_PWD = password


    def set_to(self,email):
        self.msg['To'] = email


    def set_recipients(self,email_list):
        self.msg['To'] = ", ".join(email_list)


    def send(self):
        try:
            s = smtplib.SMTP('smtp.gmail.com',587)
        except:
            print('Could not establish connection, please check you internet connection')
            return False
        s.starttls()
        s.login(self.SENDER_EMAIL, self.SENDER_PWD)
        s.send_message(self.msg)
        s.quit()