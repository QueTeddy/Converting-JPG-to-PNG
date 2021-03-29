import sys
import os, shutil
from PIL import Image

#cwd = os.getcwd()

# print(cwd)

directory = 'Folderss'

p_directory = r"C:\Users\TeddyJR\Documents\Python Scripts\Script"

mode = 0o666
path = os.path.join(p_directory,directory)

os.mkdir(path,mode)

print(f'Directory {directory} is created')



x = []
for filename in os.listdir(r"C:\Users\TeddyJR\Documents\Python Scripts\Script"):
	if filename.endswith('.jpg'):
		x.append(filename)	

#print(x)
for i in x:
	converted = Image.open(i)
	converted.save(f'{i}.png','png')

for i in os.listdir(r"C:\Users\TeddyJR\Documents\Python Scripts\Script"):
	if i.endswith('.png'):
		shutil.move(i, r"C:\Users\TeddyJR\Documents\Python Scripts\Script\Folderss" )
