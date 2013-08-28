import os
import sqlite3 as sqlite
import cPickle
from datetime import datetime

class KeyValueStore(object):
  
  def __init__(self, db_path):
    conn = self.conn = sqlite.connect(db_path) #fetch db cursor
    cursor = self.cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS spikey_metrics (key text, value blob, timestamp text)')

  def _encode_key(self, k):
    '''convert a key into python byte string'''
    byte_string = None
    try:
      byte_string = unicode(k)
    except UnicodeEncodeError:
      byte_string = unicode.decode(k).encode('unicode_escape')
    return byte_string

  def put(self, key, value):
    '''
    inserts a record with primary key 'key' and value 'value' into
    database
    '''
    #prepare for insertion
    pickled_data = sqlite.Binary(cPickle.dumps(value, cPickle.HIGHEST_PROTOCOL))
    timestamp = datetime.now().isoformat()
    sane_key = self._encode_key(key)

    #now, what can go wrong?
    self.cursor.execute('INSERT INTO spikey_metrics VALUES (?,?,?)',
                        (sane_key, pickled_data, unicode(timestamp)))
    self.conn.commit()

  def get(self, key):
    '''
    fetches the data associated with a particular key, assumes only
    single record operations. returns a tuple of value and timestamp
    '''
    sane_key = self._encode_key(key)
    self.cursor.execute('SELECT * FROM spikey_metrics WHERE key=?',(sane_key,))
    result = self.cursor.fetchone() #supports only single record ops
    if result is not None:
      r_key, r_value, r_time = result
      unpickled_data = cPickle.loads(str(r_value))
      return (unpickled_data, r_time)
    else:
      return None
