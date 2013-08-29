#!/usr/bin/env python26
'''
shared functions, primarily responsible for returning
an aerospike analytics collector object.

@author: Chuka
'''
import sys
import logging
from traceback import format_exc
from socket import gethostname
from a.wsgc.aerospike import exceptions as ce
from a.wsgc.aerospike import settings
from a.wsgc.aerospike import parsers
from a.wsgc.aerospike import store
try:
  import citrusleaf
except ImportError, ie:
  msg = 'Could not import Aerospike API client. Ensure it exists on pythonpath'
  logging.critical(msg)
  raise

class AerospikeAnalyticsConnector(object):
  '''
  AerospikeAnalyticsCollector abstracts some of the common requirements any set of
  custom monitors for AppDynamics must implement. It also hides some of the idiosyncracies
  of the data reported by Aerospike by providing a way to retrieve 'delta' changes since
  last poll.
  Relevant terminology:
  1.  delta:        A boolean value specifying whether only differences (delta changes) since
                    last poll should be returned to the client.
  
  This class implements the 'values' specified on the clinfo page
  https://docs.aerospike.com/display/AS2/Using+clinfo+to+Read+Parameters
  '''
  def __init__(self, *args, **kwargs):
    #assuming aerospike will always run locally.
    port = self.port = settings.PORT or 3000
    host = self.host = settings.HOST or gethostname()

    self.info = citrusleaf.citrusleaf_info #interface to aerospike monitor
    self.db = store.KeyValueStore(settings.DB_FILE)
    logging.debug('Finished instantiation of Aerospike information proxy')
    
  def statistics(self, name, delta=True):
    '''
    @param
      name: the statistic we are interested in. refer to:
            https://docs.aerospike.com/display/AS2/Statistics+Reference
            for a list of statistics
    @returns: a dict, with name as key, and statistic as value
    '''
    key = 'statistics'
    db_key = '%s:%s'%(key,name) 

    #query underlying citrusleaf interface, parse results,
    #process parsed results and return relevant stats.
    result = self.info('localhost', self.port, key)

    #post processing steps:
    if not result:
      raise ce.AerospikeNoDataError(self.host, self.port, name)
    if result == -1:
      raise ce.AerospikeError(self.host, self.port, name)
    
    stats = {}
    isnum = lambda x: type(x) is float or type(x) is int
    for k, v in parsers.statistics(result):
      if k == name:
        logging.debug('found data for statistic %s'%name)
        if delta:
          try:
            assert isnum(v)
          except ValueError, ve:
            raise ValueError('delta differences can only be computed for numeric values')
          else:
            stats[name] = self._delta(db_key, v)
        else:
          stats[name] = v
        continue #TODO: add support for multiple stats in one call
    return stats 

  def namespace(self, name, delta=True):
    '''
    @param
      name: the name of the namespace caller is interested in
    @returns: a dict, with namespace name as key, and statistic as value
    '''
    raise NotImplementedError

  def _delta(self, db_key, value):
    '''
    do a simple delta change calculation.
    '''
    previous = self.db.get(db_key)
    self.db.put(db_key, '%s'%value)
    print previous
    if previous:
      #hmm, is absolute difference more appropriate?
      return float(value) - float(previous)
    else:
      return value 
