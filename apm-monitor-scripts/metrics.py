#!/usr/bin/env python
'''
sample script showing how to call aerospike appdynamics connector
library.

@author: Chuka
'''
from a.wsgc.aerospike.monitor import AerospikeAnalyticsConnector
from sys import stderr 
from datetime import datetime
import math

PERFORMANCE_PREFIX = 'Aerospike|NodePerformance'
RESOURCE_PREFIX = 'Aerospike|ResourceUtilization'
STATE_PREFIX = 'Aerospike|NodeState'

def printer(name, value, prefix='Aerospike|Generic', delta=False):
  print '%s|%s, value=%s'%(prefix, name, value)

#convinence logging function
log = lambda value: stderr.write('\t'.join([datetime.now().isoformat(), 
  value, 
  '\n']))
col = AerospikeAnalyticsConnector()

######### Cluster/Node State Monitors ########
#cluster size as seen by this node
cluster_size = col.statistics('cluster_size')
log('cluster_size is %s'%cluster_size.get('cluster_size', 0))
printer('ClusterSize', 
  cluster_size.get('cluster_size', 0), 
  prefix=STATE_PREFIX)

######## Performance Monitors #######
#TODO

####### Resource Utilization Monitors #######
#TODO
