from ping.ping_ip import Ping_Ip
from ping.ping_url import Ping_Url
from utility.notification import Notification
import threading
import yaml

class mStatus:
    DATA = {}
    TIME = 600
    EMAILS = {}

    def __init__(self,file_path):
        '''
        This Class uses Ping_Url and Ping_Ip class to ping
        the ip address and get the status, if the ip or url is down,
        the notification class will send an email if email(s) were
        specified in the config.yaml file. 
        '''
        print('[Ping Configuration yaml is] : ', file_path)
        if self.read_yaml(file_path):
            self.notify = Notification()
            self.notify.setEmailList(self.EMAILS)
            self.start()


    def start(self):
        self.thread = threading.Timer(self.getTime(),self.start)
        self.thread.start()
        
        print(f'[THREADS ACTIVE] : {threading.active_count()}')
        for data in self.DATA:
            d = self.DATA[data]
            if d['type'] == 'ip':
                self.checkIP(d['value'],d['name'],d['category'])
            if d['type'] == 'url':
                self.checkURL(d['value'],d['name'],d['category'])
        print('[END] \n')


    def checkIP(self,IP_ADDRESS,NAME,CATEGORY):
        ip = Ping_Ip(IP_ADDRESS,NAME,CATEGORY)
        ip.ping()
        print(f'[STATUS] {ip.getStatus()}')
        self.notify.check(ip)


    def checkURL(self,URL_ADDRESS,NAME,CATEGORY):
        url = Ping_Url(URL_ADDRESS,NAME,CATEGORY)
        url.ping()
        print(f'[STATUS] {url.getStatus()}')
        self.notify.check(url)

    def read_yaml(self,filepath):
        with open(filepath, 'r') as stream:
            try:
                all_data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return False

        for email in all_data['email']:
            self.EMAILS.update({email:email})
        
        self.TIME = all_data['interval']

        all_data.pop('email')
        all_data.pop('interval')
        self.DATA = all_data

        return True


    def getTime(self):
        return int(self.TIME)