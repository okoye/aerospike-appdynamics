'''
responsible for parsing raw results returned by aerospike
all functions either return a dictionary or a generator of tuples (key, value)
for use by calling function.
'''
def statistics(raw):
  #parse and return all values.
  stats = raw.split(';')
  for value in stats:
    print value.split('=')
