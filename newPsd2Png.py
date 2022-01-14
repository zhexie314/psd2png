import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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
		evn.accept()
		pass


	def dropEvent(self,evn):
		self.setWindowTitle('鼠标放开了')
		pass


	def dragMoveEvent(self, evn):
		print('鼠标移入')
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	e = example()
	e.show()
	sys.exit(app.exec_())


