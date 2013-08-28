import sys
sys.path.append('../lib')
from a.wsgc.aerospike.store import KeyValueStore
import sqlite3 as sqlite
import cPickle
import logging
import unittest
from datetime import datetime
try:
  import sqlite3
except ImportError:
  import pysqlite2 as sqlite3

class TestPersistentStore(unittest.TestCase):

  def setUp(self):
    self.db_path = '/tmp/waldo.sqlite'
    self.c = sqlite.connect(self.db_path)
    self.cur = self.c.cursor()
    self.kv = KeyValueStore(self.db_path)
    
  def tearDown(self):
    self.cur.execute('DROP TABLE IF EXISTS spikey_metrics')
  
  def _put(self, k, v):
    self.cur.execute('INSERT INTO spikey_metrics VALUES (?,?,?)',
                    (unicode(k),
                    sqlite.Binary(cPickle.dumps(v, cPickle.HIGHEST_PROTOCOL)),
                    unicode(datetime.now().isoformat())))
    self.c.commit()

  def _get(self, k):
    self.cur.execute('SELECT * FROM spikey_metrics WHERE key=?', (unicode(k),)) 
    result = self.cur.fetchone()
    if result is not None:
      return cPickle.loads(str(result[1]))
    return None

  def test_get(self):
    #first test 'normal' procedure
    result = self.kv.get('chuka')
    self.assertEquals(result, None)
    
    #now, insert different types values
    self._put('rawwr', 'lion')
    result, timestamp = self.kv.get('rawwr')
    self.assertEquals(result, 'lion')
    
    self._put('2+2', 5)
    result, timestamp = self.kv.get('2+2')
    self.assertEquals(result, 5)

    self._put(2, 'prime')
    result, timestamp = self.kv.get(2)
    self.assertEquals(result, 'prime')

    self._put(unicode('found'), 'waldo')
    result, timestamp = self.kv.get('found')
    self.assertEquals(result, 'waldo')
    result, timestamp = self.kv.get(unicode('found'))
    self.assertEquals(result, 'waldo')

  def test_put(self):
    lang_dict = {'clojure': 'rocks',
                  'python': 'okay',
                  'java': 'meh'}
    self.kv.put('waldo', 'missing')
    self.kv.put(3, '65')
    self.kv.put('languages', lang_dict)
    result = self._get(3)
    self.assertEquals(result, '65')
    result = self._get('waldo')
    self.assertEquals(result, 'missing')
    result = self._get('languages')
    self.assertEquals(result, lang_dict)

if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG)
  unittest.main()
