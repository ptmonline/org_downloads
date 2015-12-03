import shutil
import os
import unrar
import rarfile
import zipfile
import sys
import argparse

parser = argparse.ArgumentParser(description='This is my help')

args = parser.parse_args()
'''
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print 'Argument interesting is: ' , str(sys.argv[1])
if str(sys.argv[1]) == 'hello':
    print 'yes it is hello'
elif str(sys.argv[1]) == 'goodbye':
    print 'also yes it says goodbye!'
else:
    print 'not a single word'
'''
if not os.path.exists('../../../tmp_torrents/'):
    os.mkdir('../../../tmp_torrents')
elif not os.path.exists('../../txt_files/'):
    os.mkdir('../../txt_files')

def org_rar(files, new_folder):
    os.makedirs(new_folder)
    destination = os.getcwd() +'/'+ str(new_folder)+'/'
    shutil.move(files,destination)
    new_id = new_folder + '/' + files
    rf = rarfile.RarFile(new_id)
    rf.extractall(new_folder);
    shutil.move(new_folder, '../../../Music/')

def initScript():
    source=os.listdir(os.getcwd())
    for files in source:
	if files.endswith(".rar"):
	    print 'files found'
	    print files
	    new_folder = files[:-4]
            org_rar(files, new_folder)
        elif files.endswith('.txt'):
            shutil.move(files,'../../txt_files/')
            print 'moved ' + files + ' into Documents/txt_files'
        elif files.endswith('.mp4'):
            shutil.move(files, '../../../Videos/')
            print 'moved ' + files + ' into Videos folder'
        elif files.endswith('.torrent'):
            shutil.move(files, '../../../tmp_torrents/')
            print 'moved ' + files + ' into tmp_torrent folder'
        elif files.endswith('.zip'):
            zfile = zipfile.ZipFile(files)
            for name in zfile.namelist():
                (dirname, filename) = os.path.split(name)
                print "Decompressing " + filename + " on " + dirname
                if not os.path.exists(dirname):
                    os.makedirs(dirname)
                zfile.extract(name, dirname)
            shutil.copy(files, dirname)

initScript();


        
