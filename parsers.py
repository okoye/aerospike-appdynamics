'''
abstracts how the data from aerospike is parsed in case of future changes.

all functions either return a dictionary or a generator of tuples (key, value)
for use by calling function.

aerospike in turn either returns a big string or dictionary.
'''
def statistics(raw):
  #since statistics module returns a big a$$ string, return results
  #immediately (via a generator) as data gets parsed
  stats = raw.split(';')
  for metric in stats:
    key, value = metric.split('=')
    yield (key, value)

def namespace(raw):
  #
