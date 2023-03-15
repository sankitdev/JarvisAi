from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        
        # Create a QVBoxLayout and set it as the layout manager for the form
        layout = QVBoxLayout(Form)
        Form.setLayout(layout)

        # Create a QHBoxLayout for the first row of widgets
        row1Layout = QHBoxLayout()
        layout.addLayout(row1Layout)

        self.ironmanLabel = QtWidgets.QLabel(Form)
        self.ironmanLabel.setStyleSheet("border-radius: 200px;\n"
                                        "background: transparent;")
        self.ironmanLabel.setText("")
        self.ironmanLabel.setPixmap(QtGui.QPixmap("E:\\ankitai\\gui_tools\\ironman-portrait.webp"))
        self.ironmanLabel.setScaledContents(True)
        self.ironmanLabel.setObjectName("ironmanLabel")
        row1Layout.addWidget(self.ironmanLabel)

        self.arcLabel = QtWidgets.QLabel(Form)
        self.arcLabel.setStyleSheet("border-radius: 200px;\n"
                                    "background: transparent;")
        self.arcLabel.setText("")
        self.arcLabel.setPixmap(QtGui.QPixmap("E:\\ankitai\\gui_tools\\techcircle.gif"))
        self.arcLabel.setScaledContents(True)
        self.arcLabel.setObjectName("arcLabel")
        row1Layout.addWidget(self.arcLabel)

        # Create a QHBoxLayout for the second row of widgets
        row2Layout = QHBoxLayout()
        layout.addLayout(row2Layout)

        self.codingLabel = QtWidgets.QLabel(Form)
        self.codingLabel.setStyleSheet("border: none;\n"
                                       "border-radius: 200px;\n"
                                       "background: transparent;")
        self.codingLabel.setText("")
        self.codingLabel.setPixmap(QtGui.QPixmap("E:\\ankitai\\gui_tools\\B.G_Template_1.gif"))
        self.codingLabel.setScaledContents(True)
        self.codingLabel.setObjectName("codingLabel")
        row2Layout.addWidget(self.codingLabel)

        self.kartisTechLabel = QtWidgets.QLabel(Form)
        self.kartisTechLabel.setStyleSheet("\n"
                                            "border-color: rgb(255, 255, 255);\n"
                                            "\n"
                                            "background-color: transparent;")
        self.kartisTechLabel.setText("")
        self.kartisTechLabel.setPixmap(QtGui.QPixmap("E:/ankitai/gui_tools/KartisTechnology(white).png"))
        self.kartisTechLabel.setScaledContents(True)
        self.kartisTechLabel.setObjectName("kartisTechLabel")
        row2Layout.addWidget(self.kartisTechLabel)

        self.backgroundLabel = QtWidgets.QLabel(Form)
        self.backgroundLabel.setText("")
        self.backgroundLabel.setPixmap(QtGui.QPixmap("E:\\ankitai\\gui_tools\\background.gif"))
        self.backgroundLabel.setScaledContents(True)

        layout.addWidget(self.backgroundLabel)

        # Set the minimum size of the form
        Form.setMinimumSize(640, 480)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
