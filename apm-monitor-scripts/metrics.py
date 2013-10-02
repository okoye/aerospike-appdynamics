#!/usr/bin/env python
from a.wsgc.aerospike.monitor import AerospikeAnalyticsConnector
import math

PERFORMANCE_PREFIX = 'Performance'
UTILIZATION_PREFIX = 'Utilization'
OPERATIONAL_PREFIX = 'Operation'

def printer(name, value, prefix='Aerospike|Generic'):
  print '%s|%s, value=%s'%(prefix, name, value)

col = AerospikeAnalyticsConnector()

######  Unknown Errors  ###########
unknown_errors = col.statistics('stat_read_errs_other')
unknown_erros = len(unknown_errors) #TODO: delta changes.


##### Uptime  ###################
uptime = math.fabs(col.statistics('uptime'))


####  Cluster Size #############
cluster_size = col.statistics('cluster_size').get()





#printer(OPERATIONAL_PREFIX,'unknown_errors', unknown_errors)
#printer(OPERATIONAL_PREFIX, 'cluster_uptime')
#printer(OPERATIONAL_PREFIX, 'stat_read_reqs')
