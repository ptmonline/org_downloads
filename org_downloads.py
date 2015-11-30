import shutil
import os
import unrar
import rarfile

def org_rar(files, new_folder):
    os.makedirs(new_folder)
    destination = os.getcwd() +'/'+ str(new_folder)+'/'
    shutil.copy(files,destination)
    new_id = new_folder + '/' + files
    rf = rarfile.RarFile(new_id)
    rf.extractall(new_folder);
    shutil.move(new_folder, 'rar_files')

def initScript():
    source=os.listdir(os.getcwd())
    for files in source:
	if files.endswith(".rar"):
	    print 'files found'
	    print files
	    new_folder = files[:-4]
	    print new_folder
            org_rar(files, new_folder)
        elif files.endswith('.txt'):
            destination = os.getcwd()+'/txt_files/'
            shutil.move(files,'txt_files')

if not os.path.exists('rar_files'):
    os.mkdir('rar_files')
elif not os.path.exists('txt_files'):
    os.mkdir('txt_files')

initScript();


        
