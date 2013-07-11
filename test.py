'''
Ideally a test library for Aerospike Analytics Collector.
Not really a unit test for functions.
'''
from core import AerospikeAnalyticsCollector



def test__instantiation():
  collector = AerospikeAnalyticsCollector('nothing')

def main():
  test__instantiation()

if __name__ == '__main__':
  main()
