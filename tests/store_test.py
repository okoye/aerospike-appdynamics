import sys
sys.path.append('../lib')
from a.wsgc.aerospike.store import PersistentStore
import logging
import unittest
import sqlite3

class TestPersistentStore(unittest.TestCase):

  def setUp(self):
    self.db_path = '/tmp/waldo.sqlite'
    self.c = sqlite3.connect(self.db_path)
    self.tname = 'spikey_metrics'

  def tearDown(self):
    self.c.execute('''DROP TABLE IF EXISTS (?)''',self.tname)

if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG)
  unittest.main()
