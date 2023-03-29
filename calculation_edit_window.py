# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculation_edit_window.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog_calculation_edit(object):
    def setupUi(self, Dialog_calculation_edit):
        if not Dialog_calculation_edit.objectName():
            Dialog_calculation_edit.setObjectName(u"Dialog_calculation_edit")
        Dialog_calculation_edit.resize(433, 370)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_calculation_edit.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(Dialog_calculation_edit)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog_calculation_edit)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.line_calculation_name = QLineEdit(Dialog_calculation_edit)
        self.line_calculation_name.setObjectName(u"line_calculation_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_calculation_name.sizePolicy().hasHeightForWidth())
        self.line_calculation_name.setSizePolicy(sizePolicy1)
        self.line_calculation_name.setReadOnly(True)

        self.horizontalLayout.addWidget(self.line_calculation_name)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Dialog_calculation_edit)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_calculation_path = QLineEdit(Dialog_calculation_edit)
        self.line_calculation_path.setObjectName(u"line_calculation_path")
        sizePolicy1.setHeightForWidth(self.line_calculation_path.sizePolicy().hasHeightForWidth())
        self.line_calculation_path.setSizePolicy(sizePolicy1)
        self.line_calculation_path.setMinimumSize(QSize(380, 0))
        self.line_calculation_path.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.line_calculation_path)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_17 = QLabel(Dialog_calculation_edit)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_17)

        self.line_cut_down_calculation_name = QLineEdit(Dialog_calculation_edit)
        self.line_cut_down_calculation_name.setObjectName(u"line_cut_down_calculation_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_cut_down_calculation_name.sizePolicy().hasHeightForWidth())
        self.line_cut_down_calculation_name.setSizePolicy(sizePolicy2)

        self.verticalLayout_32.addWidget(self.line_cut_down_calculation_name)

        self.line_cut_down_calculation_value = QLineEdit(Dialog_calculation_edit)
        self.line_cut_down_calculation_value.setObjectName(u"line_cut_down_calculation_value")
        sizePolicy2.setHeightForWidth(self.line_cut_down_calculation_value.sizePolicy().hasHeightForWidth())
        self.line_cut_down_calculation_value.setSizePolicy(sizePolicy2)

        self.verticalLayout_32.addWidget(self.line_cut_down_calculation_value)


        self.verticalLayout_2.addLayout(self.verticalLayout_32)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_18 = QLabel(Dialog_calculation_edit)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_18)

        self.line_cut_up_calculation_name = QLineEdit(Dialog_calculation_edit)
        self.line_cut_up_calculation_name.setObjectName(u"line_cut_up_calculation_name")
        sizePolicy2.setHeightForWidth(self.line_cut_up_calculation_name.sizePolicy().hasHeightForWidth())
        self.line_cut_up_calculation_name.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.line_cut_up_calculation_name)

        self.line_cut_up_calculation_value = QLineEdit(Dialog_calculation_edit)
        self.line_cut_up_calculation_value.setObjectName(u"line_cut_up_calculation_value")
        sizePolicy2.setHeightForWidth(self.line_cut_up_calculation_value.sizePolicy().hasHeightForWidth())
        self.line_cut_up_calculation_value.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.line_cut_up_calculation_value)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.frame = QFrame(Dialog_calculation_edit)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(Dialog_calculation_edit)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.retranslateUi(Dialog_calculation_edit)
        self.buttonBox.accepted.connect(Dialog_calculation_edit.accept)
        self.buttonBox.rejected.connect(Dialog_calculation_edit.reject)

        QMetaObject.connectSlotsByName(Dialog_calculation_edit)
    # setupUi

    def retranslateUi(self, Dialog_calculation_edit):
        Dialog_calculation_edit.setWindowTitle(QCoreApplication.translate("Dialog_calculation_edit", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u0440\u0430\u0441\u0447\u0451\u0442\u043e\u0432", None))
        self.label.setText(QCoreApplication.translate("Dialog_calculation_edit", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.line_calculation_name.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("Dialog_calculation_edit", u"\u041f\u0443\u0442\u044c", None))
        self.line_calculation_path.setPlaceholderText("")
        self.label_17.setText(QCoreApplication.translate("Dialog_calculation_edit", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 \u0441\u043d\u0438\u0437\u0443", None))
        self.line_cut_down_calculation_name.setText("")
        self.line_cut_down_calculation_name.setPlaceholderText(QCoreApplication.translate("Dialog_calculation_edit", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.line_cut_down_calculation_value.setText("")
        self.line_cut_down_calculation_value.setPlaceholderText(QCoreApplication.translate("Dialog_calculation_edit", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max)", None))
        self.label_18.setText(QCoreApplication.translate("Dialog_calculation_edit", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 \u0441\u0432\u0435\u0440\u0445\u0443", None))
        self.line_cut_up_calculation_name.setText("")
        self.line_cut_up_calculation_name.setPlaceholderText(QCoreApplication.translate("Dialog_calculation_edit", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.line_cut_up_calculation_value.setText("")
        self.line_cut_up_calculation_value.setPlaceholderText(QCoreApplication.translate("Dialog_calculation_edit", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (\u0447\u0438\u0441\u043b\u043e, min, max)", None))
    # retranslateUi

