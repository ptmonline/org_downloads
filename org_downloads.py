import shutil
import os
import unrar
import rarfile

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
	    #print new_folder
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


initScript();


        
