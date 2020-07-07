class PingParent():

    def __init__(self):
        '''
        This Class is the parent of Ping_Ip and Ping_Url, this was just to avoid
        repetative code. 
        '''
        self._ip = ''
        self._url = ''
        self._name = ''
        self._category = ''


    def getHost(self): pass


    def getName(self):
        return self._name


    def getCategory(self):
        return self._category


    def getStatus(self):
        return self._status

   
    def getDetails(self): pass