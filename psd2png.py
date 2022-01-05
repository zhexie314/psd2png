from PIL import Image
from psd_tools import PSDImage
from pathlib import Path
from TkinterDnD2 import *
from tkinter import *


def drop(event):
	entry_sv.set('Doing')
	ss = event.data
	newStr = ss.split(' ')
	for i in newStr:
		checkDoc(i,'.psd')
	entry_sv.set('Finish')


def checkDoc(path_dir,file_type):
	currPath = Path(path_dir)
	if currPath.is_file():
		if currPath.suffix == file_type:
			savePath = findSavePath(currPath,'.png')
			psd2png(currPath,savePath)
			return
	if currPath.is_dir():
		for file_path in currPath.glob('**/*.psd'):
			savePath = findSavePath(file_path,'.png')
			psd2png(file_path,savePath)
		return

def findSavePath(file_path,file_type):
	return(str(file_path.parent / file_path.stem) + file_type)



def psd2png(path,savePath):
	psd = PSDImage.load(path)
	merged_image = psd.as_PIL()
	merged_image.save(savePath)




root = TkinterDnD.Tk()
root.minsize(width=200, height=200)
root.maxsize(width=400, height=400)
entry_sv = StringVar()
entry_sv.set('Drop Your PSDfile or Folder Here...')
entry = Label(root, textvar=entry_sv, width=80,height=150 ,relief='sunken')
entry.pack(fill=X, padx=10, pady=10)
entry.drop_target_register(DND_FILES)
entry.dnd_bind('<<Drop>>', drop)
root.mainloop()


