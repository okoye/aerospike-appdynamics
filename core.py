'''
shared functions, primarily responsible for returning
an aerospike analytics collector object.
'''
import logging
import settings

class AerospikeAnalyticsCollector(object):
  
  def __init__(self, config_path, **kwargs):
    try:
      self._import_aerospike_lib(config_path)
    except ImportError as ie:
      msg = 'Could not import Aerospike API client. Not found in path: %s'%config_path
      logging.critical(msg)
      raise ImportError
    else:
      logging.debug('Aerospike client successfully imported')

  def _import_aerospike(self, path):
    pass
