import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from PIL import Image
from psd_tools import PSDImage
from pathlib import Path



class example(QWidget):
	def __init__(self):
		super(example, self).__init__()
		self.setWindowTitle('拖拽获取文件路径')
		self.resize(500, 400)
		self.QLabl = QLabel(self)
		self.QLabl.setGeometry(0, 100, 4000, 38)
		self.setAcceptDrops(True)


	def dragEnterEvent(self, evn):
		self.setWindowTitle('鼠标拖入窗口了')
		self.QLabl.setText('文件路径：\n' + evn.mimeData().text())
		pp = evn.mimeData().text()

		newpp = pp.split('\n')
		print(type(newpp))
		for x in newpp:
			checkDoc(x[7:len(x)],'.psd')
			# print(x)
			# print("FFFFFFFFF")

		evn.accept()
		pass


	def dropEvent(self,evn):
		self.setWindowTitle('鼠标放开了')
		pass


	# def dragMoveEvent(self, evn):
	# 	print('鼠标移入')
	# 	pass


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
	psd = PSDImage.open(path)
	# merged_image = psd.as_PIL()
	psd.save(savePath)






if __name__ == '__main__':
	app = QApplication(sys.argv)
	e = example()
	e.show()
	sys.exit(app.exec_())


