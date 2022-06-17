# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(895, 802)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.menu_open_pickle = QAction(MainWindow)
        self.menu_open_pickle.setObjectName(u"menu_open_pickle")
        self.menu_open_pickle.setCheckable(False)
        self.menu_transform = QAction(MainWindow)
        self.menu_transform.setObjectName(u"menu_transform")
        self.menu_open_help = QAction(MainWindow)
        self.menu_open_help.setObjectName(u"menu_open_help")
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_21 = QVBoxLayout(self.widget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget_main = QTabWidget(self.widget)
        self.tabWidget_main.setObjectName(u"tabWidget_main")
        self.tabWidget_main.setTabPosition(QTabWidget.North)
        self.tab_data = QWidget()
        self.tab_data.setObjectName(u"tab_data")
        self.verticalLayout_38 = QVBoxLayout(self.tab_data)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.treeWidget_calculations = QTreeWidget(self.tab_data)
        self.treeWidget_calculations.setObjectName(u"treeWidget_calculations")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_calculations.sizePolicy().hasHeightForWidth())
        self.treeWidget_calculations.setSizePolicy(sizePolicy)
        self.treeWidget_calculations.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.treeWidget_calculations.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.treeWidget_calculations.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.treeWidget_calculations.setSelectionMode(QAbstractItemView.SingleSelection)
        self.treeWidget_calculations.setRootIsDecorated(True)
        self.treeWidget_calculations.setUniformRowHeights(False)
        self.treeWidget_calculations.setItemsExpandable(False)
        self.treeWidget_calculations.setSortingEnabled(False)
        self.treeWidget_calculations.setAllColumnsShowFocus(False)
        self.treeWidget_calculations.setWordWrap(False)
        self.treeWidget_calculations.setHeaderHidden(False)
        self.treeWidget_calculations.setExpandsOnDoubleClick(True)
        self.treeWidget_calculations.header().setVisible(True)
        self.treeWidget_calculations.header().setCascadingSectionResizes(False)
        self.treeWidget_calculations.header().setMinimumSectionSize(20)
        self.treeWidget_calculations.header().setDefaultSectionSize(100)
        self.treeWidget_calculations.header().setHighlightSections(False)

        self.verticalLayout_11.addWidget(self.treeWidget_calculations)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.button_up_data = QPushButton(self.tab_data)
        self.button_up_data.setObjectName(u"button_up_data")

        self.horizontalLayout_21.addWidget(self.button_up_data)

        self.button_down_data = QPushButton(self.tab_data)
        self.button_down_data.setObjectName(u"button_down_data")

        self.horizontalLayout_21.addWidget(self.button_down_data)


        self.verticalLayout_11.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_22.addLayout(self.verticalLayout_11)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(self.tab_data)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.line_cut_down_name = QLineEdit(self.tab_data)
        self.line_cut_down_name.setObjectName(u"line_cut_down_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_cut_down_name.sizePolicy().hasHeightForWidth())
        self.line_cut_down_name.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.line_cut_down_name)

        self.line_cut_down_value = QLineEdit(self.tab_data)
        self.line_cut_down_value.setObjectName(u"line_cut_down_value")
        sizePolicy1.setHeightForWidth(self.line_cut_down_value.sizePolicy().hasHeightForWidth())
        self.line_cut_down_value.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.line_cut_down_value)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_13 = QLabel(self.tab_data)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_19.addWidget(self.label_13)

        self.line_cut_up_name = QLineEdit(self.tab_data)
        self.line_cut_up_name.setObjectName(u"line_cut_up_name")
        sizePolicy1.setHeightForWidth(self.line_cut_up_name.sizePolicy().hasHeightForWidth())
        self.line_cut_up_name.setSizePolicy(sizePolicy1)

        self.horizontalLayout_19.addWidget(self.line_cut_up_name)

        self.line_cut_up_value = QLineEdit(self.tab_data)
        self.line_cut_up_value.setObjectName(u"line_cut_up_value")
        sizePolicy1.setHeightForWidth(self.line_cut_up_value.sizePolicy().hasHeightForWidth())
        self.line_cut_up_value.setSizePolicy(sizePolicy1)

        self.horizontalLayout_19.addWidget(self.line_cut_up_value)


        self.verticalLayout_9.addLayout(self.horizontalLayout_19)

        self.tabs_add_calculatuons = QTabWidget(self.tab_data)
        self.tabs_add_calculatuons.setObjectName(u"tabs_add_calculatuons")
        self.tabs_add_calculatuons.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabs_add_calculatuons.sizePolicy().hasHeightForWidth())
        self.tabs_add_calculatuons.setSizePolicy(sizePolicy2)
        self.tabs_add_calculatuons.setLayoutDirection(Qt.LeftToRight)
        self.tab_result = QWidget()
        self.tab_result.setObjectName(u"tab_result")
        self.horizontalLayout_20 = QHBoxLayout(self.tab_result)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.line_name_calc = QLineEdit(self.tab_result)
        self.line_name_calc.setObjectName(u"line_name_calc")
        sizePolicy2.setHeightForWidth(self.line_name_calc.sizePolicy().hasHeightForWidth())
        self.line_name_calc.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.line_name_calc)

        self.line_path_to_result = QLineEdit(self.tab_result)
        self.line_path_to_result.setObjectName(u"line_path_to_result")
        sizePolicy2.setHeightForWidth(self.line_path_to_result.sizePolicy().hasHeightForWidth())
        self.line_path_to_result.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.line_path_to_result)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.button_path_to_calc = QPushButton(self.tab_result)
        self.button_path_to_calc.setObjectName(u"button_path_to_calc")
        sizePolicy1.setHeightForWidth(self.button_path_to_calc.sizePolicy().hasHeightForWidth())
        self.button_path_to_calc.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.button_path_to_calc)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.button_add_result = QPushButton(self.tab_result)
        self.button_add_result.setObjectName(u"button_add_result")
        sizePolicy2.setHeightForWidth(self.button_add_result.sizePolicy().hasHeightForWidth())
        self.button_add_result.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.button_add_result)


        self.horizontalLayout_20.addLayout(self.verticalLayout_5)

        self.tabs_add_calculatuons.addTab(self.tab_result, "")
        self.tab_sockle = QWidget()
        self.tab_sockle.setObjectName(u"tab_sockle")
        self.verticalLayout_12 = QVBoxLayout(self.tab_sockle)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_path_to_sackle = QLineEdit(self.tab_sockle)
        self.line_path_to_sackle.setObjectName(u"line_path_to_sackle")
        sizePolicy2.setHeightForWidth(self.line_path_to_sackle.sizePolicy().hasHeightForWidth())
        self.line_path_to_sackle.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.line_path_to_sackle)

        self.button_path_to_sackle = QPushButton(self.tab_sockle)
        self.button_path_to_sackle.setObjectName(u"button_path_to_sackle")
        sizePolicy1.setHeightForWidth(self.button_path_to_sackle.sizePolicy().hasHeightForWidth())
        self.button_path_to_sackle.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.button_path_to_sackle)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.button_add_sackle = QPushButton(self.tab_sockle)
        self.button_add_sackle.setObjectName(u"button_add_sackle")
        sizePolicy2.setHeightForWidth(self.button_add_sackle.sizePolicy().hasHeightForWidth())
        self.button_add_sackle.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.button_add_sackle)


        self.verticalLayout_12.addLayout(self.verticalLayout_3)

        self.tabs_add_calculatuons.addTab(self.tab_sockle, "")

        self.verticalLayout_9.addWidget(self.tabs_add_calculatuons)

        self.frame_2 = QFrame(self.tab_data)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)

        self.verticalLayout_9.addWidget(self.frame_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.button_del_chosen_data = QPushButton(self.tab_data)
        self.button_del_chosen_data.setObjectName(u"button_del_chosen_data")
        sizePolicy2.setHeightForWidth(self.button_del_chosen_data.sizePolicy().hasHeightForWidth())
        self.button_del_chosen_data.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.button_del_chosen_data)

        self.button_reset_data = QPushButton(self.tab_data)
        self.button_reset_data.setObjectName(u"button_reset_data")
        sizePolicy2.setHeightForWidth(self.button_reset_data.sizePolicy().hasHeightForWidth())
        self.button_reset_data.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.button_reset_data)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_22.addLayout(self.verticalLayout_9)


        self.verticalLayout_38.addLayout(self.horizontalLayout_22)

        self.tabWidget_main.addTab(self.tab_data, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_8 = QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.treeWidget_corrected_parameters = QTreeWidget(self.tab)
        self.treeWidget_corrected_parameters.setObjectName(u"treeWidget_corrected_parameters")

        self.verticalLayout_6.addWidget(self.treeWidget_corrected_parameters)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.button_up_correcting = QPushButton(self.tab)
        self.button_up_correcting.setObjectName(u"button_up_correcting")

        self.horizontalLayout_18.addWidget(self.button_up_correcting)

        self.button_down_correcting = QPushButton(self.tab)
        self.button_down_correcting.setObjectName(u"button_down_correcting")

        self.horizontalLayout_18.addWidget(self.button_down_correcting)


        self.verticalLayout_6.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_26.addLayout(self.verticalLayout_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.line_corrected_parameters_name = QLineEdit(self.tab)
        self.line_corrected_parameters_name.setObjectName(u"line_corrected_parameters_name")
        sizePolicy2.setHeightForWidth(self.line_corrected_parameters_name.sizePolicy().hasHeightForWidth())
        self.line_corrected_parameters_name.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.line_corrected_parameters_name)

        self.label_23 = QLabel(self.tab)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout.addWidget(self.label_23)

        self.radioButton_gradient = QRadioButton(self.tab)
        self.radioButton_gradient.setObjectName(u"radioButton_gradient")

        self.verticalLayout.addWidget(self.radioButton_gradient)

        self.radioButton_integral = QRadioButton(self.tab)
        self.radioButton_integral.setObjectName(u"radioButton_integral")

        self.verticalLayout.addWidget(self.radioButton_integral)

        self.radioButton_no_extra_operations = QRadioButton(self.tab)
        self.radioButton_no_extra_operations.setObjectName(u"radioButton_no_extra_operations")
        self.radioButton_no_extra_operations.setEnabled(True)
        self.radioButton_no_extra_operations.setChecked(True)
        self.radioButton_no_extra_operations.setAutoRepeat(False)

        self.verticalLayout.addWidget(self.radioButton_no_extra_operations)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.text_edit_correcting_expression = QTextEdit(self.tab)
        self.text_edit_correcting_expression.setObjectName(u"text_edit_correcting_expression")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.text_edit_correcting_expression.sizePolicy().hasHeightForWidth())
        self.text_edit_correcting_expression.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.text_edit_correcting_expression)

        self.button_corrected_parameters_add = QPushButton(self.tab)
        self.button_corrected_parameters_add.setObjectName(u"button_corrected_parameters_add")

        self.verticalLayout.addWidget(self.button_corrected_parameters_add)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.button_corrected_parameters_del = QPushButton(self.tab)
        self.button_corrected_parameters_del.setObjectName(u"button_corrected_parameters_del")

        self.horizontalLayout_17.addWidget(self.button_corrected_parameters_del)

        self.button_corrected_parameters_reset = QPushButton(self.tab)
        self.button_corrected_parameters_reset.setObjectName(u"button_corrected_parameters_reset")

        self.horizontalLayout_17.addWidget(self.button_corrected_parameters_reset)


        self.verticalLayout.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_26.addLayout(self.verticalLayout)


        self.verticalLayout_7.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.button_import_cfg = QPushButton(self.tab)
        self.button_import_cfg.setObjectName(u"button_import_cfg")

        self.horizontalLayout_4.addWidget(self.button_import_cfg)

        self.button_export_cfg = QPushButton(self.tab)
        self.button_export_cfg.setObjectName(u"button_export_cfg")

        self.horizontalLayout_4.addWidget(self.button_export_cfg)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.tabWidget_main.addTab(self.tab, "")
        self.tab_graphs = QWidget()
        self.tab_graphs.setObjectName(u"tab_graphs")
        self.horizontalLayout_23 = QHBoxLayout(self.tab_graphs)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.tab_graphs_list = QTabWidget(self.tab_graphs)
        self.tab_graphs_list.setObjectName(u"tab_graphs_list")
        self.tab_graphs_signle = QWidget()
        self.tab_graphs_signle.setObjectName(u"tab_graphs_signle")
        self.verticalLayout_10 = QVBoxLayout(self.tab_graphs_signle)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.treeWidget_graphs_single = QTreeWidget(self.tab_graphs_signle)
        self.treeWidget_graphs_single.setObjectName(u"treeWidget_graphs_single")
        self.treeWidget_graphs_single.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.treeWidget_graphs_single.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_10.addWidget(self.treeWidget_graphs_single)

        self.tab_graphs_list.addTab(self.tab_graphs_signle, "")
        self.tab_graphs_multy = QWidget()
        self.tab_graphs_multy.setObjectName(u"tab_graphs_multy")
        self.verticalLayout_22 = QVBoxLayout(self.tab_graphs_multy)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.treeWidget_graphs_multy = QTreeWidget(self.tab_graphs_multy)
        self.treeWidget_graphs_multy.setObjectName(u"treeWidget_graphs_multy")
        self.treeWidget_graphs_multy.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.treeWidget_graphs_multy.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_22.addWidget(self.treeWidget_graphs_multy)

        self.tab_graphs_list.addTab(self.tab_graphs_multy, "")

        self.verticalLayout_23.addWidget(self.tab_graphs_list)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.button_up_graphs = QPushButton(self.tab_graphs)
        self.button_up_graphs.setObjectName(u"button_up_graphs")

        self.horizontalLayout_15.addWidget(self.button_up_graphs)

        self.button_down_graphs = QPushButton(self.tab_graphs)
        self.button_down_graphs.setObjectName(u"button_down_graphs")

        self.horizontalLayout_15.addWidget(self.button_down_graphs)


        self.verticalLayout_23.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_16.addLayout(self.verticalLayout_23)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_5 = QLabel(self.tab_graphs)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.line_graphs_y_names = QLineEdit(self.tab_graphs)
        self.line_graphs_y_names.setObjectName(u"line_graphs_y_names")
        sizePolicy2.setHeightForWidth(self.line_graphs_y_names.sizePolicy().hasHeightForWidth())
        self.line_graphs_y_names.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.line_graphs_y_names)

        self.line_graphs_x_names = QLineEdit(self.tab_graphs)
        self.line_graphs_x_names.setObjectName(u"line_graphs_x_names")
        sizePolicy2.setHeightForWidth(self.line_graphs_x_names.sizePolicy().hasHeightForWidth())
        self.line_graphs_x_names.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.line_graphs_x_names)


        self.verticalLayout_14.addLayout(self.horizontalLayout_7)


        self.verticalLayout_13.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_6 = QLabel(self.tab_graphs)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.line_graphs_y_label = QLineEdit(self.tab_graphs)
        self.line_graphs_y_label.setObjectName(u"line_graphs_y_label")
        sizePolicy2.setHeightForWidth(self.line_graphs_y_label.sizePolicy().hasHeightForWidth())
        self.line_graphs_y_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.line_graphs_y_label)

        self.line_graphs_x_label = QLineEdit(self.tab_graphs)
        self.line_graphs_x_label.setObjectName(u"line_graphs_x_label")
        sizePolicy2.setHeightForWidth(self.line_graphs_x_label.sizePolicy().hasHeightForWidth())
        self.line_graphs_x_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.line_graphs_x_label)


        self.verticalLayout_15.addLayout(self.horizontalLayout_8)


        self.verticalLayout_13.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_8 = QLabel(self.tab_graphs)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.line_graphs_y_min = QLineEdit(self.tab_graphs)
        self.line_graphs_y_min.setObjectName(u"line_graphs_y_min")
        sizePolicy2.setHeightForWidth(self.line_graphs_y_min.sizePolicy().hasHeightForWidth())
        self.line_graphs_y_min.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.line_graphs_y_min)

        self.line_graphs_y_max = QLineEdit(self.tab_graphs)
        self.line_graphs_y_max.setObjectName(u"line_graphs_y_max")
        sizePolicy2.setHeightForWidth(self.line_graphs_y_max.sizePolicy().hasHeightForWidth())
        self.line_graphs_y_max.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.line_graphs_y_max)


        self.verticalLayout_16.addLayout(self.horizontalLayout_10)


        self.verticalLayout_13.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_7 = QLabel(self.tab_graphs)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.line_graphs_x_min = QLineEdit(self.tab_graphs)
        self.line_graphs_x_min.setObjectName(u"line_graphs_x_min")
        sizePolicy2.setHeightForWidth(self.line_graphs_x_min.sizePolicy().hasHeightForWidth())
        self.line_graphs_x_min.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.line_graphs_x_min)

        self.line_graphs_x_max = QLineEdit(self.tab_graphs)
        self.line_graphs_x_max.setObjectName(u"line_graphs_x_max")
        sizePolicy2.setHeightForWidth(self.line_graphs_x_max.sizePolicy().hasHeightForWidth())
        self.line_graphs_x_max.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.line_graphs_x_max)


        self.verticalLayout_17.addLayout(self.horizontalLayout_9)


        self.verticalLayout_13.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_10 = QLabel(self.tab_graphs)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.line_graphs_y_mult = QLineEdit(self.tab_graphs)
        self.line_graphs_y_mult.setObjectName(u"line_graphs_y_mult")
        sizePolicy2.setHeightForWidth(self.line_graphs_y_mult.sizePolicy().hasHeightForWidth())
        self.line_graphs_y_mult.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.line_graphs_y_mult)

        self.line_graphs_y_shift = QLineEdit(self.tab_graphs)
        self.line_graphs_y_shift.setObjectName(u"line_graphs_y_shift")
        sizePolicy2.setHeightForWidth(self.line_graphs_y_shift.sizePolicy().hasHeightForWidth())
        self.line_graphs_y_shift.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.line_graphs_y_shift)


        self.verticalLayout_19.addLayout(self.horizontalLayout_12)


        self.verticalLayout_18.addLayout(self.verticalLayout_19)

        self.label_9 = QLabel(self.tab_graphs)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.line_graphs_x_mult = QLineEdit(self.tab_graphs)
        self.line_graphs_x_mult.setObjectName(u"line_graphs_x_mult")
        sizePolicy2.setHeightForWidth(self.line_graphs_x_mult.sizePolicy().hasHeightForWidth())
        self.line_graphs_x_mult.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.line_graphs_x_mult)

        self.line_graphs_x_shift = QLineEdit(self.tab_graphs)
        self.line_graphs_x_shift.setObjectName(u"line_graphs_x_shift")
        sizePolicy2.setHeightForWidth(self.line_graphs_x_shift.sizePolicy().hasHeightForWidth())
        self.line_graphs_x_shift.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.line_graphs_x_shift)


        self.verticalLayout_18.addLayout(self.horizontalLayout_11)


        self.verticalLayout_13.addLayout(self.verticalLayout_18)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_11 = QLabel(self.tab_graphs)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.line_graphs_y_step = QLineEdit(self.tab_graphs)
        self.line_graphs_y_step.setObjectName(u"line_graphs_y_step")
        sizePolicy2.setHeightForWidth(self.line_graphs_y_step.sizePolicy().hasHeightForWidth())
        self.line_graphs_y_step.setSizePolicy(sizePolicy2)

        self.horizontalLayout_13.addWidget(self.line_graphs_y_step)

        self.line_graphs_x_step = QLineEdit(self.tab_graphs)
        self.line_graphs_x_step.setObjectName(u"line_graphs_x_step")
        sizePolicy2.setHeightForWidth(self.line_graphs_x_step.sizePolicy().hasHeightForWidth())
        self.line_graphs_x_step.setSizePolicy(sizePolicy2)

        self.horizontalLayout_13.addWidget(self.line_graphs_x_step)


        self.verticalLayout_20.addLayout(self.horizontalLayout_13)


        self.verticalLayout_13.addLayout(self.verticalLayout_20)

        self.label = QLabel(self.tab_graphs)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label)

        self.text_edit_graphs_description = QTextEdit(self.tab_graphs)
        self.text_edit_graphs_description.setObjectName(u"text_edit_graphs_description")
        sizePolicy3.setHeightForWidth(self.text_edit_graphs_description.sizePolicy().hasHeightForWidth())
        self.text_edit_graphs_description.setSizePolicy(sizePolicy3)

        self.verticalLayout_13.addWidget(self.text_edit_graphs_description)

        self.button_graphs_add = QPushButton(self.tab_graphs)
        self.button_graphs_add.setObjectName(u"button_graphs_add")

        self.verticalLayout_13.addWidget(self.button_graphs_add)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.button_del_chosen_graphs = QPushButton(self.tab_graphs)
        self.button_del_chosen_graphs.setObjectName(u"button_del_chosen_graphs")

        self.horizontalLayout_14.addWidget(self.button_del_chosen_graphs)

        self.button_reset_graphs = QPushButton(self.tab_graphs)
        self.button_reset_graphs.setObjectName(u"button_reset_graphs")

        self.horizontalLayout_14.addWidget(self.button_reset_graphs)


        self.verticalLayout_13.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_16.addLayout(self.verticalLayout_13)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_16)

        self.tabWidget_main.addTab(self.tab_graphs, "")
        self.tab_chrono = QWidget()
        self.tab_chrono.setObjectName(u"tab_chrono")
        self.horizontalLayout_28 = QHBoxLayout(self.tab_chrono)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.tab_chrono_list = QTabWidget(self.tab_chrono)
        self.tab_chrono_list.setObjectName(u"tab_chrono_list")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_34 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.treeWidget_chrono_single = QTreeWidget(self.tab_6)
        self.treeWidget_chrono_single.setObjectName(u"treeWidget_chrono_single")
        self.treeWidget_chrono_single.setSelectionMode(QAbstractItemView.SingleSelection)

        self.horizontalLayout_34.addWidget(self.treeWidget_chrono_single)

        self.tab_chrono_list.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_34 = QVBoxLayout(self.tab_7)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.treeWidget_chrono_multy = QTreeWidget(self.tab_7)
        self.treeWidget_chrono_multy.setObjectName(u"treeWidget_chrono_multy")
        self.treeWidget_chrono_multy.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_34.addWidget(self.treeWidget_chrono_multy)

        self.tab_chrono_list.addTab(self.tab_7, "")

        self.horizontalLayout_28.addWidget(self.tab_chrono_list)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_24 = QLabel(self.tab_chrono)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_24)

        self.line_chrono_parameter_name = QLineEdit(self.tab_chrono)
        self.line_chrono_parameter_name.setObjectName(u"line_chrono_parameter_name")
        sizePolicy2.setHeightForWidth(self.line_chrono_parameter_name.sizePolicy().hasHeightForWidth())
        self.line_chrono_parameter_name.setSizePolicy(sizePolicy2)

        self.verticalLayout_30.addWidget(self.line_chrono_parameter_name)

        self.line_chrono_parameter_value = QLineEdit(self.tab_chrono)
        self.line_chrono_parameter_value.setObjectName(u"line_chrono_parameter_value")
        sizePolicy2.setHeightForWidth(self.line_chrono_parameter_value.sizePolicy().hasHeightForWidth())
        self.line_chrono_parameter_value.setSizePolicy(sizePolicy2)
        self.line_chrono_parameter_value.setMinimumSize(QSize(380, 0))

        self.verticalLayout_30.addWidget(self.line_chrono_parameter_value)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_17 = QLabel(self.tab_chrono)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_17)

        self.line_cut_down_chrono_name = QLineEdit(self.tab_chrono)
        self.line_cut_down_chrono_name.setObjectName(u"line_cut_down_chrono_name")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.line_cut_down_chrono_name.sizePolicy().hasHeightForWidth())
        self.line_cut_down_chrono_name.setSizePolicy(sizePolicy5)

        self.verticalLayout_32.addWidget(self.line_cut_down_chrono_name)

        self.line_cut_down_chrono_value = QLineEdit(self.tab_chrono)
        self.line_cut_down_chrono_value.setObjectName(u"line_cut_down_chrono_value")
        sizePolicy5.setHeightForWidth(self.line_cut_down_chrono_value.sizePolicy().hasHeightForWidth())
        self.line_cut_down_chrono_value.setSizePolicy(sizePolicy5)

        self.verticalLayout_32.addWidget(self.line_cut_down_chrono_value)


        self.verticalLayout_30.addLayout(self.verticalLayout_32)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_18 = QLabel(self.tab_chrono)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_18)

        self.line_cut_up_chrono_name = QLineEdit(self.tab_chrono)
        self.line_cut_up_chrono_name.setObjectName(u"line_cut_up_chrono_name")
        sizePolicy5.setHeightForWidth(self.line_cut_up_chrono_name.sizePolicy().hasHeightForWidth())
        self.line_cut_up_chrono_name.setSizePolicy(sizePolicy5)

        self.verticalLayout_35.addWidget(self.line_cut_up_chrono_name)

        self.line_cut_up_chrono_value = QLineEdit(self.tab_chrono)
        self.line_cut_up_chrono_value.setObjectName(u"line_cut_up_chrono_value")
        sizePolicy5.setHeightForWidth(self.line_cut_up_chrono_value.sizePolicy().hasHeightForWidth())
        self.line_cut_up_chrono_value.setSizePolicy(sizePolicy5)

        self.verticalLayout_35.addWidget(self.line_cut_up_chrono_value)


        self.verticalLayout_30.addLayout(self.verticalLayout_35)

        self.label_29 = QLabel(self.tab_chrono)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_29)

        self.text_edit_chrono_description = QTextEdit(self.tab_chrono)
        self.text_edit_chrono_description.setObjectName(u"text_edit_chrono_description")
        sizePolicy3.setHeightForWidth(self.text_edit_chrono_description.sizePolicy().hasHeightForWidth())
        self.text_edit_chrono_description.setSizePolicy(sizePolicy3)

        self.verticalLayout_30.addWidget(self.text_edit_chrono_description)

        self.button_chrono_parameters_add = QPushButton(self.tab_chrono)
        self.button_chrono_parameters_add.setObjectName(u"button_chrono_parameters_add")

        self.verticalLayout_30.addWidget(self.button_chrono_parameters_add)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.button_del_chosen_chrono_parameters = QPushButton(self.tab_chrono)
        self.button_del_chosen_chrono_parameters.setObjectName(u"button_del_chosen_chrono_parameters")

        self.horizontalLayout_39.addWidget(self.button_del_chosen_chrono_parameters)

        self.button_reset_chrono_parameters = QPushButton(self.tab_chrono)
        self.button_reset_chrono_parameters.setObjectName(u"button_reset_chrono_parameters")

        self.horizontalLayout_39.addWidget(self.button_reset_chrono_parameters)


        self.verticalLayout_30.addLayout(self.horizontalLayout_39)


        self.horizontalLayout_28.addLayout(self.verticalLayout_30)

        self.tabWidget_main.addTab(self.tab_chrono, "")
        self.tab_key_parameters = QWidget()
        self.tab_key_parameters.setObjectName(u"tab_key_parameters")
        self.horizontalLayout_25 = QHBoxLayout(self.tab_key_parameters)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.tab_key_parameters_list = QTabWidget(self.tab_key_parameters)
        self.tab_key_parameters_list.setObjectName(u"tab_key_parameters_list")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_32 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.treeWidget_key_parameters_single = QTreeWidget(self.tab_4)
        self.treeWidget_key_parameters_single.setObjectName(u"treeWidget_key_parameters_single")
        self.treeWidget_key_parameters_single.setSelectionMode(QAbstractItemView.SingleSelection)

        self.horizontalLayout_32.addWidget(self.treeWidget_key_parameters_single)

        self.tab_key_parameters_list.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_33 = QVBoxLayout(self.tab_5)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.treeWidget_key_parameters_multy = QTreeWidget(self.tab_5)
        self.treeWidget_key_parameters_multy.setObjectName(u"treeWidget_key_parameters_multy")
        self.treeWidget_key_parameters_multy.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_33.addWidget(self.treeWidget_key_parameters_multy)

        self.tab_key_parameters_list.addTab(self.tab_5, "")

        self.verticalLayout_24.addWidget(self.tab_key_parameters_list)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.button_up_key_parameters = QPushButton(self.tab_key_parameters)
        self.button_up_key_parameters.setObjectName(u"button_up_key_parameters")

        self.horizontalLayout_24.addWidget(self.button_up_key_parameters)

        self.button_down_key_parameters = QPushButton(self.tab_key_parameters)
        self.button_down_key_parameters.setObjectName(u"button_down_key_parameters")

        self.horizontalLayout_24.addWidget(self.button_down_key_parameters)


        self.verticalLayout_24.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_25.addLayout(self.verticalLayout_24)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_21 = QLabel(self.tab_key_parameters)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_21)

        self.line_key_parameter_name = QLineEdit(self.tab_key_parameters)
        self.line_key_parameter_name.setObjectName(u"line_key_parameter_name")
        sizePolicy2.setHeightForWidth(self.line_key_parameter_name.sizePolicy().hasHeightForWidth())
        self.line_key_parameter_name.setSizePolicy(sizePolicy2)

        self.verticalLayout_31.addWidget(self.line_key_parameter_name)

        self.label_22 = QLabel(self.tab_key_parameters)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_22)

        self.line_search_parameter_name = QLineEdit(self.tab_key_parameters)
        self.line_search_parameter_name.setObjectName(u"line_search_parameter_name")
        sizePolicy2.setHeightForWidth(self.line_search_parameter_name.sizePolicy().hasHeightForWidth())
        self.line_search_parameter_name.setSizePolicy(sizePolicy2)

        self.verticalLayout_31.addWidget(self.line_search_parameter_name)

        self.line_search_parameter_value = QLineEdit(self.tab_key_parameters)
        self.line_search_parameter_value.setObjectName(u"line_search_parameter_value")
        sizePolicy2.setHeightForWidth(self.line_search_parameter_value.sizePolicy().hasHeightForWidth())
        self.line_search_parameter_value.setSizePolicy(sizePolicy2)
        self.line_search_parameter_value.setMinimumSize(QSize(380, 0))

        self.verticalLayout_31.addWidget(self.line_search_parameter_value)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_20 = QLabel(self.tab_key_parameters)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_20)

        self.line_cut_down_key_parameters_name = QLineEdit(self.tab_key_parameters)
        self.line_cut_down_key_parameters_name.setObjectName(u"line_cut_down_key_parameters_name")
        sizePolicy5.setHeightForWidth(self.line_cut_down_key_parameters_name.sizePolicy().hasHeightForWidth())
        self.line_cut_down_key_parameters_name.setSizePolicy(sizePolicy5)

        self.verticalLayout_37.addWidget(self.line_cut_down_key_parameters_name)

        self.line_cut_down_key_parameters_value = QLineEdit(self.tab_key_parameters)
        self.line_cut_down_key_parameters_value.setObjectName(u"line_cut_down_key_parameters_value")
        sizePolicy5.setHeightForWidth(self.line_cut_down_key_parameters_value.sizePolicy().hasHeightForWidth())
        self.line_cut_down_key_parameters_value.setSizePolicy(sizePolicy5)

        self.verticalLayout_37.addWidget(self.line_cut_down_key_parameters_value)


        self.verticalLayout_31.addLayout(self.verticalLayout_37)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_19 = QLabel(self.tab_key_parameters)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_19)

        self.line_cut_up_key_parameters_name = QLineEdit(self.tab_key_parameters)
        self.line_cut_up_key_parameters_name.setObjectName(u"line_cut_up_key_parameters_name")
        sizePolicy5.setHeightForWidth(self.line_cut_up_key_parameters_name.sizePolicy().hasHeightForWidth())
        self.line_cut_up_key_parameters_name.setSizePolicy(sizePolicy5)

        self.verticalLayout_36.addWidget(self.line_cut_up_key_parameters_name)

        self.line_cut_up_key_parameters_value = QLineEdit(self.tab_key_parameters)
        self.line_cut_up_key_parameters_value.setObjectName(u"line_cut_up_key_parameters_value")
        sizePolicy5.setHeightForWidth(self.line_cut_up_key_parameters_value.sizePolicy().hasHeightForWidth())
        self.line_cut_up_key_parameters_value.setSizePolicy(sizePolicy5)

        self.verticalLayout_36.addWidget(self.line_cut_up_key_parameters_value)


        self.verticalLayout_31.addLayout(self.verticalLayout_36)

        self.label_28 = QLabel(self.tab_key_parameters)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_28)

        self.text_edit_key_parameters_description = QTextEdit(self.tab_key_parameters)
        self.text_edit_key_parameters_description.setObjectName(u"text_edit_key_parameters_description")
        sizePolicy3.setHeightForWidth(self.text_edit_key_parameters_description.sizePolicy().hasHeightForWidth())
        self.text_edit_key_parameters_description.setSizePolicy(sizePolicy3)

        self.verticalLayout_31.addWidget(self.text_edit_key_parameters_description)

        self.button_key_parameters_add = QPushButton(self.tab_key_parameters)
        self.button_key_parameters_add.setObjectName(u"button_key_parameters_add")

        self.verticalLayout_31.addWidget(self.button_key_parameters_add)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.button_del_chosen_key_parameters = QPushButton(self.tab_key_parameters)
        self.button_del_chosen_key_parameters.setObjectName(u"button_del_chosen_key_parameters")

        self.horizontalLayout_38.addWidget(self.button_del_chosen_key_parameters)

        self.button_reset_key_parameters = QPushButton(self.tab_key_parameters)
        self.button_reset_key_parameters.setObjectName(u"button_reset_key_parameters")

        self.horizontalLayout_38.addWidget(self.button_reset_key_parameters)


        self.verticalLayout_31.addLayout(self.horizontalLayout_38)


        self.horizontalLayout_25.addLayout(self.verticalLayout_31)

        self.tabWidget_main.addTab(self.tab_key_parameters, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_29 = QVBoxLayout(self.tab_8)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_2 = QLabel(self.tab_8)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)

        self.verticalLayout_27.addWidget(self.label_2)

        self.line_file_save_name = QLineEdit(self.tab_8)
        self.line_file_save_name.setObjectName(u"line_file_save_name")

        self.verticalLayout_27.addWidget(self.line_file_save_name)


        self.verticalLayout_29.addLayout(self.verticalLayout_27)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_14 = QLabel(self.tab_8)
        self.label_14.setObjectName(u"label_14")
        sizePolicy5.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy5)

        self.verticalLayout_26.addWidget(self.label_14)

        self.line_graphs_width = QLineEdit(self.tab_8)
        self.line_graphs_width.setObjectName(u"line_graphs_width")

        self.verticalLayout_26.addWidget(self.line_graphs_width)


        self.verticalLayout_29.addLayout(self.verticalLayout_26)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_16 = QLabel(self.tab_8)
        self.label_16.setObjectName(u"label_16")
        sizePolicy5.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy5)

        self.verticalLayout_28.addWidget(self.label_16)

        self.line_numbers_delim = QLineEdit(self.tab_8)
        self.line_numbers_delim.setObjectName(u"line_numbers_delim")

        self.verticalLayout_28.addWidget(self.line_numbers_delim)


        self.verticalLayout_29.addLayout(self.verticalLayout_28)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_15 = QLabel(self.tab_8)
        self.label_15.setObjectName(u"label_15")
        sizePolicy5.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy5)

        self.verticalLayout_25.addWidget(self.label_15)

        self.line_font_name = QLineEdit(self.tab_8)
        self.line_font_name.setObjectName(u"line_font_name")

        self.verticalLayout_25.addWidget(self.line_font_name)

        self.line_font_value = QLineEdit(self.tab_8)
        self.line_font_value.setObjectName(u"line_font_value")

        self.verticalLayout_25.addWidget(self.line_font_value)


        self.verticalLayout_29.addLayout(self.verticalLayout_25)

        self.checkBox_round_chrono = QCheckBox(self.tab_8)
        self.checkBox_round_chrono.setObjectName(u"checkBox_round_chrono")
        self.checkBox_round_chrono.setChecked(True)

        self.verticalLayout_29.addWidget(self.checkBox_round_chrono)

        self.checkBox_round_key_parameters = QCheckBox(self.tab_8)
        self.checkBox_round_key_parameters.setObjectName(u"checkBox_round_key_parameters")
        self.checkBox_round_key_parameters.setChecked(True)

        self.verticalLayout_29.addWidget(self.checkBox_round_key_parameters)

        self.checkBox_empty_graphs = QCheckBox(self.tab_8)
        self.checkBox_empty_graphs.setObjectName(u"checkBox_empty_graphs")
        self.checkBox_empty_graphs.setChecked(True)

        self.verticalLayout_29.addWidget(self.checkBox_empty_graphs)

        self.frame_4 = QFrame(self.tab_8)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy6)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_29.addWidget(self.frame_4)

        self.tabWidget_main.addTab(self.tab_8, "")

        self.verticalLayout_2.addWidget(self.tabWidget_main)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_path_to_save = QLineEdit(self.widget)
        self.line_path_to_save.setObjectName(u"line_path_to_save")

        self.horizontalLayout.addWidget(self.line_path_to_save)

        self.button_path_save = QPushButton(self.widget)
        self.button_path_save.setObjectName(u"button_path_save")

        self.horizontalLayout.addWidget(self.button_path_save)

        self.button_pre_run = QPushButton(self.widget)
        self.button_pre_run.setObjectName(u"button_pre_run")

        self.horizontalLayout.addWidget(self.button_pre_run)

        self.button_execute = QPushButton(self.widget)
        self.button_execute.setObjectName(u"button_execute")

        self.horizontalLayout.addWidget(self.button_execute)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_21.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)

        self.tabWidget_main.setCurrentIndex(0)
        self.tabs_add_calculatuons.setCurrentIndex(0)
        self.tab_graphs_list.setCurrentIndex(0)
        self.tab_chrono_list.setCurrentIndex(0)
        self.tab_key_parameters_list.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SOCRAT EYE", None))
        self.menu_open_pickle.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u0431\u0438\u043d\u0430\u0440\u043d\u043e\u043c \u0432\u0438\u0434\u0435", None))
        self.menu_transform.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u044c \u0432 \u0431\u0438\u043d\u0430\u0440\u043d\u044b\u0439 \u0432\u0438\u0434", None))
        self.menu_open_help.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0441\u043f\u0440\u0430\u0432\u043a\u0443", None))
        ___qtreewidgetitem = self.treeWidget_calculations.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 \u0441\u0432\u0435\u0440\u0445\u0443", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 \u0441\u043d\u0438\u0437\u0443", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        self.button_up_data.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0440\u0445", None))
        self.button_down_data.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u0437", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 \u0441\u043d\u0438\u0437\u0443", None))
        self.line_cut_down_name.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.line_cut_down_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.line_cut_down_value.setText(QCoreApplication.translate("MainWindow", u"-0.1", None))
        self.line_cut_down_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 \u0441\u0432\u0435\u0440\u0445\u0443", None))
        self.line_cut_up_name.setText(QCoreApplication.translate("MainWindow", u"time", None))
        self.line_cut_up_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.line_cut_up_value.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.line_cut_up_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max)", None))
        self.line_name_calc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.line_path_to_result.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 result", None))
        self.button_path_to_calc.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.button_add_result.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.tabs_add_calculatuons.setTabText(self.tabs_add_calculatuons.indexOf(self.tab_result), QCoreApplication.translate("MainWindow", u"*/RESULT", None))
        self.line_path_to_sackle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a *.sockle", None))
        self.button_path_to_sackle.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.button_add_sackle.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.tabs_add_calculatuons.setTabText(self.tabs_add_calculatuons.indexOf(self.tab_sockle), QCoreApplication.translate("MainWindow", u"*.sockle", None))
        self.button_del_chosen_data.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.button_reset_data.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_data), QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
        ___qtreewidgetitem1 = self.treeWidget_corrected_parameters.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None));
        self.button_up_correcting.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0440\u0445", None))
        self.button_down_correcting.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u0437", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u0443\u0435\u043c\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440", None))
        self.line_corrected_parameters_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.radioButton_gradient.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0444\u0444\u0435\u0440\u0435\u043d\u0446\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.radioButton_integral.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0433\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.radioButton_no_extra_operations.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0437 \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0439", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.button_corrected_parameters_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.button_corrected_parameters_del.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.button_corrected_parameters_reset.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.button_import_cfg.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a", None))
        self.button_export_cfg.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        ___qtreewidgetitem2 = self.treeWidget_graphs_single.headerItem()
        ___qtreewidgetitem2.setText(15, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None));
        ___qtreewidgetitem2.setText(14, QCoreApplication.translate("MainWindow", u"X \u0448\u0430\u0433 \u0441\u0435\u0442\u043a\u0438", None));
        ___qtreewidgetitem2.setText(13, QCoreApplication.translate("MainWindow", u"Y \u0448\u0430\u0433 \u0441\u0435\u0442\u043a\u0438", None));
        ___qtreewidgetitem2.setText(12, QCoreApplication.translate("MainWindow", u"X \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u0435", None));
        ___qtreewidgetitem2.setText(11, QCoreApplication.translate("MainWindow", u"X \u043c\u043d\u043e\u0436\u0438\u0442\u0435\u043b\u044c", None));
        ___qtreewidgetitem2.setText(10, QCoreApplication.translate("MainWindow", u"Y \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u0435", None));
        ___qtreewidgetitem2.setText(9, QCoreApplication.translate("MainWindow", u"Y \u043c\u043d\u043e\u0436\u0438\u0442\u0435\u043b\u044c", None));
        ___qtreewidgetitem2.setText(8, QCoreApplication.translate("MainWindow", u"X \u043e\u0431\u0440\u0435\u0437\u043a\u0430 \u0441\u0432\u0435\u0440\u0445\u0443", None));
        ___qtreewidgetitem2.setText(7, QCoreApplication.translate("MainWindow", u"X \u043e\u0431\u0440\u0435\u0437\u043a\u0430 \u0441\u043d\u0438\u0437\u0443", None));
        ___qtreewidgetitem2.setText(6, QCoreApplication.translate("MainWindow", u"Y \u043e\u0431\u0440\u0435\u0437\u043a\u0430 \u0441\u0432\u0435\u0440\u0445\u0443", None));
        ___qtreewidgetitem2.setText(5, QCoreApplication.translate("MainWindow", u"Y \u043e\u0431\u0440\u0435\u0437\u043a\u0430 \u0441\u043d\u0438\u0437\u0443", None));
        ___qtreewidgetitem2.setText(4, QCoreApplication.translate("MainWindow", u"X \u043f\u043e\u0434\u043f\u0438\u0441\u044c", None));
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("MainWindow", u"Y \u043f\u043e\u0434\u043f\u0438\u0441\u044c", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"X \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"Y \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440", None));
        self.tab_graphs_list.setTabText(self.tab_graphs_list.indexOf(self.tab_graphs_signle), QCoreApplication.translate("MainWindow", u"Single", None))
        ___qtreewidgetitem3 = self.treeWidget_graphs_multy.headerItem()
        ___qtreewidgetitem3.setText(15, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None));
        ___qtreewidgetitem3.setText(14, QCoreApplication.translate("MainWindow", u"X \u0448\u0430\u0433 \u0441\u0435\u0442\u043a\u0438", None));
        ___qtreewidgetitem3.setText(13, QCoreApplication.translate("MainWindow", u"Y \u0448\u0430\u0433 \u0441\u0435\u0442\u043a\u0438", None));
        ___qtreewidgetitem3.setText(12, QCoreApplication.translate("MainWindow", u"X \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u0435", None));
        ___qtreewidgetitem3.setText(11, QCoreApplication.translate("MainWindow", u"X \u043c\u043d\u043e\u0436\u0438\u0442\u0435\u043b\u044c", None));
        ___qtreewidgetitem3.setText(10, QCoreApplication.translate("MainWindow", u"Y \u0441\u043c\u0435\u0449\u0435\u043d\u0438\u0435", None));
        ___qtreewidgetitem3.setText(9, QCoreApplication.translate("MainWindow", u"Y \u043c\u043d\u043e\u0436\u0438\u0442\u0435\u043b\u044c", None));
        ___qtreewidgetitem3.setText(8, QCoreApplication.translate("MainWindow", u"X \u043e\u0431\u0440\u0435\u0437\u043a\u0430 \u0441\u0432\u0435\u0440\u0445\u0443", None));
        ___qtreewidgetitem3.setText(7, QCoreApplication.translate("MainWindow", u"X \u043e\u0431\u0440\u0435\u0437\u043a\u0430 \u0441\u043d\u0438\u0437\u0443", None));
        ___qtreewidgetitem3.setText(6, QCoreApplication.translate("MainWindow", u"Y \u043e\u0431\u0440\u0435\u0437\u043a\u0430 \u0441\u0432\u0435\u0440\u0445\u0443", None));
        ___qtreewidgetitem3.setText(5, QCoreApplication.translate("MainWindow", u"Y \u043e\u0431\u0440\u0435\u0437\u043a\u0430 \u0441\u043d\u0438\u0437\u0443", None));
        ___qtreewidgetitem3.setText(4, QCoreApplication.translate("MainWindow", u"X \u043f\u043e\u0434\u043f\u0438\u0441\u044c", None));
        ___qtreewidgetitem3.setText(3, QCoreApplication.translate("MainWindow", u"Y \u043f\u043e\u0434\u043f\u0438\u0441\u044c", None));
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("MainWindow", u"X \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"Y \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440", None));
        self.tab_graphs_list.setTabText(self.tab_graphs_list.indexOf(self.tab_graphs_multy), QCoreApplication.translate("MainWindow", u"Multy", None))
        self.button_up_graphs.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0440\u0445", None))
        self.button_down_graphs.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u0437", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432", None))
        self.line_graphs_y_names.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u044c Y", None))
        self.line_graphs_x_names.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.line_graphs_x_names.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u044c X", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043f\u0438\u0441\u0438 \u043e\u0441\u0435\u0439", None))
        self.line_graphs_y_label.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u044c Y", None))
        self.line_graphs_x_label.setText(QCoreApplication.translate("MainWindow", u"t, s", None))
        self.line_graphs_x_label.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u044c X", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 \u043f\u043e \u043e\u0441\u0438 Y", None))
        self.line_graphs_y_min.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 Y \u0441\u043d\u0438\u0437\u0443", None))
        self.line_graphs_y_max.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 Y \u0441\u0432\u0435\u0440\u0445\u0443", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 \u043f\u043e \u043e\u0441\u0438 X", None))
        self.line_graphs_x_min.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.line_graphs_x_min.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 X \u0441\u043b\u0435\u0432\u0430", None))
        self.line_graphs_x_max.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 X \u0441\u043f\u0440\u0430\u0432\u0430", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u043a\u0430 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u043f\u043e Y", None))
        self.line_graphs_y_mult.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0423\u043c\u043d\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u043e Y", None))
        self.line_graphs_y_shift.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u043f\u043e Y", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u043a\u0430 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u043f\u043e X", None))
        self.line_graphs_x_mult.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0423\u043c\u043d\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u043e X", None))
        self.line_graphs_x_shift.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u043f\u043e X", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433 \u0441\u0435\u0442\u043a\u0438", None))
        self.line_graphs_y_step.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433 \u0441\u0435\u0442\u043a\u0438 \u043f\u043e Y", None))
        self.line_graphs_x_step.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433 \u0441\u0435\u0442\u043a\u0438 \u043f\u043e X", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.button_graphs_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.button_del_chosen_graphs.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.button_reset_graphs.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_graphs), QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
        ___qtreewidgetitem4 = self.treeWidget_chrono_single.headerItem()
        ___qtreewidgetitem4.setText(4, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None));
        ___qtreewidgetitem4.setText(3, QCoreApplication.translate("MainWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u0432\u0435\u0440\u0445\u0443", None));
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("MainWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u043d\u0438\u0437\u0443", None));
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430", None));
        self.tab_chrono_list.setTabText(self.tab_chrono_list.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Single", None))
        ___qtreewidgetitem5 = self.treeWidget_chrono_multy.headerItem()
        ___qtreewidgetitem5.setText(4, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None));
        ___qtreewidgetitem5.setText(3, QCoreApplication.translate("MainWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u0432\u0435\u0440\u0445\u0443", None));
        ___qtreewidgetitem5.setText(2, QCoreApplication.translate("MainWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u043d\u0438\u0437\u0443", None));
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430", None));
        self.tab_chrono_list.setTabText(self.tab_chrono_list.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Multy", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 ", None))
        self.line_chrono_parameter_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 (TRANSDUCER, TRIP, COMMAND)", None))
        self.line_chrono_parameter_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max, ON_FIRST, ON_LAST, OFF_FIRST, OFF_LAST)", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u043d\u0438\u0437\u0443", None))
        self.line_cut_down_chrono_name.setText("")
        self.line_cut_down_chrono_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.line_cut_down_chrono_value.setText("")
        self.line_cut_down_chrono_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u0432\u0435\u0440\u0445\u0443", None))
        self.line_cut_up_chrono_name.setText("")
        self.line_cut_up_chrono_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.line_cut_up_chrono_value.setText("")
        self.line_cut_up_chrono_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max)", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.button_chrono_parameters_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.button_del_chosen_chrono_parameters.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.button_reset_chrono_parameters.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_chrono), QCoreApplication.translate("MainWindow", u"\u0425\u0440\u043e\u043d\u043e\u043b\u043e\u0433\u0438\u044f", None))
        ___qtreewidgetitem6 = self.treeWidget_key_parameters_single.headerItem()
        ___qtreewidgetitem6.setText(5, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None));
        ___qtreewidgetitem6.setText(4, QCoreApplication.translate("MainWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u0432\u0435\u0440\u0445\u0443", None));
        ___qtreewidgetitem6.setText(3, QCoreApplication.translate("MainWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u043d\u0438\u0437\u0443", None));
        ___qtreewidgetitem6.setText(2, QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None));
        ___qtreewidgetitem6.setText(1, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430", None));
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447\u0435\u0432\u043e\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440", None));
        self.tab_key_parameters_list.setTabText(self.tab_key_parameters_list.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Single", None))
        ___qtreewidgetitem7 = self.treeWidget_key_parameters_multy.headerItem()
        ___qtreewidgetitem7.setText(5, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None));
        ___qtreewidgetitem7.setText(4, QCoreApplication.translate("MainWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u0432\u0435\u0440\u0445\u0443", None));
        ___qtreewidgetitem7.setText(3, QCoreApplication.translate("MainWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u043d\u0438\u0437\u0443", None));
        ___qtreewidgetitem7.setText(2, QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None));
        ___qtreewidgetitem7.setText(1, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430", None));
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447\u0435\u0432\u043e\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440", None));
        self.tab_key_parameters_list.setTabText(self.tab_key_parameters_list.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Multy", None))
        self.button_up_key_parameters.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0440\u0445", None))
        self.button_down_key_parameters.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u0437", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447\u0435\u0432\u043e\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440", None))
        self.line_key_parameter_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 (TRANSDUCER)", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 ", None))
        self.line_search_parameter_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 (TRANSDUCER, TRIP, COMMAND)", None))
        self.line_search_parameter_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max, ON_FIRST, ON_LAST, OFF_FIRST, OFF_LAST)", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u043d\u0438\u0437\u0443", None))
        self.line_cut_down_key_parameters_name.setText("")
        self.line_cut_down_key_parameters_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.line_cut_down_key_parameters_value.setText("")
        self.line_cut_down_key_parameters_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u0432\u0435\u0440\u0445\u0443", None))
        self.line_cut_up_key_parameters_name.setText("")
        self.line_cut_up_key_parameters_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.line_cut_up_key_parameters_value.setText("")
        self.line_cut_up_key_parameters_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max)", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.button_key_parameters_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.button_del_chosen_key_parameters.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.button_reset_key_parameters.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_key_parameters), QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430", None))
        self.line_file_save_name.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.line_file_save_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432", None))
        self.line_graphs_width.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.line_graphs_width.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0441\u043c)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0434\u0440\u043e\u0431\u043d\u043e\u0439 \u0447\u0430\u0441\u0442\u0438", None))
        self.line_numbers_delim.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0448\u0440\u0438\u0444\u0442\u0430", None))
        self.line_font_name.setText(QCoreApplication.translate("MainWindow", u"Times New Roman", None))
        self.line_font_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.line_font_value.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.line_font_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440", None))
        self.checkBox_round_chrono.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0440\u0443\u0433\u043b\u044f\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0432 \u0445\u0440\u043e\u043d\u043e\u043b\u043e\u0433\u0438\u0438", None))
        self.checkBox_round_key_parameters.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0440\u0443\u0433\u043b\u044f\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043a\u043b\u044e\u0447\u0435\u0432\u044b\u0445 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432", None))
        self.checkBox_empty_graphs.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0438\u0441\u043e\u0432\u0430\u0442\u044c \u043f\u0443\u0441\u0442\u044b\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432", None))
        self.line_path_to_save.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432", None))
        self.button_path_save.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.button_pre_run.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0430", None))
        self.button_execute.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
    # retranslateUi

