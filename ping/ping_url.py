from ping.ping_parent import PingParent
import requests
import re


class Ping_Url(PingParent):
    
    def __init__(self,URL='',NAME='',CATEGORY=''):
        '''
        This Class uses uses the requests module to check the status
        of any website. 
        '''
        super().__init__()
        if URL == '' or NAME == '' or CATEGORY == '':
            raise Exception('Please enter a valid URL,Category and Name')   
        self._name = NAME
        self._url = URL
        self._category = CATEGORY


    def ping(self):
        self.input_data = self.getHost()
        try:
            self.response = requests.get(self.input_data)
            self.status_code = int(self.response.status_code)
            if self.response.ok:
                self._status = True
                return self.status_code
            else:
                self._status = False
        except Exception as e:
            self.status_code = e
            self._status = False

        return False


    def getDetails(self):
        return f'The response we got was : {self.status_code}'


    def getHost(self):
        return self._url