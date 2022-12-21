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

		self.setWindowTitle(config.NAME_GUI)
		self.setGeometry(config.OFFSETX, config.OFFSETY, config.WIDTH, config.HEIGHT)

		self.button = QtWidgets.QPushButton(self)
		self.button.move(70, 150)
		self.button.setText('Push me~!')
		self.button.setFixedWidth(200)
		self.button.clicked.connect(self.clicked_button)

	def clicked_button(self):
		pass


def ui_create_app():
	pass


def create_app():
	app = QtWidgets.QApplication(sys.argv)
	name = Window()
	name.show()
	# print(Window.mro())  # rules entry
	sys.exit(app.exec_())


if __name__ == '__main__':
	create_app()


# pyuic5 -x .\main_window_1.ui -o .\main_window_1.py