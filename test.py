'''
Ideally a test library for Aerospike Analytics Collector.
Also shows how to call/use the core library module.
'''
from core import AerospikeAnalyticsCollector
import logging
import unittest

class TestAerospikeConnector(unittest.TestCase):

  def test__instantiation_and_retrieval():
    collector = AerospikeAnalyticsCollector()
    uptime_result = collector.statistics('uptime')
    err_result = collector.statistics('stat_read_errs_other')
    self.assertTrue('uptime' in uptime_result)
    self.assertTrue(type(uptime_result['uptime']) is float)
    self.assertTrue('stat_read_errs_other' in err_result)
    self.assertTrue(type(err_result['stat_read_errs_other']) is float)

  def test__non_delta_statistics():
    latency_result = collector.statistics('stat_read_latency_gt50', delta=False)
    latency_2_result = collector.statistics('stat_read_latency_gt50', delta=False)
    self.assertTrue('stat_read_latency_gt50' in latency_result)
    self.assertTrue(type(latency_result['stat_read_latency_gt50']) is float)
    self.assertTrue(latency_2_result['stat_read_latency_gt50'] is not None)

  def test__non_numeric_stats():
    lwm = collector.statistics('lwm-breached')
    self.assertTrue(lwm is not None)

if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG)
  unittest.main()
