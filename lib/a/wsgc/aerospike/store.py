import pickle
import sql

class PersistentStore(object):
  
  def __init__(self, db_path):
    self.db = db_path

  def _exists(self):
    pass

  def put(self, key, value):
    pass

  def get(self, key):
    pass
