# https://stackoverflow.com/questions/13161659/how-can-i-call-robocopy-within-a-python-script-to-bulk-copy-multiple-folders

from subprocess import call
import subprocess
import os
from time import time
#from multiprocessing import Pool as ThreadPool
from multiprocessing.dummy import Pool as ThreadPool 

def genpathlist(fromroot):
    pathlist=[]
    with os.scandir(fromroot) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():
                dpath='{}\{}'.format(fromroot,entry.name)
                #print(dpath)
                pathlist.append(dpath)
                try: 
                    with os.scandir(dpath) as it2:
                        for ent2 in it2:
                            if not ent2.name.startswith('.') and ent2.is_dir():
                                #print('{}\{}'.format(dpath,ent2.name))
                                pathlist.append('{}\{}'.format(dpath,ent2.name))
                except PermissionError:
                    pathlist.pop() # if there was a permission error drop the last entry from the list
                    #print('Access denied...')
        return pathlist

#def python_robocopy (dirpath, logname):
def python_robocopy (dirpath):
    filelist=[]
    process = subprocess.Popen(['robocopy', dirpath, '%tmp%', '/l', '/s', '/bytes', '/ts', '/nc', '/ndl', '/njs', '/njh', '/min:1'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    out=out.replace(b'\t  \t\t', b'')
    out=out.replace(b'\r\n', b'\n')
    out=out.replace(b'\n\n', b'\n')
    out=out.decode(encoding='ISO 8859-1')
    out=out.splitlines()#.decode(encoding='ISO 8859-1')
    for line in out:
        if len(line)>10:
            filelist.append(line)
    return filelist

def flattenlist(sublist):
    flatlist=[]
    for i in range(len(sublist)):
        flatlist+=sublist[i]
    return flatlist


if __name__ == '__main__':

    #root=r'\\teeis1008\Santry\Operations'
    root=r'\\teeis1008\Santry'
    
    start=time()
    print('\n\tparallel processing commenced {} ......\n'.format(start-start))
    dirlist=genpathlist(root)
    poolnum=32
    pool = ThreadPool(poolnum) # create parellel execution pools
    dlist = pool.map(python_robocopy, dirlist) # launch the tasks
    pool.close() 
    pool.join()
    pool.terminate()
    end=time()
    
    print('\tpools: {} \n\tendtime: {}'.format(poolnum, end-start))
    print('\tsublists: {}\n'.format(len(dlist)))
    print('\tflatten the list.. ',time()-start)
    
    flatlist=flattenlist(dlist)
    print('\twrite to file.. ',time()-start)
    with open('teeis1008_20180720', 'w', encoding='ISO 8859-1')as outfile:
        for line in flatlist:
            outfile.write('{}\n'.format(line))
    print('\tprocessing completed ... \n\n',time()-start)

    