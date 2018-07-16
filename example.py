# http://chriskiehl.com/article/parallelism-in-one-line/

#import urllib2
from urllib.request import urlopen
#from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool 
import time

urls = [
  'http://www.python.org', 
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  'http://planet.python.org/',
  'https://wiki.python.org/moin/LocalUserGroups',
  'http://www.python.org/psf/',
  'http://docs.python.org/devguide/',
  'http://www.python.org/community/awards/'
  # etc.. 
  ]

lines=[] # create an empty list of files
with open('docs', 'r', encoding='ISO 8859-1') as file: # then read the list from a file into memory
    lines=[line.strip() for line in file]

def file_len(fname):
    i=0
    with open(fname, 'r', encoding='ISO 8859-1') as f:
        for i, l in enumerate(f):
             pass
    return i + 1

def fname(fname):
    #time.sleep(0.1)
    return fname


if __name__ == '__main__':
    # Make the Pool of workers
    pools=4
    for i in range(0,8):
        pools=2**i
        start=time.time()
        pool = ThreadPool(pools) 
        # Open the urls in their own threads
        # and return the results
        #result = pool.map(file_len, lines)
        result = pool.map(urlopen, urls)
        #close the pool and wait for the work to finish 
        pool.close() 
        pool.join() 
        end=time.time()
        print('pools: {} time: {}'.format(pools,end-start))