import os
import cPickle
import sqlite3
from datetime import datetime

class PersistentStore(object):
  
  def __init__(self, db_path):
    self.cursor = sqlite3.connect(db_path) #fetch db cursor
    self.table_name = 'spikey_metrics'
    
  def _create(self):
    self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS (?) (key text, value blob, timestamp text)
    ''', self.table_name)
  
  def _encode_key(self, k):
    '''convert a key into python byte string'''
    byte_string = None
    try:
      byte_string = str(k)
    except UnicodeEncodeError:
      byte_string = unicode.decode(k).encode('unicode_escape')
    finally:
      return byte_string

  def put(self, key, value):
    '''
    inserts a record with primary key 'key' and value 'value' into
    database
    '''
    #prepare for insertion
    pickled_data = cPickle.dumps(value, cPickle.HIGHEST_PROTOCOL)
    timestamp = datetime.now().isoformat()
    sane_key = self._encode_key(key)

    #now, what can go wrong?
    self.cursor.execute('''INSERT INTO (?) VALUES (?,?,?)''',
                        self.table_name, sane_key, pickled_data, timestamp)
    self.cursor.commit()

  def get(self, key):
    '''
    fetches the data associated with a particular key, assumes only
    single record operations. returns a tuple of value and timestamp
    '''
    sane_key = self._encode_key(key)
    self.cursor.execute('''SELECT * FROM (?) WHERE key=?''',
                        self.table_name, sane_key)
    r_key, r_value, r_time = self.cursor.fetchone() #single record operations
    unpicked_data = cPickle.loads(r_value)
    return (unpickled_data, r_time)
