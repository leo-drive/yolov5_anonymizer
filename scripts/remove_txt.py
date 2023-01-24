from os import listdir, rename, remove
from os.path import isfile, join
import shutil

folder_path = "./etiketlenecek/"
dest_path = "./silinecek/"

ext = 'jpg'

filenames = sorted([f[:-4] for f in listdir(folder_path) if isfile(join(folder_path, f)) and f[-3:] == ext])
all_files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

for f in filenames:
	if f + ".txt" not in all_files:
		print(f)
		shutil.move(folder_path + f + ".jpg", dest_path)