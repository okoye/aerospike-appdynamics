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

class AerospikeNoData(AerospikeBaseException):
  
  def __init__(self, host, port, stat, **kwargs):
    super(AerospikeNoData, self).__init__(host, port, stat)
    self.context = 'no data'

class AerospikeError(AerospikeBaseException):
  
  def __init__(self, host, port, stat, **kwargs):
    super(AerospikeError, self).__init__(host, port, stat)
    self.context = 'error code -1'

class AerospikeNoSuchStat(AerospikeBaseException):
  
  def __init__(self, host, port, stat, **kwargs):
    super(AerospikeNoSuchStat, self).__init__(host, port, stat)
    self.context = 'no such statistic'

class LibraryInternalError(Exception):
  
  def __init__(self, msg, traceback,**kwargs):
    super(LibraryInternalError, self).__init__()
    if not msg:
      self.msg = 'An internal problem was encountered'
    else:
      self.msg = msg
    self.tb = traceback

