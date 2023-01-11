"""

This block created GUI for view information from postgres database.

Author: Kirto
Version: 0.5
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import typing
import variables as config
import psycopg2 as sql
import sys
import os


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

		self.data = add_and_receive_variables_to_os_environment_from_file()

		self.data['main_window'] = self
		self.data['select_item'] = {}
		self.data['change_item'] = {}

		self.connect_to_db_window = QtWidgets.QMainWindow()
		self.data['connect_window'] = self.connect_to_db_window
		self.ui_connect_to_db = UiFormConnectToDB(self.data)
		self.ui_connect_to_db.setup_ui(self.connect_to_db_window)

		self.change_params_window = QtWidgets.QMainWindow()
		self.data['params_window'] = self.change_params_window   # now not used
		self.ui_change_params = UiFormChangingParametersInDb(self.data)
		self.ui_change_params.setup_ui(self.change_params_window)
		self.data['params_ui'] = self.ui_change_params

		if int(self.data['DEFAULT_SETTINGS_LOAD']) == 1:
			self.ui_connect_to_db.parameters_check_default_connect_settings.setChecked(True)

	def update_search_button_when_no_search_text(self):
		if self.search_text.text():
			self.search_button.setEnabled(True)
		else:
			self.search_button.setEnabled(False)

	@staticmethod
	def exit_push_button():
		exit()

	@staticmethod
	def exit_menu_action():
		exit()

	def change_parameters_in_item_in_db(self):
		self.load_settings_for_item_from_db()

	def validate_text_on_change(self, old_data: dict) -> dict:   # FIXME: _____
		""" This save parameters from window with parameters of item in date base to self.data['change_item']. """

		data = {}

		name = self.ui_change_params.parameters_name_item_in_db_text.text()
		ozm = int(self.ui_change_params.parameters_ozm_item_in_db_text.text())
		description = self.ui_change_params.parameters_description_item_in_db_text.toPlainText()
		quantity = int(self.ui_change_params.parameters_quantity_item_in_db_spin_box.text())
		row_in_warehouse = self.ui_change_params.parameters_row_location_in_warehouse_spin_box.text()
		shelf_in_warehouse = self.ui_change_params.parameters_shelf_location_in_warehouse_spin_box.text()

		if old_data['name'] != name:
			data['name'] = name
		if old_data['ozm'] != ozm:
			data['ozm'] = ozm
		if old_data['description'] != description:
			data['description'] = description
		if old_data['quantity'] != quantity:
			data['quantity'] = quantity
		# if old_data['row'] != row_in_warehouse:
		# 	data['row'] = row_in_warehouse
		# if old_data['shelf'] != shelf_in_warehouse:
		# 	data['shelf'] = shelf_in_warehouse

		return data

	def save_to_db_new_parameters(self):
		if self.data['change_item']:
			update_db_a_new_values(self.data)

	def save_parameters_in_data(self):
		self.data['change_item'] = self.validate_text_on_change(self.data['select_item'])

		if self.data['change_item']:
			self.data['main_window'].command_save_button.setEnabled(True)
			self.data['main_window'].command_undo_button.setEnabled(True)
		else:
			self.data['main_window'].command_save_button.setEnabled(False)
			self.data['main_window'].command_undo_button.setEnabled(False)

		self.data['params_window'].close()

	def stay_parameters_in_prev_state_of_item_in_db(self):
		self.data['change_item'] = {}

	def search_item_in_db(self):  # FIXME:  _____
		print('search ....')

	def action_file_connect_to_db(self):
		load_connection_default_settings(self.ui_connect_to_db, self.data)
		ui_show_module(self.connect_to_db_window)

	def action_file_export_to_svc(self):   # FIXME:  _____
		print('File -> Export -> to *.svc')

	def action_about_help(self):   # FIXME:  _____
		print('About -> Help')

	def show_items_from_db_on_connect_to_db(self):
		for _ in self.data['catalog_items_db']:
			s = 'ID = {:6} | NAME = {:30} | OZM = {:10} | DESCR = {:30} | COUNT = {:6}'.format(_[0], _[1], _[2],
			                                                                                   _[3], _[4])
			self.result_list_view.insertItem(0, s)

	def add_values_to_parameters_of_item(self, ui, values: dict):  # FIXME: add to window OZM text and label in QtDesiner
		ui.parameters_id_item_in_db_text.setText(str(values['id']))
		ui.parameters_name_item_in_db_text.setText(values['name'])
		ui.parameters_ozm_item_in_db_text.setText(str(values['ozm']))
		ui.parameters_description_item_in_db_text.setText(values['description'])
		ui.parameters_quantity_item_in_db_spin_box.setValue(values['quantity'])
	# ui.parameters_row_location_in_warehouse_spin_box.setValue(values['row'])
	# ui.parameters_shelf_location_in_warehouse_spin_box.setValue(values['shelf'])

	def add_selected_item_in_data(self, data: dict):
		self.data = load_settings_selected_item_for_to_parametrate_this_item(data, data['catalog_item_db_ID'])
		self.add_values_to_parameters_of_item(data['params_ui'], data['select_item'])

	def load_settings_for_item_from_db(self):
		s = self.result_list_view.currentItem().text()
		s = s.split('|')[0].strip()
		ss = ''
		for _ in s:
			if _.isdigit():
				ss += _
		if ss:
			self.data['catalog_item_db_ID'] = int(ss)
		else:
			self.data['catalog_item_db_ID'] = 0
		self.add_selected_item_in_data(self.data)
		ui_show_module(self.change_params_window)

	# Main settings
	def setup_ui(self, MainWindow):
		MainWindow.setObjectName(config.NAME_GUI)
		MainWindow.setFixedSize(config.WIDTH_MAIN, config.HEIGHT_MAIN)
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

		self.result_list_view = QtWidgets.QListWidget(self.result_combo_box)
		self.result_list_view.setGeometry(QtCore.QRect(20, 40, 1021, 401))
		self.result_list_view.setObjectName("result_list_view")
		self.result_list_view.doubleClicked.connect(self.load_settings_for_item_from_db)

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
		self.search_text.textChanged.connect(self.update_search_button_when_no_search_text)

		self.horizontalLayout.addWidget(self.search_text)

		self.search_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.search_button.setObjectName("search_button")
		self.search_button.setEnabled(False)
		self.search_button.clicked.connect(self.search_item_in_db)

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
		self.command_undo_button.setEnabled(False)
		self.command_undo_button.clicked.connect(self.stay_parameters_in_prev_state_of_item_in_db)

		self.command_save_button = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.command_save_button.setObjectName("command_save_button")
		self.gridLayout.addWidget(self.command_save_button, 0, 1, 1, 1)
		self.command_save_button.setEnabled(False)
		self.command_save_button.clicked.connect(self.save_to_db_new_parameters)

		self.command_change_button = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.command_change_button.setObjectName("command_change_button")
		self.gridLayout.addWidget(self.command_change_button, 0, 0, 1, 1)
		self.command_change_button.setEnabled(False)
		self.command_change_button.clicked.connect(self.change_parameters_in_item_in_db)

		self.command_exit_button = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.command_exit_button.setObjectName("command_exit_button")
		self.gridLayout.addWidget(self.command_exit_button, 0, 3, 1, 1)
		self.command_exit_button.clicked.connect(self.exit_push_button)

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
		self.menu_file_connect.triggered.connect(self.action_file_connect_to_db)

		self.action = QtWidgets.QAction(MainWindow)
		self.action.setCheckable(False)
		self.action.setEnabled(False)
		self.action.setObjectName("action")

		self.menu_file_exit = QtWidgets.QAction(MainWindow)
		self.menu_file_exit.setObjectName("menu_file_exit")
		self.menu_file_exit.triggered.connect(self.exit_menu_action)

		self.menu_about_help = QtWidgets.QAction(MainWindow)
		self.menu_about_help.setObjectName("menu_about_help")
		self.menu_about_help.triggered.connect(self.action_about_help)

		self.menu_file_export_to_svc = QtWidgets.QAction(MainWindow)
		self.menu_file_export_to_svc.setObjectName("menu_file_export_to_svc")
		self.menu_file_export_to_svc.triggered.connect(self.action_file_export_to_svc)
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
		self.menu_file_export_to.setTitle(_translate("MainWindow", "Импорт ..."))
		self.menu_about.setTitle(_translate("MainWindow", "О программе"))
		self.menu_file_connect.setText(_translate("MainWindow", "Подключить ..."))
		self.action.setText(_translate("MainWindow", "-------------------"))
		self.menu_file_exit.setText(_translate("MainWindow", "Выход ...."))
		self.menu_about_help.setText(_translate("MainWindow", "Помощь ..."))
		self.menu_file_export_to_svc.setText(_translate("MainWindow", "в *.svc ...."))


class UiFormChangingParametersInDb(object):

	def __init__(self, data: dict):
		super(UiFormChangingParametersInDb, self).__init__()
		self.data = data

	def cancel_change_parameters(self):
		self.data['params_window'].close()

	def setup_ui(self, form_changing_parameters_in_db):
		form_changing_parameters_in_db.setObjectName(config.NAME_GUI_CHANGE_ITEM)
		form_changing_parameters_in_db.setFixedSize(config.WIDTH_CHANGE, config.HEIGHT_CHANGE)
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
		self.__spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(self.__spacerItem, 1, 2, 1, 1)

		self.parameters_quantity_item_in_db_spin_box = QtWidgets.QSpinBox(self.gridLayoutWidget)
		self.parameters_quantity_item_in_db_spin_box.setAlignment(
			QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
		self.parameters_quantity_item_in_db_spin_box.setObjectName("parameters_quantity_item_in_db_spin_box")
		self.gridLayout.addWidget(self.parameters_quantity_item_in_db_spin_box, 6, 1, 1, 1)
		self.parameters_quantity_item_in_db_spin_box.setMaximum(config.MAX_VALUES_FOR_ITEMS)

		self.parameters_id_item_in_db_label = QtWidgets.QLabel(self.gridLayoutWidget)
		self.parameters_id_item_in_db_label.setObjectName("parameters_id_item_in_db_label")
		self.gridLayout.addWidget(self.parameters_id_item_in_db_label, 1, 0, 1, 1)

		self.parameters_description_item_in_db_text = QtWidgets.QTextEdit(self.gridLayoutWidget)
		self.parameters_description_item_in_db_text.setObjectName("parameters_description_item_in_db_text")
		self.gridLayout.addWidget(self.parameters_description_item_in_db_text, 4, 1, 1, 2)

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
		self.gridLayout.addWidget(self.parameters_description_item_in_db_label, 4, 0, 1, 1)

		self.parameters_quantity_item_in_db_label = QtWidgets.QLabel(self.gridLayoutWidget)
		self.parameters_quantity_item_in_db_label.setObjectName("parameters_quantity_item_in_db_label")
		self.gridLayout.addWidget(self.parameters_quantity_item_in_db_label, 6, 0, 1, 1)

		self.parameters_ozm_item_in_db_label = QtWidgets.QLabel(self.gridLayoutWidget)
		self.parameters_ozm_item_in_db_label.setObjectName("parameters_ozm_item_in_db_label")
		self.gridLayout.addWidget(self.parameters_ozm_item_in_db_label, 3, 0, 1, 1)

		self.parameters_ozm_item_in_db_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
		self.parameters_ozm_item_in_db_text.setObjectName("parameters_ozm_item_in_db_text")
		self.gridLayout.addWidget(self.parameters_ozm_item_in_db_text, 3, 1, 1, 1)

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
		self.parameters_row_location_in_warehouse_label = QtWidgets.QLabel(
			self.parameters_location_in_warehouse_combo_box)
		self.parameters_row_location_in_warehouse_label.setGeometry(QtCore.QRect(40, 20, 55, 16))
		self.parameters_row_location_in_warehouse_label.setObjectName("parameters_row_location_in_warehouse_label")

		self.parameters_row_location_in_warehouse_spin_box = QtWidgets.QSpinBox(
			self.parameters_location_in_warehouse_combo_box)
		self.parameters_row_location_in_warehouse_spin_box.setGeometry(QtCore.QRect(110, 20, 151, 22))
		self.parameters_row_location_in_warehouse_spin_box.setAlignment(
			QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
		self.parameters_row_location_in_warehouse_spin_box.setObjectName(
			"parameters_row_location_in_warehouse_spin_box")
		self.parameters_row_location_in_warehouse_spin_box.setMaximum(config.MAX_VALUES_FOR_ROW)

		self.parameters_shelf_location_in_warehouse_spin_box = QtWidgets.QSpinBox(
			self.parameters_location_in_warehouse_combo_box)
		self.parameters_shelf_location_in_warehouse_spin_box.setGeometry(QtCore.QRect(110, 50, 151, 22))
		self.parameters_shelf_location_in_warehouse_spin_box.setAlignment(
			QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
		self.parameters_shelf_location_in_warehouse_spin_box.setObjectName(
			"parameters_shelf_location_in_warehouse_spin_box")
		self.parameters_shelf_location_in_warehouse_spin_box.setMaximum(config.MAX_VALUES_FOR_SHELF)

		self.save_button = QtWidgets.QPushButton(form_changing_parameters_in_db)
		self.save_button.setGeometry(QtCore.QRect(680, 420, 93, 28))
		self.save_button.setObjectName("save_button")
		self.save_button.clicked.connect(self.data['main_window'].save_parameters_in_data)

		self.cancel_button = QtWidgets.QPushButton(form_changing_parameters_in_db)
		self.cancel_button.setGeometry(QtCore.QRect(800, 420, 93, 28))
		self.cancel_button.setObjectName("cancel_button")
		self.cancel_button.clicked.connect(self.cancel_change_parameters)

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
		self.parameters_ozm_item_in_db_label.setText(
			_translate("form_changing_parameters_in_db", "Заказной номер (ОЗМ):"))
		self.parameters_description_item_in_db_label.setText(
			_translate("form_changing_parameters_in_db", "Описание предмета:"))
		self.parameters_quantity_item_in_db_label.setText(
			_translate("form_changing_parameters_in_db", "Количество предмета на складе:"))
		self.parameters_location_in_warehouse_combo_box.setTitle(
			_translate("form_changing_parameters_in_db", "Расположение"))
		self.parameters_shelf_location_in_warehouse_label.setText(
			_translate("form_changing_parameters_in_db", "Полка:"))
		self.parameters_row_location_in_warehouse_label.setText(_translate("form_changing_parameters_in_db", "Ряд:"))
		self.save_button.setText(_translate("form_changing_parameters_in_db", "Сохранить"))
		self.cancel_button.setText(_translate("form_changing_parameters_in_db", "Отмена"))


class UiFormConnectToDB(object):

	def __init__(self, data: dict):
		super(UiFormConnectToDB, self).__init__()
		self.data = data

	def connection_connect_button(self):
		cursor = connect_to_db(self.data)
		if cursor:
			self.data['cursor'] = cursor
			self.data['catalog_items_db'] = load_from_db_items(self.data, config.LIMIT_IN_LIST_HOME_PAGE)
			self.data['main_window'].show_items_from_db_on_connect_to_db()
			self.data['main_window'].command_change_button.setEnabled(True)
			self.data['connect_window'].close()

	def connection_cancel_button(self):
		self.data['connect_window'].close()

	def load_default_if_checked_checkbox(self):
		load_connection_default_settings(self, self.data)

	def setup_ui(self, form_connect_to_db):
		form_connect_to_db.setObjectName(config.NAME_GUI_CONNECT)
		form_connect_to_db.setFixedSize(config.WIDTH_CONNECT, config.HEIGHT_CONNECT)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(config.PNG_ICO_PATH), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		form_connect_to_db.setWindowIcon(icon)

		self.parameters_combo_box = QtWidgets.QGroupBox(form_connect_to_db)
		self.parameters_combo_box.setGeometry(QtCore.QRect(0, 0, 641, 241))
		self.parameters_combo_box.setObjectName("parameters_combo_box")

		self.parameters_fault_label = QtWidgets.QLabel(self.parameters_combo_box)
		self.parameters_fault_label.setEnabled(True)
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
		self.parameters_check_default_connect_settings.stateChanged.connect(self.load_default_if_checked_checkbox)

		self.connect_to_db_button = QtWidgets.QPushButton(form_connect_to_db)
		self.connect_to_db_button.setGeometry(QtCore.QRect(402, 250, 111, 28))
		self.connect_to_db_button.setObjectName("connect_to_db_button")
		self.cursor = self.connect_to_db_button.clicked.connect(self.connection_connect_button)

		self.cancel_connect_to_db_button = QtWidgets.QPushButton(form_connect_to_db)
		self.cancel_connect_to_db_button.setGeometry(QtCore.QRect(530, 250, 93, 28))
		self.cancel_connect_to_db_button.setObjectName("cancel_connect_to_db_button")
		self.cancel_connect_to_db_button.clicked.connect(self.connection_cancel_button)

		self.retranslate_ui(form_connect_to_db)
		QtCore.QMetaObject.connectSlotsByName(form_connect_to_db)

	def retranslate_ui(self, form_connect_to_db):
		_translate = QtCore.QCoreApplication.translate
		form_connect_to_db.setWindowTitle(_translate("form_connect_to_db", "Подключение к базе данных"))
		self.parameters_fault_label.setText(_translate("form_connect_to_db", "ОШИБКА"))
		self.parameters_combo_box.setTitle(_translate("form_connect_to_db", "Параметры"))
		self.parameters_check_save_parametrs.setText(_translate("form_connect_to_db", "Сохранить параметры"))
		self.parameters_host_label.setText(_translate("form_connect_to_db", "Хост:"))
		self.parameters_name_db_label.setText(_translate("form_connect_to_db", "База данных:"))
		self.parameters_user_name_label.setText(_translate("form_connect_to_db", "Пользователь:"))
		self.parameters_password_label.setText(_translate("form_connect_to_db", "Пароль:"))
		self.parameters_port_label.setText(_translate("form_connect_to_db", "Порт:"))
		self.parameters_check_default_connect_settings.setText(_translate("form_connect_to_db", "Тестовые параметры "
		                                                                                        "подключения (по "
		                                                                                        "умолчанию "
		                                                                                        "posgress)"))
		self.connect_to_db_button.setText(_translate("form_connect_to_db", "Подключиться"))
		self.cancel_connect_to_db_button.setText(_translate("form_connect_to_db", "Отменить"))


def ui_show_module(name):
	name.show()


def ui_create_app():
	app = QtWidgets.QApplication(sys.argv)

	main_window = QtWidgets.QMainWindow()
	ui = UiMainWindow()
	ui.setup_ui(main_window)

	# Show module
	ui_show_module(main_window)

	sys.exit(app.exec_())


def load_connection_default_settings(name, conf: dict):
	if name.parameters_check_default_connect_settings.isChecked():
		name.parameters_name_db_text.setText(conf['DB_NAME'])
		name.parameters_user_name_text.setText(conf['USER_NAME_DB'])
		name.parameters_host_text.setText(conf['HOST'])
		name.parameters_port_text.setText(conf['PORT'])
		name.parameters_password_text.setText(conf['PASSWORD_DB'])
	else:
		name.parameters_name_db_text.clear()
		name.parameters_user_name_text.clear()
		name.parameters_host_text.clear()
		name.parameters_port_text.clear()
		name.parameters_password_text.clear()


def create_app():  # for class Window()
	app = QtWidgets.QApplication(sys.argv)
	name = Window()
	name.show()
	sys.exit(app.exec_())


def add_and_receive_variables_to_os_environment_from_file(name: str = '.env', sep: str = ' = ') -> dict:
	f = open(os.getcwd() + '\\..\\\\' + name, 'rt')
	data = {}
	with f:
		for _ in f:
			s = _.strip().split(sep=sep)
			if s[1][0] == '\'':
				s[1] = s[1][1:-1]
			if not os.getenv(s[0]):
				os.environ.setdefault(s[0], s[1])
			data[s[0]] = s[1]
	return data


def connect_to_db(data: dict):
	conn_string = "host=" + data['HOST'] + " port=" + data['PORT'] + " dbname=" + \
				  data['DB_NAME'] + " user=" + data['USER_NAME_DB'] + " password=" + data['PASSWORD_DB']
	conn = sql.connect(conn_string)
	cursor = conn.cursor()
	return cursor


def load_from_db_items(data: dict, limit: int):
	sql_query = f"SELECT id, name, ozm, description, quantity FROM {data['TABLE_NAME']} ORDER BY quantity ASC LIMIT" \
	            f" {limit}"
	data['cursor'].execute(sql_query)
	sel = data['cursor'].fetchall()
	return sel


def update_db_a_new_values(data: dict): # FIXME:__
	print(data)
	print('Updating ...')


def load_settings_selected_item_for_to_parametrate_this_item(data: dict, id: int):  # not used!!!!  FIXME: _____
	sql_query = f"SELECT * FROM {data['TABLE_NAME']} WHERE id = {id}"
	data['cursor'].execute(sql_query)
	sel = data['cursor'].fetchall()
	data['select_item']['id'] = sel[0][0]
	data['select_item']['name'] = sel[0][1]
	data['select_item']['ozm'] = sel[0][2]
	data['select_item']['description'] = sel[0][3]
	data['select_item']['quantity'] = sel[0][4]
	# item['select_item']['row'] = sel[5] | None
	# item['select_item']['shelf'] = sel[6] | None
	return data


if __name__ == '__main__':
	# print(add_and_receive_variables_to_os_environment_from_file())
	# print(os.environ.values())
	# create_app()     # old UI
	ui_create_app()  # new UI


	# sql_query = f"SELECT * FROM {data['TABLE_NAME']} ORDER BY quantity ASC LIMIT 10"
	# cursor.execute(sql_query)
	#
	# sel = cursor.fetchall()


# From directory catalog make command in terminal for compile *.ui to *.py
# pyuic5 -x .\views\qt_windows\main_window.ui -o .\views\qt_to_py_windows\main_window.py
# pyuic5 -x .\views\qt_windows\connect_to_db.ui -o .\views\qt_to_py_windows\connect_to_db.py
# pyuic5 -x .\views\qt_windows\change_values_item_in_db.ui -o .\views\qt_to_py_windows\change_values_item_in_db.py
