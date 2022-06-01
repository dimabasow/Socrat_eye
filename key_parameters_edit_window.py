# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'key_parameters_edit_window.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog_key_parameters_edit(object):
    def setupUi(self, Dialog_key_parameters_edit):
        if not Dialog_key_parameters_edit.objectName():
            Dialog_key_parameters_edit.setObjectName(u"Dialog_key_parameters_edit")
        Dialog_key_parameters_edit.resize(511, 719)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_key_parameters_edit.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Dialog_key_parameters_edit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_21 = QLabel(Dialog_key_parameters_edit)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_21)

        self.line_key_parameter_name = QLineEdit(Dialog_key_parameters_edit)
        self.line_key_parameter_name.setObjectName(u"line_key_parameter_name")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_key_parameter_name.sizePolicy().hasHeightForWidth())
        self.line_key_parameter_name.setSizePolicy(sizePolicy)

        self.verticalLayout_31.addWidget(self.line_key_parameter_name)

        self.label_22 = QLabel(Dialog_key_parameters_edit)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_22)

        self.line_search_parameter_name = QLineEdit(Dialog_key_parameters_edit)
        self.line_search_parameter_name.setObjectName(u"line_search_parameter_name")
        sizePolicy.setHeightForWidth(self.line_search_parameter_name.sizePolicy().hasHeightForWidth())
        self.line_search_parameter_name.setSizePolicy(sizePolicy)

        self.verticalLayout_31.addWidget(self.line_search_parameter_name)

        self.line_search_parameter_value = QLineEdit(Dialog_key_parameters_edit)
        self.line_search_parameter_value.setObjectName(u"line_search_parameter_value")
        sizePolicy.setHeightForWidth(self.line_search_parameter_value.sizePolicy().hasHeightForWidth())
        self.line_search_parameter_value.setSizePolicy(sizePolicy)
        self.line_search_parameter_value.setMinimumSize(QSize(380, 0))

        self.verticalLayout_31.addWidget(self.line_search_parameter_value)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_20 = QLabel(Dialog_key_parameters_edit)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_20)

        self.line_cut_down_key_parameters_name = QLineEdit(Dialog_key_parameters_edit)
        self.line_cut_down_key_parameters_name.setObjectName(u"line_cut_down_key_parameters_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_cut_down_key_parameters_name.sizePolicy().hasHeightForWidth())
        self.line_cut_down_key_parameters_name.setSizePolicy(sizePolicy1)

        self.verticalLayout_37.addWidget(self.line_cut_down_key_parameters_name)

        self.line_cut_down_key_parameters_value = QLineEdit(Dialog_key_parameters_edit)
        self.line_cut_down_key_parameters_value.setObjectName(u"line_cut_down_key_parameters_value")
        sizePolicy1.setHeightForWidth(self.line_cut_down_key_parameters_value.sizePolicy().hasHeightForWidth())
        self.line_cut_down_key_parameters_value.setSizePolicy(sizePolicy1)

        self.verticalLayout_37.addWidget(self.line_cut_down_key_parameters_value)


        self.verticalLayout_31.addLayout(self.verticalLayout_37)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_19 = QLabel(Dialog_key_parameters_edit)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_19)

        self.line_cut_up_key_parameters_name = QLineEdit(Dialog_key_parameters_edit)
        self.line_cut_up_key_parameters_name.setObjectName(u"line_cut_up_key_parameters_name")
        sizePolicy1.setHeightForWidth(self.line_cut_up_key_parameters_name.sizePolicy().hasHeightForWidth())
        self.line_cut_up_key_parameters_name.setSizePolicy(sizePolicy1)

        self.verticalLayout_36.addWidget(self.line_cut_up_key_parameters_name)

        self.line_cut_up_key_parameters_value = QLineEdit(Dialog_key_parameters_edit)
        self.line_cut_up_key_parameters_value.setObjectName(u"line_cut_up_key_parameters_value")
        sizePolicy1.setHeightForWidth(self.line_cut_up_key_parameters_value.sizePolicy().hasHeightForWidth())
        self.line_cut_up_key_parameters_value.setSizePolicy(sizePolicy1)

        self.verticalLayout_36.addWidget(self.line_cut_up_key_parameters_value)


        self.verticalLayout_31.addLayout(self.verticalLayout_36)

        self.label_28 = QLabel(Dialog_key_parameters_edit)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_28)

        self.text_edit_key_parameters_description = QTextEdit(Dialog_key_parameters_edit)
        self.text_edit_key_parameters_description.setObjectName(u"text_edit_key_parameters_description")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.text_edit_key_parameters_description.sizePolicy().hasHeightForWidth())
        self.text_edit_key_parameters_description.setSizePolicy(sizePolicy2)

        self.verticalLayout_31.addWidget(self.text_edit_key_parameters_description)


        self.verticalLayout.addLayout(self.verticalLayout_31)

        self.buttonBox = QDialogButtonBox(Dialog_key_parameters_edit)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog_key_parameters_edit)
        self.buttonBox.accepted.connect(Dialog_key_parameters_edit.accept)
        self.buttonBox.rejected.connect(Dialog_key_parameters_edit.reject)

        QMetaObject.connectSlotsByName(Dialog_key_parameters_edit)
    # setupUi

    def retranslateUi(self, Dialog_key_parameters_edit):
        Dialog_key_parameters_edit.setWindowTitle(QCoreApplication.translate("Dialog_key_parameters_edit", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043a\u043b\u044e\u0447\u0435\u0432\u044b\u0445 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432", None))
        self.label_21.setText(QCoreApplication.translate("Dialog_key_parameters_edit", u"\u041a\u043b\u044e\u0447\u0435\u0432\u043e\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440", None))
        self.line_key_parameter_name.setPlaceholderText(QCoreApplication.translate("Dialog_key_parameters_edit", u"\u0418\u043c\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 (TRANSDUCER)", None))
        self.label_22.setText(QCoreApplication.translate("Dialog_key_parameters_edit", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 ", None))
        self.line_search_parameter_name.setPlaceholderText(QCoreApplication.translate("Dialog_key_parameters_edit", u"\u0418\u043c\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 (TRANSDUCER, TRIP, COMMAND)", None))
        self.line_search_parameter_value.setPlaceholderText(QCoreApplication.translate("Dialog_key_parameters_edit", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max, ON_FIRST, ON_LAST, OFF_FIRST, OFF_LAST)", None))
        self.label_20.setText(QCoreApplication.translate("Dialog_key_parameters_edit", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u043d\u0438\u0437\u0443", None))
        self.line_cut_down_key_parameters_name.setText("")
        self.line_cut_down_key_parameters_name.setPlaceholderText(QCoreApplication.translate("Dialog_key_parameters_edit", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.line_cut_down_key_parameters_value.setText("")
        self.line_cut_down_key_parameters_value.setPlaceholderText(QCoreApplication.translate("Dialog_key_parameters_edit", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max)", None))
        self.label_19.setText(QCoreApplication.translate("Dialog_key_parameters_edit", u"\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0441\u0432\u0435\u0440\u0445\u0443", None))
        self.line_cut_up_key_parameters_name.setText("")
        self.line_cut_up_key_parameters_name.setPlaceholderText(QCoreApplication.translate("Dialog_key_parameters_edit", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.line_cut_up_key_parameters_value.setText("")
        self.line_cut_up_key_parameters_value.setPlaceholderText(QCoreApplication.translate("Dialog_key_parameters_edit", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max)", None))
        self.label_28.setText(QCoreApplication.translate("Dialog_key_parameters_edit", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
    # retranslateUi

