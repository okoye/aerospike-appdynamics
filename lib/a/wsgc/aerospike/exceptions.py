'''
A clean set of exceptions this core library may throw
'''
class AerospikeBaseException(Exception):
  
  #NOTE: normally, we would set all the object properties
  #       like self.host, self.port in this base class
  #       alas, Exception class for python 2.x is an old
  #       style class and does not support super() magic bullet!

  @property
  def error(self):
    return 'command %s to %s:%s returned %s'%(self.stat,
                                              self.host,
                                              self.port,
                                              self.info)

class AerospikeNoData(AerospikeBaseException):
  
  def __init__(self, host, port, stat, **kwargs):
    self.host = host
    self.port = port
    self.stat = stat
    self.context = 'no data'

class AerospikeError(AerospikeBaseException):
  
  def __init__(self, host, port, stat, **kwargs):
    self.host = host
    self.port = port
    self.stat = stat
    self.context = 'error code -1'
  
  def __str__(self):
    return '%s:%s => %s'(self.host, self.port, self.context)

class AerospikeNoSuchStat(AerospikeBaseException):
  
  def __init__(self, host, port, stat, **kwargs):
    self.host = host
    self.port = port
    self.stat = stat
    self.context = 'no such statistic'

class LibraryInternalError(Exception):
  
  def __init__(self, msg, traceback,**kwargs):
    if not msg:
      self.msg = 'An internal problem was encountered'
    else:
      self.msg = msg
    self.tb = traceback

