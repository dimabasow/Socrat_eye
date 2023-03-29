# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'correcting_edit_window.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog_correcting_edit(object):
    def setupUi(self, Dialog_correcting_edit):
        if not Dialog_correcting_edit.objectName():
            Dialog_correcting_edit.setObjectName(u"Dialog_correcting_edit")
        Dialog_correcting_edit.resize(486, 717)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_correcting_edit.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Dialog_correcting_edit)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(Dialog_correcting_edit)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.line_corrected_parameters_name = QLineEdit(Dialog_correcting_edit)
        self.line_corrected_parameters_name.setObjectName(u"line_corrected_parameters_name")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_corrected_parameters_name.sizePolicy().hasHeightForWidth())
        self.line_corrected_parameters_name.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.line_corrected_parameters_name)

        self.label_23 = QLabel(Dialog_correcting_edit)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout.addWidget(self.label_23)

        self.radioButton_gradient = QRadioButton(Dialog_correcting_edit)
        self.radioButton_gradient.setObjectName(u"radioButton_gradient")

        self.verticalLayout.addWidget(self.radioButton_gradient)

        self.radioButton_integral = QRadioButton(Dialog_correcting_edit)
        self.radioButton_integral.setObjectName(u"radioButton_integral")
        self.radioButton_integral.setChecked(False)

        self.verticalLayout.addWidget(self.radioButton_integral)

        self.radioButton_no_extra_operations = QRadioButton(Dialog_correcting_edit)
        self.radioButton_no_extra_operations.setObjectName(u"radioButton_no_extra_operations")
        self.radioButton_no_extra_operations.setEnabled(True)
        self.radioButton_no_extra_operations.setChecked(True)
        self.radioButton_no_extra_operations.setAutoRepeat(False)

        self.verticalLayout.addWidget(self.radioButton_no_extra_operations)

        self.label_3 = QLabel(Dialog_correcting_edit)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.text_edit_correcting_expression = QTextEdit(Dialog_correcting_edit)
        self.text_edit_correcting_expression.setObjectName(u"text_edit_correcting_expression")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.text_edit_correcting_expression.sizePolicy().hasHeightForWidth())
        self.text_edit_correcting_expression.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.text_edit_correcting_expression)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(Dialog_correcting_edit)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog_correcting_edit)
        self.buttonBox.accepted.connect(Dialog_correcting_edit.accept)
        self.buttonBox.rejected.connect(Dialog_correcting_edit.reject)

        QMetaObject.connectSlotsByName(Dialog_correcting_edit)
    # setupUi

    def retranslateUi(self, Dialog_correcting_edit):
        Dialog_correcting_edit.setWindowTitle(QCoreApplication.translate("Dialog_correcting_edit", u"\u041a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u0443\u0435\u043c\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_correcting_edit", u"\u041a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u0443\u0435\u043c\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440", None))
        self.line_corrected_parameters_name.setPlaceholderText(QCoreApplication.translate("Dialog_correcting_edit", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.label_23.setText(QCoreApplication.translate("Dialog_correcting_edit", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.radioButton_gradient.setText(QCoreApplication.translate("Dialog_correcting_edit", u"\u0414\u0438\u0444\u0444\u0435\u0440\u0435\u043d\u0446\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.radioButton_integral.setText(QCoreApplication.translate("Dialog_correcting_edit", u"\u0418\u043d\u0442\u0435\u0433\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.radioButton_no_extra_operations.setText(QCoreApplication.translate("Dialog_correcting_edit", u"\u0411\u0435\u0437 \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0439", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_correcting_edit", u"\u0412\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
    # retranslateUi

