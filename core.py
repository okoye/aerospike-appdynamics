'''
shared functions, primarily responsible for returning
an aerospike analytics collector object.

@author: Chuka
'''
import sys
import logging
import settings
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

  Some relevant terms you should be familiar with to use this class are:

  1.  policy: how should this analytics collector act. possible values are:
        dumbpipe:   relay results from the Aerospike API straight to caller
        aggregate:  tally total aggregate of result and send to caller. e.g latency is
                    reported in 1ms, 8ms, 10ms intervals, so aggregate sums all values
                    and reports as single statistic.
        specific:   return a specific value from the statistic requested. e.g continuing 
                    with the latency example, you could set policy as specific and will be
                    required to provide a value to specific_key for the value you want.
  2.  specific_key: represents the specific key from a statistic we are interested in.
                    should be accompanied with the specific policy setting.
  3.  delta:        A boolean value specifying whether only differences (delta changes) since
                    last poll should be returned to the client.
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

    self.info = citrusleaf.citrusleaf_info 
    logging.debug('Finished instantiation of Aerospike information proxy')
    
  def nodestatistic(self, name, policy=''):
    '''
    returns the total number of requests 
    '''
    key = 'statistics/'

  def throughput(self):
    pass
