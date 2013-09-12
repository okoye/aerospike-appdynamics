#!/usr/bin/env python
from a.wsgc.aerospike.monitor import AerospikeAnalyticsConnector


PERFORMANCE_PREFIX = 'Performance'
UTILIZATION_PREFIX = 'Utilization'
OPERATIONAL_PREFIX = 'Operation'

def printer(name, value, prefix='Aerospike|Generic'):
  print '%s|%s, value=%s'%(prefix, name, value)

col = AerospikeAnalyticsConnector()
unknown_errors = col.statistics('stat_read_errs_other')
uptime = col.statistics('uptime')

printer(OPERATIONAL_PREFIX,'unknown_errors', unknown_errors)
printer(OPERATIONAL_PREFIX, 'cluster_uptime')
printer(OPERATIONAL_PREFIX, '')
