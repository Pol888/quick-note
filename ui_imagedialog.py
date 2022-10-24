from datetime import datetime
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ImageDialog(object):
    def setupUi(self, ImageDialog):
        ImageDialog.setObjectName("ImageDialog")
        ImageDialog.resize(866, 638)
        font = QtGui.QFont()
        font.setPointSize(20)
        ImageDialog.setFont(font)
        ImageDialog.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.lcdNumber = QtWidgets.QLCDNumber(ImageDialog)
        self.lcdNumber.setGeometry(QtCore.QRect(280, 0, 581, 91))
        self.lcdNumber.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lcdNumber.setLineWidth(2)
        self.lcdNumber.setMidLineWidth(3)
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(21)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Mode.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton = QtWidgets.QPushButton(ImageDialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 470, 221, 131))
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(ImageDialog)
        self.frame.setGeometry(QtCore.QRect(130, 120, 81, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(ImageDialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 140, 801, 301))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(ImageDialog)
        QtCore.QMetaObject.connectSlotsByName(ImageDialog)

    def retranslateUi(self, ImageDialog):
        _translate = QtCore.QCoreApplication.translate
        ImageDialog.setWindowTitle(_translate("ImageDialog", "Hello Friend"))
        self.pushButton.setText(_translate("ImageDialog", "Нажми меня"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageDialog = QtWidgets.QDialog()
    ui = Ui_ImageDialog()
    ui.setupUi(ImageDialog)
    ImageDialog.show()

    ui.lcdNumber.display(datetime.today().strftime('%d-%m-%Y %H-%M-%S'))  # выводит на lcdNumber текушую дату и время.


    def on_click():
        print('Работает!!!!')
        # form.textEdit.toPlainText() # берет вводимый текс из textEdit панели.

        with open('filessss.txt', 'a', encoding='utf-8') as file888:  # запись в текстовый файл.

            print(f"\n{datetime.today().strftime('%d-%m-%Y %H-%M-%S')}\n{ui.textEdit.toPlainText()}", file=file888)


    ui.pushButton.clicked.connect(on_click)

    sys.exit(app.exec())
