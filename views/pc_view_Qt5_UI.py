"""

This block created GUI for view information from postgres database.

Author: Kirto
version: zero
"""

from PyQt5 import QtWidgets
import variables as config
import sys


class Window(QtWidgets.QMainWindow):

	def __init__(self):

		super().__init__()

		self.setWindowTitle('Catalog')
		self.setGeometry(300, 250, 500, 500)

		self.main_text = QtWidgets.QLabel(self)
		self.main_text.setText('This is base label!')
		self.main_text.move(100, 240)  # move in window (relative coordinate)
		self.main_text.adjustSize()

		self.second_text = QtWidgets.QLabel(self)

		self.button = QtWidgets.QPushButton(self)
		self.button.move(70, 150)
		self.button.setText('Push me~!')
		self.button.setFixedWidth(200)
		self.button.clicked.connect(self.clicked_button)

	def clicked_button(self):
		self.second_text.setText('New label')
		self.second_text.move(100, 10)


def create_app():
	app = QtWidgets.QApplication(sys.argv)
	name = Window()
	name.show()
	# print(Window.mro())  # rules entry
	sys.exit(app.exec())


if __name__ == '__main__':
	create_app()
