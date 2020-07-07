from ping.ping_parent import PingParent
import platform    # For getting the operating system name
from subprocess import PIPE, run  # For executing a shell command
from re import search as re_search

class Ping_Ip(PingParent):

    def __init__(self,IP='',NAME='',CATEGORY=''):
        '''
        This Class uses uses the subprocess module to ping ip addresses
        and returns the status. 
        '''
        super().__init__()
        if IP == '' or NAME == '' or CATEGORY == '':
            raise Exception('Please enter a valid IP,Category and Name')   
        self._name = NAME
        self._ip = IP
        self._category = CATEGORY


    def ping(self):
        opSys = platform.system().lower()
        
        if opSys == 'windows':
            param = '-n'
        else:
            param = '-c'

        command = ['ping', param, '1', self.getHost()]

        result = run(command, stdout=PIPE, stderr=PIPE, stdin=PIPE, universal_newlines=True)

        self.result_output = str(result.stdout)

        try:
            if opSys == 'linux':
                reply_ip = re_search('bytes from (.*):', self.result_output).group(1)
            else:
                reply_ip = re_search('Reply from (.*):', self.result_output).group(1)
        except AttributeError:
            reply_ip = 0
        

        if str(reply_ip) == str(self.getHost()):
            self._status = True
            return self.result_output
        else:
            self._status = False

        return False


    def getDetails(self):
        return self.result_output


    def getHost(self):
        return self._ip
