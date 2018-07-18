# http://chriskiehl.com/article/parallelism-in-one-line/

#import urllib2
from urllib.request import urlopen
from multiprocessing import Pool as ThreadPool
#from multiprocessing.dummy import Pool as ThreadPool 
import time
import urls

nline=0 
# %userprofile%\AppData\Local\Microsoft\Windows\History


lines=[] # create an empty list of files
with open('datalogs', 'r', encoding='ISO 8859-1') as file: # then read the list from a file into memory
    lines=[line.strip() for line in file]

def file_len(fname):
    global nline
    nline = nline + 1
    i=0
    with open(fname, 'r', encoding='ISO 8859-1') as f:
        for line_num, line in enumerate(f):
             pass
    #return nline, line_num + 1
    return nline

def fname(fname):
    #time.sleep(0.1)
    #print(fname)
    return fname

def myurlopen(urlname):
    global nline
    lnine=nline+1
    #print('{} {}'.format(line,urlname))
    #dat=urlopen(urlname)
    #time.sleep(0.1)
    return urlname

if __name__ == '__main__':
    # Make the Pool of workers
    
    pools=4
    for i in range(0,7): #for i in range(2,3):
        nline=0
        #i=0
        pools=2**i
        start=time.time()
        pool = ThreadPool(pools) 
        # Open the urls in their own threads
        # and return the results
        #result = pool.map(fname, lines)
        result = pool.map(file_len, lines)
        #result = pool.map(myurlopen, urls)
        #close the pool and wait for the work to finish 
        pool.close() 
        pool.join() 
        end=time.time()
        #print(result)
        print('pools: {} time: {}'.format(pools,end-start))
        