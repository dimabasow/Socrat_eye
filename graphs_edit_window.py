# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graphs_edit_window.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog_graphs_edit(object):
    def setupUi(self, Dialog_graphs_edit):
        if not Dialog_graphs_edit.objectName():
            Dialog_graphs_edit.setObjectName(u"Dialog_graphs_edit")
        Dialog_graphs_edit.resize(362, 571)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_graphs_edit.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Dialog_graphs_edit)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_5 = QLabel(Dialog_graphs_edit)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.line_graphs_y_names = QLineEdit(Dialog_graphs_edit)
        self.line_graphs_y_names.setObjectName(u"line_graphs_y_names")
        sizePolicy.setHeightForWidth(self.line_graphs_y_names.sizePolicy().hasHeightForWidth())
        self.line_graphs_y_names.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.line_graphs_y_names)

        self.line_graphs_x_names = QLineEdit(Dialog_graphs_edit)
        self.line_graphs_x_names.setObjectName(u"line_graphs_x_names")
        sizePolicy.setHeightForWidth(self.line_graphs_x_names.sizePolicy().hasHeightForWidth())
        self.line_graphs_x_names.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.line_graphs_x_names)


        self.verticalLayout_14.addLayout(self.horizontalLayout_7)


        self.verticalLayout_13.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_6 = QLabel(Dialog_graphs_edit)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.line_graphs_y_label = QLineEdit(Dialog_graphs_edit)
        self.line_graphs_y_label.setObjectName(u"line_graphs_y_label")
        sizePolicy.setHeightForWidth(self.line_graphs_y_label.sizePolicy().hasHeightForWidth())
        self.line_graphs_y_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.line_graphs_y_label)

        self.line_graphs_x_label = QLineEdit(Dialog_graphs_edit)
        self.line_graphs_x_label.setObjectName(u"line_graphs_x_label")
        sizePolicy.setHeightForWidth(self.line_graphs_x_label.sizePolicy().hasHeightForWidth())
        self.line_graphs_x_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.line_graphs_x_label)


        self.verticalLayout_15.addLayout(self.horizontalLayout_8)


        self.verticalLayout_13.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_8 = QLabel(Dialog_graphs_edit)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.line_graphs_y_min = QLineEdit(Dialog_graphs_edit)
        self.line_graphs_y_min.setObjectName(u"line_graphs_y_min")
        sizePolicy.setHeightForWidth(self.line_graphs_y_min.sizePolicy().hasHeightForWidth())
        self.line_graphs_y_min.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.line_graphs_y_min)

        self.line_graphs_y_max = QLineEdit(Dialog_graphs_edit)
        self.line_graphs_y_max.setObjectName(u"line_graphs_y_max")
        sizePolicy.setHeightForWidth(self.line_graphs_y_max.sizePolicy().hasHeightForWidth())
        self.line_graphs_y_max.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.line_graphs_y_max)


        self.verticalLayout_16.addLayout(self.horizontalLayout_10)


        self.verticalLayout_13.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_7 = QLabel(Dialog_graphs_edit)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.line_graphs_x_min = QLineEdit(Dialog_graphs_edit)
        self.line_graphs_x_min.setObjectName(u"line_graphs_x_min")
        sizePolicy.setHeightForWidth(self.line_graphs_x_min.sizePolicy().hasHeightForWidth())
        self.line_graphs_x_min.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.line_graphs_x_min)

        self.line_graphs_x_max = QLineEdit(Dialog_graphs_edit)
        self.line_graphs_x_max.setObjectName(u"line_graphs_x_max")
        sizePolicy.setHeightForWidth(self.line_graphs_x_max.sizePolicy().hasHeightForWidth())
        self.line_graphs_x_max.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.line_graphs_x_max)


        self.verticalLayout_17.addLayout(self.horizontalLayout_9)


        self.verticalLayout_13.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_10 = QLabel(Dialog_graphs_edit)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.line_graphs_y_mult = QLineEdit(Dialog_graphs_edit)
        self.line_graphs_y_mult.setObjectName(u"line_graphs_y_mult")
        sizePolicy.setHeightForWidth(self.line_graphs_y_mult.sizePolicy().hasHeightForWidth())
        self.line_graphs_y_mult.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.line_graphs_y_mult)

        self.line_graphs_y_shift = QLineEdit(Dialog_graphs_edit)
        self.line_graphs_y_shift.setObjectName(u"line_graphs_y_shift")
        sizePolicy.setHeightForWidth(self.line_graphs_y_shift.sizePolicy().hasHeightForWidth())
        self.line_graphs_y_shift.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.line_graphs_y_shift)


        self.verticalLayout_19.addLayout(self.horizontalLayout_12)


        self.verticalLayout_18.addLayout(self.verticalLayout_19)

        self.label_9 = QLabel(Dialog_graphs_edit)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.line_graphs_x_mult = QLineEdit(Dialog_graphs_edit)
        self.line_graphs_x_mult.setObjectName(u"line_graphs_x_mult")
        sizePolicy.setHeightForWidth(self.line_graphs_x_mult.sizePolicy().hasHeightForWidth())
        self.line_graphs_x_mult.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.line_graphs_x_mult)

        self.line_graphs_x_shift = QLineEdit(Dialog_graphs_edit)
        self.line_graphs_x_shift.setObjectName(u"line_graphs_x_shift")
        sizePolicy.setHeightForWidth(self.line_graphs_x_shift.sizePolicy().hasHeightForWidth())
        self.line_graphs_x_shift.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.line_graphs_x_shift)


        self.verticalLayout_18.addLayout(self.horizontalLayout_11)


        self.verticalLayout_13.addLayout(self.verticalLayout_18)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_11 = QLabel(Dialog_graphs_edit)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.line_graphs_y_step = QLineEdit(Dialog_graphs_edit)
        self.line_graphs_y_step.setObjectName(u"line_graphs_y_step")
        sizePolicy.setHeightForWidth(self.line_graphs_y_step.sizePolicy().hasHeightForWidth())
        self.line_graphs_y_step.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.line_graphs_y_step)

        self.line_graphs_x_step = QLineEdit(Dialog_graphs_edit)
        self.line_graphs_x_step.setObjectName(u"line_graphs_x_step")
        sizePolicy.setHeightForWidth(self.line_graphs_x_step.sizePolicy().hasHeightForWidth())
        self.line_graphs_x_step.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.line_graphs_x_step)


        self.verticalLayout_20.addLayout(self.horizontalLayout_13)


        self.verticalLayout_13.addLayout(self.verticalLayout_20)

        self.label = QLabel(Dialog_graphs_edit)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label)

        self.text_edit_graphs_description = QTextEdit(Dialog_graphs_edit)
        self.text_edit_graphs_description.setObjectName(u"text_edit_graphs_description")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.text_edit_graphs_description.sizePolicy().hasHeightForWidth())
        self.text_edit_graphs_description.setSizePolicy(sizePolicy1)

        self.verticalLayout_13.addWidget(self.text_edit_graphs_description)


        self.verticalLayout.addLayout(self.verticalLayout_13)

        self.buttonBox = QDialogButtonBox(Dialog_graphs_edit)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog_graphs_edit)
        self.buttonBox.accepted.connect(Dialog_graphs_edit.accept)
        self.buttonBox.rejected.connect(Dialog_graphs_edit.reject)

        QMetaObject.connectSlotsByName(Dialog_graphs_edit)
    # setupUi

    def retranslateUi(self, Dialog_graphs_edit):
        Dialog_graphs_edit.setWindowTitle(QCoreApplication.translate("Dialog_graphs_edit", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_graphs_edit", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432", None))
        self.line_graphs_y_names.setPlaceholderText(QCoreApplication.translate("Dialog_graphs_edit", u"\u041e\u0441\u044c Y", None))
        self.line_graphs_x_names.setText("")
        self.line_graphs_x_names.setPlaceholderText(QCoreApplication.translate("Dialog_graphs_edit", u"\u041e\u0441\u044c X", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_graphs_edit", u"\u041f\u043e\u0434\u043f\u0438\u0441\u0438 \u043e\u0441\u0435\u0439", None))
        self.line_graphs_y_label.setPlaceholderText(QCoreApplication.translate("Dialog_graphs_edit", u"\u041e\u0441\u044c Y", None))
        self.line_graphs_x_label.setText("")
        self.line_graphs_x_label.setPlaceholderText(QCoreApplication.translate("Dialog_graphs_edit", u"\u041e\u0441\u044c X", None))
        self.label_8.setText(QCoreApplication.translate("Dialog_graphs_edit", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 \u043f\u043e \u043e\u0441\u0438 Y", None))
        self.line_graphs_y_min.setPlaceholderText(QCoreApplication.translate("Dialog_graphs_edit", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 Y \u0441\u043d\u0438\u0437\u0443", None))
        self.line_graphs_y_max.setPlaceholderText(QCoreApplication.translate("Dialog_graphs_edit", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 Y \u0441\u0432\u0435\u0440\u0445\u0443", None))
        self.label_7.setText(QCoreApplication.translate("Dialog_graphs_edit", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 \u043f\u043e \u043e\u0441\u0438 X", None))
        self.line_graphs_x_min.setText("")
        self.line_graphs_x_min.setPlaceholderText(QCoreApplication.translate("Dialog_graphs_edit", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 X \u0441\u043b\u0435\u0432\u0430", None))
        self.line_graphs_x_max.setPlaceholderText(QCoreApplication.translate("Dialog_graphs_edit", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 X \u0441\u043f\u0440\u0430\u0432\u0430", None))
        self.label_10.setText(QCoreApplication.translate("Dialog_graphs_edit", u"\u041a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u043a\u0430 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u043f\u043e Y", None))
        self.line_graphs_y_mult.setPlaceholderText(QCoreApplication.translate("Dialog_graphs_edit", u"\u0423\u043c\u043d\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u043e Y", None))
        self.line_graphs_y_shift.setPlaceholderText(QCoreApplication.translate("Dialog_graphs_edit", u"\u0421\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u043f\u043e Y", None))
        self.label_9.setText(QCoreApplication.translate("Dialog_graphs_edit", u"\u041a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u043a\u0430 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u043f\u043e X", None))
        self.line_graphs_x_mult.setPlaceholderText(QCoreApplication.translate("Dialog_graphs_edit", u"\u0423\u043c\u043d\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u043e X", None))
        self.line_graphs_x_shift.setPlaceholderText(QCoreApplication.translate("Dialog_graphs_edit", u"\u0421\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u043f\u043e X", None))
        self.label_11.setText(QCoreApplication.translate("Dialog_graphs_edit", u"\u0428\u0430\u0433 \u0441\u0435\u0442\u043a\u0438", None))
        self.line_graphs_y_step.setPlaceholderText(QCoreApplication.translate("Dialog_graphs_edit", u"\u0428\u0430\u0433 \u0441\u0435\u0442\u043a\u0438 \u043f\u043e Y", None))
        self.line_graphs_x_step.setPlaceholderText(QCoreApplication.translate("Dialog_graphs_edit", u"\u0428\u0430\u0433 \u0441\u0435\u0442\u043a\u0438 \u043f\u043e X", None))
        self.label.setText(QCoreApplication.translate("Dialog_graphs_edit", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
    # retranslateUi

