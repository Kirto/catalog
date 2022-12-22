"""

This block created GUI for view information from postgres database.

Author: Kirto
version: zero
"""

from PyQt5 import QtCore, QtGui, QtWidgets
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


class UiMainWindow(object):
	def __init__(self):
		super(UiMainWindow, self).__init__()

	# Main settings
	def setup_ui(self, MainWindow):
		MainWindow.setObjectName(config.NAME_GUI)
		MainWindow.resize(config.WIDTH_MAIN, config.HEIGHT_MAIN)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(config.PNG_ICO_PATH), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)

		self.main_wrapper = QtWidgets.QWidget(MainWindow)
		self.main_wrapper.setObjectName("main_wrapper")
		self.select_tab_panel = QtWidgets.QTabWidget(self.main_wrapper)
		self.select_tab_panel.setEnabled(True)
		self.select_tab_panel.setGeometry(QtCore.QRect(0, 0, 1071, 711))
		self.select_tab_panel.setObjectName("select_tab_panel")
		self.main_tab = QtWidgets.QWidget()
		self.main_tab.setObjectName("main_tab")
		self.result_combo_box = QtWidgets.QGroupBox(self.main_tab)
		self.result_combo_box.setGeometry(QtCore.QRect(0, 100, 1061, 461))
		self.result_combo_box.setObjectName("result_combo_box")
		self.result_list_view = QtWidgets.QListView(self.result_combo_box)
		self.result_list_view.setGeometry(QtCore.QRect(10, 30, 1041, 421))
		self.result_list_view.setObjectName("result_list_view")
		self.search_combo_box = QtWidgets.QGroupBox(self.main_tab)
		self.search_combo_box.setGeometry(QtCore.QRect(10, 10, 1051, 81))
		self.search_combo_box.setObjectName("search_combo_box")
		self.horizontalLayoutWidget = QtWidgets.QWidget(self.search_combo_box)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1031, 61))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.search_text = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
		self.search_text.setObjectName("search_text")
		self.horizontalLayout.addWidget(self.search_text)
		self.search_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.search_button.setObjectName("search_button")
		self.horizontalLayout.addWidget(self.search_button)
		self.commands_combo_box = QtWidgets.QGroupBox(self.main_tab)
		self.commands_combo_box.setGeometry(QtCore.QRect(0, 570, 1061, 101))
		self.commands_combo_box.setObjectName("commands_combo_box")
		self.gridLayoutWidget = QtWidgets.QWidget(self.commands_combo_box)
		self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1041, 71))
		self.gridLayoutWidget.setObjectName("gridLayoutWidget")
		self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setContentsMargins(10, 0, 10, 0)
		self.gridLayout.setObjectName("gridLayout")
		self.command_undo_button = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.command_undo_button.setObjectName("command_undo_button")
		self.gridLayout.addWidget(self.command_undo_button, 0, 2, 1, 1)
		self.command_save_button = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.command_save_button.setObjectName("command_save_button")
		self.gridLayout.addWidget(self.command_save_button, 0, 1, 1, 1)
		self.command_change_button = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.command_change_button.setObjectName("command_change_button")
		self.gridLayout.addWidget(self.command_change_button, 0, 0, 1, 1)
		self.command_exit_button = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.command_exit_button.setObjectName("command_exit_button")
		self.gridLayout.addWidget(self.command_exit_button, 0, 3, 1, 1)
		self.select_tab_panel.addTab(self.main_tab, "")
		self.settings_tab = QtWidgets.QWidget()
		self.settings_tab.setObjectName("settings_tab")
		self.select_tab_panel.addTab(self.settings_tab, "")
		MainWindow.setCentralWidget(self.main_wrapper)
		self.menu_bar = QtWidgets.QMenuBar(MainWindow)
		self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1070, 26))
		self.menu_bar.setObjectName("menu_bar")
		self.menu_file = QtWidgets.QMenu(self.menu_bar)
		self.menu_file.setObjectName("menu_file")
		self.menu_file_export_to = QtWidgets.QMenu(self.menu_file)
		self.menu_file_export_to.setObjectName("menu_file_export_to")
		self.menu_about = QtWidgets.QMenu(self.menu_bar)
		self.menu_about.setObjectName("menu_about")
		MainWindow.setMenuBar(self.menu_bar)
		self.status_bar = QtWidgets.QStatusBar(MainWindow)
		self.status_bar.setObjectName("status_bar")
		MainWindow.setStatusBar(self.status_bar)
		self.menu_file_connect = QtWidgets.QAction(MainWindow)
		self.menu_file_connect.setObjectName("menu_file_connect")
		self.action = QtWidgets.QAction(MainWindow)
		self.action.setCheckable(False)
		self.action.setEnabled(False)
		self.action.setObjectName("action")
		self.menu_file_exit = QtWidgets.QAction(MainWindow)
		self.menu_file_exit.setObjectName("menu_file_exit")
		self.menu_about_help = QtWidgets.QAction(MainWindow)
		self.menu_about_help.setObjectName("menu_about_help")
		self.menu_file_export_to_svc = QtWidgets.QAction(MainWindow)
		self.menu_file_export_to_svc.setObjectName("menu_file_export_to_svc")
		self.menu_file_export_to.addAction(self.menu_file_export_to_svc)
		self.menu_file.addAction(self.menu_file_connect)
		self.menu_file.addAction(self.menu_file_export_to.menuAction())
		self.menu_file.addSeparator()
		self.menu_file.addAction(self.menu_file_exit)
		self.menu_about.addAction(self.menu_about_help)
		self.menu_bar.addAction(self.menu_file.menuAction())
		self.menu_bar.addAction(self.menu_about.menuAction())

		self.retranslate_ui(MainWindow)
		self.select_tab_panel.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	# Titles
	def retranslate_ui(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.result_combo_box.setTitle(_translate("MainWindow", "Результат"))
		self.search_combo_box.setTitle(_translate("MainWindow", "Поиск по имени или ОЗМ"))
		self.search_button.setText(_translate("MainWindow", "Поиск ..."))
		self.commands_combo_box.setTitle(_translate("MainWindow", "Управление"))
		self.command_undo_button.setText(_translate("MainWindow", "Отменить"))
		self.command_save_button.setText(_translate("MainWindow", "Сохранить"))
		self.command_change_button.setText(_translate("MainWindow", "Изменить"))
		self.command_exit_button.setText(_translate("MainWindow", "Выйти"))
		self.select_tab_panel.setTabText(self.select_tab_panel.indexOf(self.main_tab),
										 _translate("MainWindow", "Основная часть"))
		self.select_tab_panel.setTabText(self.select_tab_panel.indexOf(self.settings_tab),
										 _translate("MainWindow", "Настройки"))
		self.menu_file.setTitle(_translate("MainWindow", "Файл"))
		self.menu_file_export_to.setTitle(_translate("MainWindow", "Export ..."))
		self.menu_about.setTitle(_translate("MainWindow", "О программе"))
		self.menu_file_connect.setText(_translate("MainWindow", "Connect ..."))
		self.action.setText(_translate("MainWindow", "-------------------"))
		self.menu_file_exit.setText(_translate("MainWindow", "Exit ...."))
		self.menu_about_help.setText(_translate("MainWindow", "Help ..."))
		self.menu_file_export_to_svc.setText(_translate("MainWindow", "to *.svc ...."))


class UiFormChangingParametersInDb(object):

	def __init__(self):
		super(UiFormChangingParametersInDb, self).__init__()

	def setup_ui(self, form_changing_parameters_in_db):
		form_changing_parameters_in_db.setObjectName(config.NAME_GUI_CHANGE_ITEM)
		form_changing_parameters_in_db.resize(config.WIDTH_CHANGE, config.HEIGHT_CHANGE)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(config.PNG_ICO_PATH), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		form_changing_parameters_in_db.setWindowIcon(icon)

		self.parameters_combo_box = QtWidgets.QGroupBox(form_changing_parameters_in_db)
		self.parameters_combo_box.setGeometry(QtCore.QRect(10, 0, 901, 401))
		self.parameters_combo_box.setObjectName("parameters_combo_box")
		self.parameters_item_in_db_combo_box = QtWidgets.QGroupBox(self.parameters_combo_box)
		self.parameters_item_in_db_combo_box.setGeometry(QtCore.QRect(0, 20, 601, 371))
		self.parameters_item_in_db_combo_box.setObjectName("parameters_item_in_db_combo_box")
		self.gridLayoutWidget = QtWidgets.QWidget(self.parameters_item_in_db_combo_box)
		self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 581, 351))
		self.gridLayoutWidget.setObjectName("gridLayoutWidget")
		self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.gridLayout.setObjectName("gridLayout")
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
		self.parameters_quantity_item_in_db_spin_box = QtWidgets.QSpinBox(self.gridLayoutWidget)
		self.parameters_quantity_item_in_db_spin_box.setAlignment(
			QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
		self.parameters_quantity_item_in_db_spin_box.setObjectName("parameters_quantity_item_in_db_spin_box")
		self.gridLayout.addWidget(self.parameters_quantity_item_in_db_spin_box, 4, 1, 1, 1)
		self.parameters_id_item_in_db_label = QtWidgets.QLabel(self.gridLayoutWidget)
		self.parameters_id_item_in_db_label.setObjectName("parameters_id_item_in_db_label")
		self.gridLayout.addWidget(self.parameters_id_item_in_db_label, 1, 0, 1, 1)
		self.parameters_description_item_in_db_text = QtWidgets.QTextEdit(self.gridLayoutWidget)
		self.parameters_description_item_in_db_text.setObjectName("parameters_description_item_in_db_text")
		self.gridLayout.addWidget(self.parameters_description_item_in_db_text, 3, 1, 1, 2)
		self.parameters_id_item_in_db_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
		self.parameters_id_item_in_db_text.setAcceptDrops(True)
		self.parameters_id_item_in_db_text.setFrame(True)
		self.parameters_id_item_in_db_text.setReadOnly(True)
		self.parameters_id_item_in_db_text.setObjectName("parameters_id_item_in_db_text")
		self.gridLayout.addWidget(self.parameters_id_item_in_db_text, 1, 1, 1, 1)
		self.parameters_name_item_in_db_label = QtWidgets.QLabel(self.gridLayoutWidget)
		self.parameters_name_item_in_db_label.setTextFormat(QtCore.Qt.AutoText)
		self.parameters_name_item_in_db_label.setObjectName("parameters_name_item_in_db_label")
		self.gridLayout.addWidget(self.parameters_name_item_in_db_label, 2, 0, 1, 1)
		self.parameters_description_item_in_db_label = QtWidgets.QLabel(self.gridLayoutWidget)
		self.parameters_description_item_in_db_label.setObjectName("parameters_description_item_in_db_label")
		self.gridLayout.addWidget(self.parameters_description_item_in_db_label, 3, 0, 1, 1)
		self.parameters_quantity_item_in_db_label = QtWidgets.QLabel(self.gridLayoutWidget)
		self.parameters_quantity_item_in_db_label.setObjectName("parameters_quantity_item_in_db_label")
		self.gridLayout.addWidget(self.parameters_quantity_item_in_db_label, 4, 0, 1, 1)
		self.parameters_name_item_in_db_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
		self.parameters_name_item_in_db_text.setObjectName("parameters_name_item_in_db_text")
		self.gridLayout.addWidget(self.parameters_name_item_in_db_text, 2, 1, 1, 2)
		self.parameters_location_in_warehouse_combo_box = QtWidgets.QGroupBox(self.parameters_combo_box)
		self.parameters_location_in_warehouse_combo_box.setGeometry(QtCore.QRect(610, 30, 281, 81))
		self.parameters_location_in_warehouse_combo_box.setObjectName("parameters_location_in_warehouse_combo_box")
		self.parameters_shelf_location_in_warehouse_label = QtWidgets.QLabel(
			self.parameters_location_in_warehouse_combo_box)
		self.parameters_shelf_location_in_warehouse_label.setGeometry(QtCore.QRect(40, 50, 55, 16))
		self.parameters_shelf_location_in_warehouse_label.setObjectName("parameters_shelf_location_in_warehouse_label")
		self.parameters_row_location_in_warehouse_label = QtWidgets.QLabel(self.parameters_location_in_warehouse_combo_box)
		self.parameters_row_location_in_warehouse_label.setGeometry(QtCore.QRect(40, 20, 55, 16))
		self.parameters_row_location_in_warehouse_label.setObjectName("parameters_row_location_in_warehouse_label")
		self.parameters_row_location_in_warehouse_spin_box = QtWidgets.QSpinBox(
			self.parameters_location_in_warehouse_combo_box)
		self.parameters_row_location_in_warehouse_spin_box.setGeometry(QtCore.QRect(110, 20, 151, 22))
		self.parameters_row_location_in_warehouse_spin_box.setAlignment(
			QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
		self.parameters_row_location_in_warehouse_spin_box.setObjectName("parameters_row_location_in_warehouse_spin_box")
		self.parameters_shelf_location_in_warehouse_spin_box = QtWidgets.QSpinBox(
			self.parameters_location_in_warehouse_combo_box)
		self.parameters_shelf_location_in_warehouse_spin_box.setGeometry(QtCore.QRect(110, 50, 151, 22))
		self.parameters_shelf_location_in_warehouse_spin_box.setAlignment(
			QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
		self.parameters_shelf_location_in_warehouse_spin_box.setObjectName(
			"parameters_shelf_location_in_warehouse_spin_box")
		self.save_button = QtWidgets.QPushButton(form_changing_parameters_in_db)
		self.save_button.setGeometry(QtCore.QRect(680, 420, 93, 28))
		self.save_button.setObjectName("save_button")
		self.cancel_button = QtWidgets.QPushButton(form_changing_parameters_in_db)
		self.cancel_button.setGeometry(QtCore.QRect(800, 420, 93, 28))
		self.cancel_button.setObjectName("cancel_button")

		self.retranslate_ui(form_changing_parameters_in_db)
		QtCore.QMetaObject.connectSlotsByName(form_changing_parameters_in_db)

	def retranslate_ui(self, form_changing_parameters_in_db):
		_translate = QtCore.QCoreApplication.translate
		form_changing_parameters_in_db.setWindowTitle(
			_translate("form_changing_parameters_in_db", "Change values selected item in database"))
		self.parameters_combo_box.setTitle(_translate("form_changing_parameters_in_db", "Параметры для изменения"))
		self.parameters_item_in_db_combo_box.setTitle(_translate("form_changing_parameters_in_db", "Общие"))
		self.parameters_id_item_in_db_label.setText(_translate("form_changing_parameters_in_db", "ID предмета в базе:"))
		self.parameters_name_item_in_db_label.setText(_translate("form_changing_parameters_in_db", "Имя:"))
		self.parameters_description_item_in_db_label.setText(
			_translate("form_changing_parameters_in_db", "Описание предмета:"))
		self.parameters_quantity_item_in_db_label.setText(
			_translate("form_changing_parameters_in_db", "Количество предмета на складе:"))
		self.parameters_location_in_warehouse_combo_box.setTitle(
			_translate("form_changing_parameters_in_db", "Расположение"))
		self.parameters_shelf_location_in_warehouse_label.setText(_translate("form_changing_parameters_in_db", "Полка:"))
		self.parameters_row_location_in_warehouse_label.setText(_translate("form_changing_parameters_in_db", "Ряд:"))
		self.save_button.setText(_translate("form_changing_parameters_in_db", "Сохранить"))
		self.cancel_button.setText(_translate("form_changing_parameters_in_db", "Отмена"))


class UiFormConnectToDB(object):

	def __init__(self):
		super(UiFormConnectToDB, self).__init__()

	def setup_ui(self, form_connect_to_db):
		form_connect_to_db.setObjectName(config.NAME_GUI_CONNECT)
		form_connect_to_db.resize(config.WIDTH_CONNECT, config.HEIGHT_CONNECT)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(config.PNG_ICO_PATH), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		form_connect_to_db.setWindowIcon(icon)
		self.parameters_combo_box = QtWidgets.QGroupBox(form_connect_to_db)
		self.parameters_combo_box.setGeometry(QtCore.QRect(0, 0, 641, 241))
		self.parameters_combo_box.setObjectName("parameters_combo_box")
		self.parameters_fault_label = QtWidgets.QLabel(self.parameters_combo_box)
		self.parameters_fault_label.setEnabled(False)
		self.parameters_fault_label.setGeometry(QtCore.QRect(470, 60, 55, 16))
		self.parameters_fault_label.setObjectName("parameters_fault_label")
		self.parameters_check_save_parametrs = QtWidgets.QCheckBox(self.parameters_combo_box)
		self.parameters_check_save_parametrs.setGeometry(QtCore.QRect(20, 190, 161, 20))
		self.parameters_check_save_parametrs.setObjectName("parameters_check_save_parametrs")
		self.parameters_host_label = QtWidgets.QLabel(self.parameters_combo_box)
		self.parameters_host_label.setGeometry(QtCore.QRect(20, 30, 55, 16))
		self.parameters_host_label.setObjectName("parameters_host_label")
		self.parameters_name_db_label = QtWidgets.QLabel(self.parameters_combo_box)
		self.parameters_name_db_label.setGeometry(QtCore.QRect(20, 90, 91, 16))
		self.parameters_name_db_label.setObjectName("parameters_name_db_label")
		self.parameters_user_name_label = QtWidgets.QLabel(self.parameters_combo_box)
		self.parameters_user_name_label.setGeometry(QtCore.QRect(20, 120, 101, 16))
		self.parameters_user_name_label.setObjectName("parameters_user_name_label")
		self.parameters_password_label = QtWidgets.QLabel(self.parameters_combo_box)
		self.parameters_password_label.setGeometry(QtCore.QRect(20, 150, 55, 16))
		self.parameters_password_label.setObjectName("parameters_password_label")
		self.parameters_port_label = QtWidgets.QLabel(self.parameters_combo_box)
		self.parameters_port_label.setGeometry(QtCore.QRect(20, 60, 55, 16))
		self.parameters_port_label.setObjectName("parameters_port_label")
		self.parameters_host_text = QtWidgets.QLineEdit(self.parameters_combo_box)
		self.parameters_host_text.setGeometry(QtCore.QRect(140, 30, 301, 22))
		self.parameters_host_text.setObjectName("parameters_host_text")
		self.parameters_port_text = QtWidgets.QLineEdit(self.parameters_combo_box)
		self.parameters_port_text.setGeometry(QtCore.QRect(140, 60, 301, 22))
		self.parameters_port_text.setObjectName("parameters_port_text")
		self.parameters_name_db_text = QtWidgets.QLineEdit(self.parameters_combo_box)
		self.parameters_name_db_text.setGeometry(QtCore.QRect(140, 90, 301, 22))
		self.parameters_name_db_text.setObjectName("parameters_name_db_text")
		self.parameters_user_name_text = QtWidgets.QLineEdit(self.parameters_combo_box)
		self.parameters_user_name_text.setGeometry(QtCore.QRect(140, 120, 301, 22))
		self.parameters_user_name_text.setObjectName("parameters_user_name_text")
		self.parameters_password_text = QtWidgets.QLineEdit(self.parameters_combo_box)
		self.parameters_password_text.setGeometry(QtCore.QRect(140, 150, 301, 22))
		self.parameters_password_text.setEchoMode(QtWidgets.QLineEdit.Password)
		self.parameters_password_text.setPlaceholderText("")
		self.parameters_password_text.setObjectName("parameters_password_text")
		self.parameters_check_default_connect_settings = QtWidgets.QCheckBox(self.parameters_combo_box)
		self.parameters_check_default_connect_settings.setGeometry(QtCore.QRect(210, 190, 391, 20))
		self.parameters_check_default_connect_settings.setObjectName("parameters_check_default_connect_settings")
		self.connect_to_db_button = QtWidgets.QPushButton(form_connect_to_db)
		self.connect_to_db_button.setGeometry(QtCore.QRect(402, 250, 111, 28))
		self.connect_to_db_button.setObjectName("connect_to_db_button")
		self.cancel_connect_to_db_button = QtWidgets.QPushButton(form_connect_to_db)
		self.cancel_connect_to_db_button.setGeometry(QtCore.QRect(530, 250, 93, 28))
		self.cancel_connect_to_db_button.setObjectName("cancel_connect_to_db_button")

		self.retranslate_ui(form_connect_to_db)
		QtCore.QMetaObject.connectSlotsByName(form_connect_to_db)

	def retranslate_ui(self, form_connect_to_db):
		_translate = QtCore.QCoreApplication.translate
		form_connect_to_db.setWindowTitle(_translate("form_connect_to_db", "Connect to database"))
		self.parameters_combo_box.setTitle(_translate("form_connect_to_db", "Параметры"))
		self.parameters_fault_label.setText(_translate("form_connect_to_db", "ОШИБКА"))
		self.parameters_check_save_parametrs.setText(_translate("form_connect_to_db", "Сохранить параметры"))
		self.parameters_host_label.setText(_translate("form_connect_to_db", "Хост:"))
		self.parameters_name_db_label.setText(_translate("form_connect_to_db", "База данных:"))
		self.parameters_user_name_label.setText(_translate("form_connect_to_db", "Пользователь:"))
		self.parameters_password_label.setText(_translate("form_connect_to_db", "Пароль:"))
		self.parameters_port_label.setText(_translate("form_connect_to_db", "Порт:"))
		self.parameters_check_default_connect_settings.setText(_translate("form_connect_to_db", "Тестовые параметры подключения (по умолчанию posgress)"))
		self.connect_to_db_button.setText(_translate("form_connect_to_db", "Подключиться"))
		self.cancel_connect_to_db_button.setText(_translate("form_connect_to_db", "Отменить"))


def ui_show_module(name):
	name.show()


def ui_create_app():
	app = QtWidgets.QApplication(sys.argv)

	main_window = QtWidgets.QMainWindow()
	ui = UiMainWindow()
	ui.setup_ui(main_window)

	change_params_window = QtWidgets.QMainWindow()
	ui_change_params = UiFormChangingParametersInDb()
	ui_change_params.setup_ui(change_params_window)

	connect_to_db_window = QtWidgets.QMainWindow()
	ui_connect_to_db = UiFormConnectToDB()
	ui_connect_to_db.setup_ui(connect_to_db_window)

	ui_show_module(main_window)
	ui_show_module(change_params_window)
	ui_show_module(connect_to_db_window)

	sys.exit(app.exec_())


def create_app():
	app = QtWidgets.QApplication(sys.argv)
	name = Window()
	name.show()
	# print(Window.mro())  # rules entry
	sys.exit(app.exec_())


if __name__ == '__main__':
	# create_app()     # old UI
	ui_create_app()  # new UI

# From directory catalog make command for compile *.ui to *.py
# pyuic5 -x .\views\qt_windows\main_window.ui -o .\views\qt_to_py_windows\main_window.py
# pyuic5 -x .\views\qt_windows\connect_to_db.ui -o .\views\qt_to_py_windows\connect_to_db.py
# pyuic5 -x .\views\qt_windows\change_values_item_in_db.ui -o .\views\qt_to_py_windows\change_values_item_in_db.py

