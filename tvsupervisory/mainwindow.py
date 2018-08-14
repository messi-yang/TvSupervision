#!/usr/bin/python  
# -*- coding: utf-8 -*-

"""
author: Jeffrey
date: 2018/8/13
"""

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets


class Ui_Form(object):
    def setupUi(self, form):
        """
        Construct all kinds of UI widget of the application.

        All UI objects are there and also include signals and slots declaration.

        :return:
        """
        form.setObjectName('Form')
        form.resize(300, 200)
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        form.setFont(font)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('../../docs/images/tv.jpg'),
                       QtGui.QIcon.Normal, QtGui.QIcon.On)
        form.setWindowIcon(icon)

        self.main_layout = QtWidgets.QVBoxLayout(form)
        self.main_layout.setObjectName('main_layout')

        # Power type stackedwidget including widgets and layout.
        self.powertype_groupbox = QtWidgets.QGroupBox(form)
        self.powertype_groupbox.setObjectName('powertype_groupbox')
        self.main_layout.addWidget(self.powertype_groupbox)
        self.powertype_layout = QtWidgets.QVBoxLayout(self.powertype_groupbox)
        self.powertype_layout.setObjectName('powertype_layout')
        self.powertype_stackedwidget = QtWidgets.QStackedWidget()
        self.powertype_stackedwidget.setObjectName('powertype_stackedwidget')
        self.powertype_layout.addWidget(self.powertype_stackedwidget)
        # Power box widget including it's child widget and layout
        self.powerbox_widget = QtWidgets.QWidget()
        self.powerbox_widget.setObjectName('powerbox_widget')
        self.powerbox_layout = QtWidgets.QFormLayout(self.powerbox_widget)
        self.powerbox_layout.setObjectName('powerbox_layout')
        self.powerbox_count_label = QtWidgets.QLabel()
        self.powerbox_count_label.setObjectName('powerbox_count_label')
        self.powerbox_count_lineedit = QtWidgets.QLineEdit()
        self.powerbox_count_lineedit.setObjectName('powerbox_count_lineedit')
        self.powerbox_layout.addRow(self.powerbox_count_label,
                                    self.powerbox_count_lineedit)
        self.powerbox_interval_label = QtWidgets.QLabel()
        self.powerbox_interval_label.setObjectName('powerbox_interval_label')
        self.powerbox_interval_lineedit = QtWidgets.QLineEdit()
        self.powerbox_interval_lineedit.setObjectName(
            'powerbox_interval_lineedit')
        self.powerbox_layout.addRow(self.powerbox_interval_label,
                                    self.powerbox_interval_lineedit)
        self.powertype_stackedwidget.addWidget(self.powerbox_widget)
        # Direct power widget including it's child widget and layout
        self.directpower_widget = QtWidgets.QWidget()
        self.directpower_widget.setObjectName('directpower_widget')
        self.directpower_layout = QtWidgets.QFormLayout(self.directpower_widget)
        self.directpower_layout.setObjectName('directpower_layout')
        self.directpower_count_label = QtWidgets.QLabel()
        self.directpower_count_label.setObjectName('directpower_count_label')
        self.directpower_count_lineedit = QtWidgets.QLineEdit()
        self.directpower_count_lineedit.setObjectName(
            'directpower_count_lineedit')
        self.directpower_layout.addRow(self.directpower_count_label,
                                       self.directpower_count_lineedit)
        self.directpower_offtime_label = QtWidgets.QLabel()
        self.directpower_offtime_label.setObjectName(
            'directpower_offtime_label')
        self.directpower_offtime_lineedit = QtWidgets.QLineEdit()
        self.directpower_offtime_lineedit.setObjectName(
            'directpower_offtime_lineedit')
        self.directpower_layout.addRow(self.directpower_offtime_label,
                                       self.directpower_offtime_lineedit)
        self.directpower_keyvalue_label = QtWidgets.QLabel()
        self.directpower_keyvalue_label.setObjectName(
            'directpower_keyvalue_label')
        self.directpower_keyvalue_lineedit = QtWidgets.QLineEdit()
        self.directpower_keyvalue_lineedit.setObjectName(
            'directpower_keyvalue_lineedit')
        self.directpower_layout.addRow(self.directpower_keyvalue_label,
                                       self.directpower_keyvalue_lineedit)
        self.directpower_interval_label = QtWidgets.QLabel()
        self.directpower_interval_label.setObjectName(
            'pdirectpower_interval_label')
        self.directpower_interval_lineedit = QtWidgets.QLineEdit()
        self.directpower_interval_lineedit.setObjectName(
            'pdirectpower_interval_lineedit')
        self.directpower_layout.addRow(self.directpower_interval_label,
                                       self.directpower_interval_lineedit)
        self.powertype_stackedwidget.addWidget(self.directpower_widget)
        # PRO 800 cross power widget including it's child widget and layout
        self.crosspower_widget = QtWidgets.QWidget()
        self.crosspower_widget.setObjectName('crosspower_widget')
        self.crosspower_layout = QtWidgets.QFormLayout(self.crosspower_widget)
        self.crosspower_layout.setObjectName('crosspower_layout')
        self.crosspower_count_label = QtWidgets.QLabel()
        self.crosspower_count_label.setObjectName('crosspower_count_label')
        self.crosspower_count_lineedit = QtWidgets.QLineEdit()
        self.crosspower_count_lineedit.setObjectName(
            'crosspower_count_lineedit')
        self.crosspower_layout.addRow(self.crosspower_count_label,
                                      self.crosspower_count_lineedit)
        self.crosspower_address_label = QtWidgets.QLabel()
        self.crosspower_address_label.setObjectName('crosspower_address_labe')
        self.crosspower_address_lineedit = QtWidgets.QLineEdit()
        self.crosspower_address_lineedit.setObjectName(
            'crosspower_address_lineedit')
        self.crosspower_layout.addRow(self.crosspower_address_label,
                                      self.crosspower_address_lineedit)
        self.crosspower_on_keyvalue_label = QtWidgets.QLabel()
        self.crosspower_on_keyvalue_label.setObjectName(
            'crosspower_on_keyvalue_label')
        self.crosspower_on_keyvalue_lineedit = QtWidgets.QLineEdit()
        self.crosspower_on_keyvalue_lineedit.setObjectName(
            'crosspower_on_keyvalue_lineedit')
        self.crosspower_layout.addRow(self.crosspower_on_keyvalue_label,
                                      self.crosspower_on_keyvalue_lineedit)
        self.crosspower_off_keyvalue_label = QtWidgets.QLabel()
        self.crosspower_off_keyvalue_label.setObjectName(
            'crosspower_off_keyvalue_label')
        self.crosspower_off_keyvalue_lineedit = QtWidgets.QLineEdit()
        self.crosspower_off_keyvalue_lineedit.setObjectName(
            'crosspower_off_keyvalue_lineedit')
        self.crosspower_layout.addRow(self.crosspower_off_keyvalue_label,
                                      self.crosspower_off_keyvalue_lineedit)
        self.crosspower_interval_label = QtWidgets.QLabel()
        self.crosspower_interval_label.setObjectName(
            'crosspower_interval_label')
        self.crosspower_interval_lineedit = QtWidgets.QLineEdit()
        self.crosspower_interval_lineedit.setObjectName(
            'crosspower_interval_lineedit')
        self.crosspower_layout.addRow(self.crosspower_interval_label,
                                      self.crosspower_interval_lineedit)
        self.powertype_stackedwidget.addWidget(self.crosspower_widget)
        # Power type combobox including it's child and layout
        self.powertype_combobox = QtWidgets.QComboBox()
        self.powertype_combobox.setObjectName('powertype_combobox')
        self.powertype_layout.addWidget(self.powertype_combobox)
        self.powertype_combobox.addItem('')
        self.powertype_combobox.addItem('')
        self.powertype_combobox.addItem('')

        # Camera Setting's widget including it's child and layout
        self.camerasetting_groupbox = QtWidgets.QGroupBox(form)
        self.camerasetting_groupbox.setObjectName('camerasetting_groupbox')
        self.main_layout.addWidget(self.camerasetting_groupbox)
        self.camerasetting_layout = QtWidgets.QVBoxLayout(
            self.camerasetting_groupbox)
        self.camerasetting_layout.setObjectName('camerasetting_layout')
        self.cameratable_tablewidget = QtWidgets.QTableWidget()
        self.cameratable_tablewidget.setObjectName('cameratable_tablewidget')
        self.cameratable_tablewidget.setColumnCount(3)
        self.cameratable_tablewidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cameratable_tablewidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cameratable_tablewidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cameratable_tablewidget.setHorizontalHeaderItem(2, item)
        self.cameratable_tablewidget.hideColumn(2)
        self.camerasetting_layout.addWidget(self.cameratable_tablewidget)
        # Camera buttons using QHBoxLayout
        self.camerabuttons_layout = QtWidgets.QHBoxLayout(
            self.camerasetting_groupbox)
        self.camerabuttons_layout.setObjectName('camerabuttons_layout')
        self.refreshcameratable_pushbutton = QtWidgets.QPushButton()
        self.refreshcameratable_pushbutton.setObjectName(
            'refreshcameratable_pushbutton')
        self.camerabuttons_layout.addWidget(self.refreshcameratable_pushbutton)
        self.opencamera_pushbutton = QtWidgets.QPushButton()
        self.opencamera_pushbutton.setObjectName('opencamera_pushbutton')
        self.camerabuttons_layout.addWidget(self.opencamera_pushbutton)
        self.capturestd_pushbutton = QtWidgets.QPushButton()
        self.capturestd_pushbutton.setObjectName('capturestd_pushbutton')
        self.camerabuttons_layout.addWidget(self.capturestd_pushbutton)
        self.camerasetting_layout.addLayout(self.camerabuttons_layout)

        self.retranslateUi(form)
        self.powertype_stackedwidget.setCurrentIndex(0)
        self.powertype_combobox.currentIndexChanged['int'].connect(
            self.powertype_stackedwidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate('Form', 'TvSupervisory'))

        self.powertype_groupbox.setTitle(_translate('Form',
                                                    'PowerType'))
        self.powerbox_count_label.setText(_translate('Form', '开关机次数'))
        self.powerbox_interval_label.setText(_translate('Form', '拍摄时间间隔'))
        self.directpower_count_label.setText(_translate('Form', '开关机次数'))
        self.directpower_offtime_label.setText(_translate('Form', '关机时间'))
        self.directpower_keyvalue_label.setText(_translate('Form', '电源键值'))
        self.directpower_interval_label.setText((_translate('Form', '拍摄时间间隔')))
        self.crosspower_count_label.setText((_translate('Form', '开关机次数')))
        self.crosspower_address_label.setText((_translate('Form', '继电器地址')))
        self.crosspower_on_keyvalue_label.setText((_translate('Form', '开机键值')))
        self.crosspower_off_keyvalue_label.setText((_translate('Form', '关机键值')))
        self.crosspower_interval_label.setText(_translate('Form', '拍摄时间间隔'))
        self.powertype_combobox.setItemText(0, _translate('Form', '电源箱交流'))
        self.powertype_combobox.setItemText(1, _translate('Form', '红外直流'))
        self.powertype_combobox.setItemText(2, _translate('Form', 'PRO800交流'))

        self.camerasetting_groupbox.setTitle(_translate('Form',
                                                        'CameraSetting'))
        item = self.cameratable_tablewidget.horizontalHeaderItem(0)
        item.setText(_translate('Form', 'Tag'))
        item = self.cameratable_tablewidget.horizontalHeaderItem(1)
        item.setText(_translate('Form', 'Name'))
        item = self.cameratable_tablewidget.horizontalHeaderItem(2)
        item.setText(_translate('Form', 'ID'))
        self.refreshcameratable_pushbutton.setText(_translate('Form', '刷新列表'))
        self.opencamera_pushbutton.setText(_translate('Form', '打开摄像头'))
        self.capturestd_pushbutton.setText(_translate('Form', '拍摄标准图'))
