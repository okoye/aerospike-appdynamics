'''
shared functions, primarily responsible for returning
an aerospike analytics collector object.

@author: Chuka
'''
import sys
import logging
import settings
import parsers
import exceptions
from socket import gethostname
try:
  import citrusleaf
except ImportError, ie:
  msg = 'Could not import Aerospike API client. Ensure it exists on pythonpath'
  logging.critical(msg)
  raise

class AerospikeAnalyticsCollector(object):
  '''
  AerospikeAnalyticsCollector abstracts some of the common requirements any set of
  custom monitors for AppDynamics must implement. It also hides some of the idiosyncracies
  of the data reported by Aerospike by providing a way to retrieve 'delta' changes since
  last poll.

  1.  delta:        A boolean value specifying whether only differences (delta changes) since
                    last poll should be returned to the client.
  
  This class implements the 'values' specified on the clinfo page
  https://docs.aerospike.com/display/AS2/Using+clinfo+to+Read+Parameters
  '''
  def __init__(self, *args, **kwargs):
    try:
      config_path = settings.LIB_DIR or kwargs.get('config', None)
    except ImportError, ie:
      msg = 'Could not import Aerospike API client. Not found in path: %s'%config_path
      logging.critical(msg)
      raise ImportError
    else:
      logging.debug('Aerospike client successfully imported')
    
    #assuming aerospike will always run locally.
    port = self.port = settings.PORT or 3000
    host = self.host = settings.HOST or gethostname()

    self.info = citrusleaf.citrusleaf_info #interface to aerospike monitor

    logging.debug('Finished instantiation of Aerospike information proxy')
    
  def statistics(self, name, delta=True):
    '''
    name: the statistic we are interested in. refer to:
          https://docs.aerospike.com/display/AS2/Statistics+Reference
          for a list of statistics
    '''
    key = 'statistics'
    #simply return the specified statistic
    #query underlying citrusleaf interface, parse results,
    #process parsed results and return relevant stat.
    result = self.info('localhost', self.port, key)

    #post processing steps:
    if not result:
      raise exceptions.AerospikeNoDataError(self.host, self.port, name)
    if result == -1:
      raise exceptions.AerospikeError(self.host, self.port, name)

  def namespace(self, name, delta=True):
    '''
    name: the name of the namespace caller is interested in
    '''
