# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chrono_edit_window.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog_chrono_edit(object):
    def setupUi(self, Dialog_chrono_edit):
        if not Dialog_chrono_edit.objectName():
            Dialog_chrono_edit.setObjectName(u"Dialog_chrono_edit")
        Dialog_chrono_edit.resize(400, 588)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_chrono_edit.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Dialog_chrono_edit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_24 = QLabel(Dialog_chrono_edit)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_24)

        self.line_chrono_parameter_name = QLineEdit(Dialog_chrono_edit)
        self.line_chrono_parameter_name.setObjectName(u"line_chrono_parameter_name")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_chrono_parameter_name.sizePolicy().hasHeightForWidth())
        self.line_chrono_parameter_name.setSizePolicy(sizePolicy)

        self.verticalLayout_30.addWidget(self.line_chrono_parameter_name)

        self.line_chrono_parameter_value = QLineEdit(Dialog_chrono_edit)
        self.line_chrono_parameter_value.setObjectName(u"line_chrono_parameter_value")
        sizePolicy.setHeightForWidth(self.line_chrono_parameter_value.sizePolicy().hasHeightForWidth())
        self.line_chrono_parameter_value.setSizePolicy(sizePolicy)
        self.line_chrono_parameter_value.setMinimumSize(QSize(380, 0))

        self.verticalLayout_30.addWidget(self.line_chrono_parameter_value)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_17 = QLabel(Dialog_chrono_edit)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_17)

        self.line_cut_down_chrono_name = QLineEdit(Dialog_chrono_edit)
        self.line_cut_down_chrono_name.setObjectName(u"line_cut_down_chrono_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_cut_down_chrono_name.sizePolicy().hasHeightForWidth())
        self.line_cut_down_chrono_name.setSizePolicy(sizePolicy1)

        self.verticalLayout_32.addWidget(self.line_cut_down_chrono_name)

        self.line_cut_down_chrono_value = QLineEdit(Dialog_chrono_edit)
        self.line_cut_down_chrono_value.setObjectName(u"line_cut_down_chrono_value")
        sizePolicy1.setHeightForWidth(self.line_cut_down_chrono_value.sizePolicy().hasHeightForWidth())
        self.line_cut_down_chrono_value.setSizePolicy(sizePolicy1)

        self.verticalLayout_32.addWidget(self.line_cut_down_chrono_value)


        self.verticalLayout_30.addLayout(self.verticalLayout_32)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_18 = QLabel(Dialog_chrono_edit)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_18)

        self.line_cut_up_chrono_name = QLineEdit(Dialog_chrono_edit)
        self.line_cut_up_chrono_name.setObjectName(u"line_cut_up_chrono_name")
        sizePolicy1.setHeightForWidth(self.line_cut_up_chrono_name.sizePolicy().hasHeightForWidth())
        self.line_cut_up_chrono_name.setSizePolicy(sizePolicy1)

        self.verticalLayout_35.addWidget(self.line_cut_up_chrono_name)

        self.line_cut_up_chrono_value = QLineEdit(Dialog_chrono_edit)
        self.line_cut_up_chrono_value.setObjectName(u"line_cut_up_chrono_value")
        sizePolicy1.setHeightForWidth(self.line_cut_up_chrono_value.sizePolicy().hasHeightForWidth())
        self.line_cut_up_chrono_value.setSizePolicy(sizePolicy1)

        self.verticalLayout_35.addWidget(self.line_cut_up_chrono_value)


        self.verticalLayout_30.addLayout(self.verticalLayout_35)

        self.label_29 = QLabel(Dialog_chrono_edit)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_29)

        self.text_edit_chrono_description = QTextEdit(Dialog_chrono_edit)
        self.text_edit_chrono_description.setObjectName(u"text_edit_chrono_description")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.text_edit_chrono_description.sizePolicy().hasHeightForWidth())
        self.text_edit_chrono_description.setSizePolicy(sizePolicy2)

        self.verticalLayout_30.addWidget(self.text_edit_chrono_description)


        self.verticalLayout.addLayout(self.verticalLayout_30)

        self.buttonBox = QDialogButtonBox(Dialog_chrono_edit)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog_chrono_edit)
        self.buttonBox.accepted.connect(Dialog_chrono_edit.accept)
        self.buttonBox.rejected.connect(Dialog_chrono_edit.reject)

        QMetaObject.connectSlotsByName(Dialog_chrono_edit)
    # setupUi

    def retranslateUi(self, Dialog_chrono_edit):
        Dialog_chrono_edit.setWindowTitle(QCoreApplication.translate("Dialog_chrono_edit", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0445\u0440\u043e\u043d\u043e\u043b\u043e\u0433\u0438\u0438", None))
        self.label_24.setText(QCoreApplication.translate("Dialog_chrono_edit", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 ", None))
        self.line_chrono_parameter_name.setPlaceholderText(QCoreApplication.translate("Dialog_chrono_edit", u"\u0418\u043c\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 (TRANSDUCER, TRIP, COMMAND)", None))
        self.line_chrono_parameter_value.setPlaceholderText(QCoreApplication.translate("Dialog_chrono_edit", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max, ON_FIRST, ON_LAST, OFF_FIRST, OFF_LAST)", None))
        self.label_17.setText(QCoreApplication.translate("Dialog_chrono_edit", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u043d\u0438\u0437\u0443", None))
        self.line_cut_down_chrono_name.setText("")
        self.line_cut_down_chrono_name.setPlaceholderText(QCoreApplication.translate("Dialog_chrono_edit", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.line_cut_down_chrono_value.setText("")
        self.line_cut_down_chrono_value.setPlaceholderText(QCoreApplication.translate("Dialog_chrono_edit", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max)", None))
        self.label_18.setText(QCoreApplication.translate("Dialog_chrono_edit", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u0432\u0435\u0440\u0445\u0443", None))
        self.line_cut_up_chrono_name.setText("")
        self.line_cut_up_chrono_name.setPlaceholderText(QCoreApplication.translate("Dialog_chrono_edit", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.line_cut_up_chrono_value.setText("")
        self.line_cut_up_chrono_value.setPlaceholderText(QCoreApplication.translate("Dialog_chrono_edit", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max)", None))
        self.label_29.setText(QCoreApplication.translate("Dialog_chrono_edit", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
    # retranslateUi

