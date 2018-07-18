# https://stackoverflow.com/questions/13161659/how-can-i-call-robocopy-within-a-python-script-to-bulk-copy-multiple-folders

from subprocess import call
import os
from time import time

def python_robocopy (dirpath, logname):
    log='/log:{}'.format(logname) # create a logfile string from the name to pass into robocopy call
    call(['robocopy', dirpath, '%tmp%', '/l', '/s', '/bytes', '/ts', '/nc', '/ndl', '/njs', '/njh', log])
    print('pyrobo done....')
    with open(logname) as file:
        result=file.read()
        result=result.replace('\n\t  \t\t','')
    os.remove(logname)
    return result



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


if __name__ == '__main__':

    start=time()
    root=r'\\teeis1008\Santry'
    #plist=genpathlist(root)
    #print(plist)
    #python_robocopy(r'C:\Users\121988\documents', 'localdocs_1')
    #python_robocopy(dirlist[1], 'archive')
    result = python_robocopy(r'\\teeis1008\Santry\samba-linux', 'test_1')
    end=time()
    #print(result)
    print('time:' , end-start)
