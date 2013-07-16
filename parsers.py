'''
abstracts how the data from aerospike is parsed in case of future changes.

all functions either return a dictionary or a generator of tuples (key, value)
for use by calling function.

aerospike in turn either returns a big string or dictionary.
'''
def _parse(delimiter=';'):
  '''
  internal routine to parse information and return as it is generated
  '''
  stats - raw.split(delimiter)
  for metric in stats:
    key, value = metric.split('=')
    yield (key, value)

def statistics(raw):
  #since statistics module returns a big a$$ string, return results
  #immediately (via a generator) as data gets parsed
  for k, v in _parse(raw):
    yield k, v

def namespace(raw):
  #returns results immediately (via a generator) as data gets parsed
  for k, v in _parse(raw):
    yield k, v
