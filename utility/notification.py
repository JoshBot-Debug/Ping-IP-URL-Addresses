import _thread 
from utility.send_email import SendEmail
import time

class Notification(object):

    def __init__(self):
        '''
        This class should be instiated and the check() method should be called
        and passed an object. The object unique data (in this case an ip and url)
        will be stored to make sure that we do not send duplicate emails everytime
        the check() method is called.
        '''
        self.__NOTIFICATION = {}


    def check(self,ping_obj):
        # Setting the ping obj here
        self.ping_obj = ping_obj

        if ping_obj.getStatus():
            if ping_obj.getHost() in self.__NOTIFICATION:
                self.__NOTIFICATION.pop(ping_obj.getHost())

        if not ping_obj.getStatus():
            if ping_obj.getHost() in self.__NOTIFICATION:
                # Notification already sent
                print('Email already sent')
                return True
            else:
                # Sending email
                self.__NOTIFICATION.update({ping_obj.getHost():{
                    'status': ping_obj.getStatus(),
                    'time': time.strftime("%H:%M:%S", time.localtime()),
                }})
                
                first_line = self.ping_obj.getHost()
                second_line = self.ping_obj.getDetails()
                _thread.start_new_thread(self.sendEmail, (first_line,second_line)) # NEED TO CHECK IF THIS THREAD CLOSES ON ITS OWN

                print('SENDING email')


    def sendEmail(self,first_line,second_line):
        if self._list_email:
            print(f'[SENDING EMAIL(s) TO] : {self._list_email}')
            email = SendEmail()
            email.set_body(f'Hey there, \n \n Something is wrong, here are some details : \n \n {first_line} \n \n {second_line} \n \n Regards,\nYour friendly bot')
            email.set_subject(f'{first_line} => is down')
            email.set_from('trioittesting@gmail.com')
            email.set_from_pwd('P@ssw0rd@123')
            email.set_recipients(self._list_email)
            email.send()
            print('[SENT ALL EMAILS]')
        else:
            pass
            #print(f'[EMAIL LIST IS EMPTY] : {self._list_email}')


    def setEmailList(self,email_dict):
        self._list_email = list(email_dict)