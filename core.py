'''
shared functions, primarily responsible for returning
an aerospike analytics collector object.
'''
import sys
import logging
import settings
from socket import gethostname

class AerospikeAnalyticsCollector(object):
  
  def __init__(self, *args, **kwargs):
    try:
      config_path = settings.LIB_DIR or kwargs.get('config', None)
      self._import_aerospike_lib(config_path)
    except ImportError, ie:
      msg = 'Could not import Aerospike API client. Not found in path: %s'%config_path
      logging.critical(msg)
      raise ImportError
    else:
      logging.debug('Aerospike client successfully imported')
    
    #assuming aerospike will always run locally.
    self.port = settings.PORT or 3000
    self.host = settings.HOST or gethostname()

  def _import_aerospike_lib(self, path):
    if not path in sys.path:
      logging.debug('Adding %s to sys.path'%path)
      sys.path.append(path)

      try:
        import citrusleaf
        import python_citrusleaf
      except Exception as ex:
        raise ImportError()

