'''
Ideally a test library for Aerospike Analytics Collector.
Not really a unit test for functions.
Also shows how to call/use the core library module.
'''
from core import AerospikeAnalyticsCollector
import logging


def test__instantiation():
  collector = AerospikeAnalyticsCollector()
  collector.statistics('uptime')

def main():
  test__instantiation()

if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG)
  main()
