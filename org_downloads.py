import shutil
import os
import unrar
import rarfile

source=os.listdir(os.getcwd())
for files in source:
#	print files
	if files.endswith(".rar"):
		print 'files found'
		print files
		new_folder = files[:-4]
		print new_folder
		if not os.path.exists(new_folder):
			destination = os.makedirs(new_folder)
			destination2 = os.getcwd() +'/'+ str(new_folder)+'/'
			shutil.move(files,destination2)
		new_id = new_folder + '/' + files
		rf = rarfile.RarFile(new_id)
		rf.extractall(new_folder);
