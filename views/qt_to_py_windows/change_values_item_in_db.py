# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\views\qt_windows\change_values_item_in_db.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_changing_parameters_in_db(object):
    def setupUi(self, form_changing_parameters_in_db):
        form_changing_parameters_in_db.setObjectName("form_changing_parameters_in_db")
        form_changing_parameters_in_db.resize(918, 469)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\views\\qt_windows\\../ico_gui.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.parameters_quantity_item_in_db_spin_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.parameters_quantity_item_in_db_spin_box.setObjectName("parameters_quantity_item_in_db_spin_box")
        self.gridLayout.addWidget(self.parameters_quantity_item_in_db_spin_box, 6, 1, 1, 1)
        self.parameters_id_item_in_db_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.parameters_id_item_in_db_label.setObjectName("parameters_id_item_in_db_label")
        self.gridLayout.addWidget(self.parameters_id_item_in_db_label, 1, 0, 1, 1)
        self.parameters_description_item_in_db_text = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.parameters_description_item_in_db_text.setObjectName("parameters_description_item_in_db_text")
        self.gridLayout.addWidget(self.parameters_description_item_in_db_text, 4, 1, 1, 2)
        self.parameters_name_item_in_db_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.parameters_name_item_in_db_label.setTextFormat(QtCore.Qt.AutoText)
        self.parameters_name_item_in_db_label.setObjectName("parameters_name_item_in_db_label")
        self.gridLayout.addWidget(self.parameters_name_item_in_db_label, 2, 0, 1, 1)
        self.parameters_id_item_in_db_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.parameters_id_item_in_db_text.setAcceptDrops(True)
        self.parameters_id_item_in_db_text.setFrame(True)
        self.parameters_id_item_in_db_text.setReadOnly(True)
        self.parameters_id_item_in_db_text.setObjectName("parameters_id_item_in_db_text")
        self.gridLayout.addWidget(self.parameters_id_item_in_db_text, 1, 1, 1, 1)
        self.parameters_description_item_in_db_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.parameters_description_item_in_db_label.setObjectName("parameters_description_item_in_db_label")
        self.gridLayout.addWidget(self.parameters_description_item_in_db_label, 4, 0, 1, 1)
        self.parameters_name_item_in_db_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.parameters_name_item_in_db_text.setObjectName("parameters_name_item_in_db_text")
        self.gridLayout.addWidget(self.parameters_name_item_in_db_text, 2, 1, 1, 2)
        self.parameters_quantity_item_in_db_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.parameters_quantity_item_in_db_label.setObjectName("parameters_quantity_item_in_db_label")
        self.gridLayout.addWidget(self.parameters_quantity_item_in_db_label, 6, 0, 1, 1)
        self.parameters_ozm_item_in_db_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.parameters_ozm_item_in_db_label.setObjectName("parameters_ozm_item_in_db_label")
        self.gridLayout.addWidget(self.parameters_ozm_item_in_db_label, 3, 0, 1, 1)
        self.parameters_ozm_item_in_db_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.parameters_ozm_item_in_db_text.setObjectName("parameters_ozm_item_in_db_text")
        self.gridLayout.addWidget(self.parameters_ozm_item_in_db_text, 3, 1, 1, 1)
        self.parameters_location_in_warehouse_combo_box = QtWidgets.QGroupBox(self.parameters_combo_box)
        self.parameters_location_in_warehouse_combo_box.setGeometry(QtCore.QRect(610, 30, 281, 81))
        self.parameters_location_in_warehouse_combo_box.setObjectName("parameters_location_in_warehouse_combo_box")
        self.parameters_shelf_location_in_warehouse_label = QtWidgets.QLabel(self.parameters_location_in_warehouse_combo_box)
        self.parameters_shelf_location_in_warehouse_label.setGeometry(QtCore.QRect(40, 50, 55, 16))
        self.parameters_shelf_location_in_warehouse_label.setObjectName("parameters_shelf_location_in_warehouse_label")
        self.parameters_row_location_in_warehouse_label = QtWidgets.QLabel(self.parameters_location_in_warehouse_combo_box)
        self.parameters_row_location_in_warehouse_label.setGeometry(QtCore.QRect(40, 20, 55, 16))
        self.parameters_row_location_in_warehouse_label.setObjectName("parameters_row_location_in_warehouse_label")
        self.parameters_row_location_in_warehouse_spin_box = QtWidgets.QSpinBox(self.parameters_location_in_warehouse_combo_box)
        self.parameters_row_location_in_warehouse_spin_box.setGeometry(QtCore.QRect(110, 20, 151, 22))
        self.parameters_row_location_in_warehouse_spin_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.parameters_row_location_in_warehouse_spin_box.setObjectName("parameters_row_location_in_warehouse_spin_box")
        self.parameters_shelf_location_in_warehouse_spin_box = QtWidgets.QSpinBox(self.parameters_location_in_warehouse_combo_box)
        self.parameters_shelf_location_in_warehouse_spin_box.setGeometry(QtCore.QRect(110, 50, 151, 22))
        self.parameters_shelf_location_in_warehouse_spin_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.parameters_shelf_location_in_warehouse_spin_box.setObjectName("parameters_shelf_location_in_warehouse_spin_box")
        self.save_button = QtWidgets.QPushButton(form_changing_parameters_in_db)
        self.save_button.setGeometry(QtCore.QRect(680, 420, 93, 28))
        self.save_button.setObjectName("save_button")
        self.cancel_button = QtWidgets.QPushButton(form_changing_parameters_in_db)
        self.cancel_button.setGeometry(QtCore.QRect(800, 420, 93, 28))
        self.cancel_button.setObjectName("cancel_button")

        self.retranslateUi(form_changing_parameters_in_db)
        QtCore.QMetaObject.connectSlotsByName(form_changing_parameters_in_db)

    def retranslateUi(self, form_changing_parameters_in_db):
        _translate = QtCore.QCoreApplication.translate
        form_changing_parameters_in_db.setWindowTitle(_translate("form_changing_parameters_in_db", "Change values selected item in database"))
        self.parameters_combo_box.setTitle(_translate("form_changing_parameters_in_db", "Параметры для изменения"))
        self.parameters_item_in_db_combo_box.setTitle(_translate("form_changing_parameters_in_db", "Общие"))
        self.parameters_id_item_in_db_label.setText(_translate("form_changing_parameters_in_db", "ID предмета в базе:"))
        self.parameters_name_item_in_db_label.setText(_translate("form_changing_parameters_in_db", "Имя:"))
        self.parameters_description_item_in_db_label.setText(_translate("form_changing_parameters_in_db", "Описание предмета:"))
        self.parameters_quantity_item_in_db_label.setText(_translate("form_changing_parameters_in_db", "Количество предмета на складе:"))
        self.parameters_ozm_item_in_db_label.setText(_translate("form_changing_parameters_in_db", "Заказной номер (ОЗМ)"))
        self.parameters_location_in_warehouse_combo_box.setTitle(_translate("form_changing_parameters_in_db", "Расположение"))
        self.parameters_shelf_location_in_warehouse_label.setText(_translate("form_changing_parameters_in_db", "Полка:"))
        self.parameters_row_location_in_warehouse_label.setText(_translate("form_changing_parameters_in_db", "Ряд:"))
        self.save_button.setText(_translate("form_changing_parameters_in_db", "Сохранить"))
        self.cancel_button.setText(_translate("form_changing_parameters_in_db", "Отмена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_changing_parameters_in_db = QtWidgets.QDialog()
    ui = Ui_form_changing_parameters_in_db()
    ui.setupUi(form_changing_parameters_in_db)
    form_changing_parameters_in_db.show()
    sys.exit(app.exec_())
