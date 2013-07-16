'''
A clean set of exceptions this core library may throw
'''

class AerospikeBaseException(Exception):
  
  def __init__(self, host, port, stat):
    super(AerospikeBaseException, self).__init__()
    self.host = host
    self.port = port
    self.stat = stat
    self.context = 'a non-success code'

  @property
  def error(self):
    return 'command %s to %s:%s returned %s'%(self.stat,
                                              self.host,
                                              self.port,
                                              self.info)

class AerospikeNoDataError(AerospikeBaseException):
  
  def __init__(self, host, port, stat, **kwargs):
    super(NoDataError, self).__init__(host, port, stat)
    self.context = 'no data'

class AerospikeError(self, host, port, stat, **kwargs):
  
  def __init__(self, host, port, stat, **kwargs):
    super(AerospikeError, self).__init__(host, port, stat)
    self.context = 'error code -1'

