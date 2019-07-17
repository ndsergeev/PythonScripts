from PySide2.QtWidgets import QPushButton, QLabel, QLineEdit
from PySide2.QtWidgets import QApplication, QHBoxLayout
from PySide2.QtWidgets import QFileDialog, QTextEdit, QSizePolicy
from PySide2.QtWidgets import QMainWindow, QWidget, QGridLayout
from PySide2 import QtCore, QtGui
import sys

class MainWindow(QLabel):
    WIDTH = 400
    HEIGHT = 210
    MIN_WIDGET_SIZE = 22
    MIN_APP_WIDTH = 220
    BUTTON_HEIGHT = 34
    BUTTON_WIDTH = 55
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.clipboard = QApplication.clipboard()
        
        # GUI definition
        self.central_widget = QWidget(self)
        self.layout_grid = QGridLayout(self.central_widget)
        self.layout_grid.setSpacing(5)
        
        self.label_windws = QLabel()
        self.line_edit_windws = QLineEdit()
        self.button_copy_windws = QPushButton('Copy')
        
        self.label_debian = QLabel()
        self.line_edit_debian = QLineEdit()
        self.button_copy_debian = QPushButton('Copy')
        
        self.layout_grid.addWidget(self.label_windws, 1, 0)
        self.layout_grid.addWidget(self.line_edit_windws, 2, 0)
        self.layout_grid.addWidget(self.button_copy_windws, 2, 1)
        
        self.layout_grid.addWidget(self.label_debian, 3, 0)
        self.layout_grid.addWidget(self.line_edit_debian, 4, 0)
        self.layout_grid.addWidget(self.button_copy_debian, 4, 1)
        
        # Description of all Widgets above:
        self.setupUi()
        
        # Delete Window on close button
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    
    def setupUi(self):
        self.setWindowTitle('Path converter')
        self.resize(self.WIDTH, self.HEIGHT)
        
        self.label_windws.setObjectName("label_windws")
        
        self.line_edit_windws.setObjectName("line_edit_windws")
        self.line_edit_windws.setMinimumSize(QtCore.QSize(self.MIN_APP_WIDTH, self.MIN_WIDGET_SIZE))
        self.line_edit_windws.textChanged.connect(self.convert_line_edit_debian)
        
        self.button_copy_windws.setMinimumSize(QtCore.QSize(self.BUTTON_WIDTH, self.BUTTON_HEIGHT))
        self.button_copy_windws.setMaximumSize(QtCore.QSize(self.BUTTON_WIDTH, self.BUTTON_HEIGHT))
        self.button_copy_windws.setCheckable(False)
        self.button_copy_windws.setObjectName("button_copy_windws")
        self.button_copy_windws.clicked.connect(self.on_click_button_copy_windws)
        
        self.label_debian.setObjectName("label_debian")
        
        self.line_edit_debian.setObjectName("line_edit_debian")
        self.line_edit_debian.setMinimumSize(QtCore.QSize(self.MIN_APP_WIDTH, self.MIN_WIDGET_SIZE))
        self.line_edit_debian.textChanged.connect(self.convert_line_edit_windws)
        
        self.button_copy_debian.setMinimumSize(QtCore.QSize(self.BUTTON_WIDTH, self.BUTTON_HEIGHT))
        self.button_copy_debian.setMaximumSize(QtCore.QSize(self.BUTTON_WIDTH, self.BUTTON_HEIGHT))
        self.button_copy_debian.setCheckable(False)
        self.button_copy_debian.setObjectName("button_copy_debian")
        self.button_copy_debian.clicked.connect(self.on_click_button_copy_debian)
        
        self.line_edit_windws.setFocus()
        
        self.retranslateUI()
        self.retranslateUIStyleSheet()
        
        # Button deactivation if no pyperclip module
        try: import pyperclip
        except ImportError:
            self.button_copy_windws.setEnabled(False)
            self.button_copy_debian.setEnabled(False)
            self.button_copy_windws.setStyleSheet("color: rgb(255, 153, 153);")
            self.button_copy_debian.setStyleSheet("color: rgb(255, 153, 153);")
            self.label_3 = QLabel('Install pyperclip module to copy using button!')
            self.label_3.setStyleSheet("color: rgb(255, 153, 153);")
            self.layout_grid.addWidget(self.label_3, 5, 0)
        
        self.setLayout(self.layout_grid)
    
    # Change text var if needed:
    def retranslateUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_windws.setText(_translate("MainWindow", "Windows Path"))
        self.label_debian.setText(_translate("MainWindow", "Debian Path"))
    
    # Custom palette if needed:
    def retranslateUIStyleSheet(self):
        self.label_windws.setStyleSheet("color: rgb(255, 153, 0);")
        self.label_debian.setStyleSheet("color: rgb(255, 153, 0);")
        self.button_copy_windws.setStyleSheet("color: rgb(255, 153, 0);")
        self.button_copy_debian.setStyleSheet("color: rgb(255, 153, 0);")
    # or
    # self.setStyleSheet(hou.qt.styleSheet())
    # self.setProperty("houdiniStyle", True)
    
    def on_click_button_copy_windws(self):
        try: pyperclip.copy(self.line_edit_windws.text())
        except ImportError: pass
    
    def on_click_button_copy_debian(self):
        try: pyperclip.copy(self.line_edit_debian.text())
        except ImportError: pass
    
    def convert_line_edit_windws(self):
        if self.line_edit_debian.isModified():
            # Change your Debian path to Windows
            self.line_edit_windws.setText(self.line_edit_debian.text()+'Windows')

    def convert_line_edit_debian(self):
        if self.line_edit_windws.isModified():
            # Change your Windows path to Debian
            self.line_edit_debian.setText(self.line_edit_windws.text()+'Debian')

    
    def run(self):
        self.show()
        pyqt_app.exec_()

if __name__ == '__main__':
    pyqt_app = QApplication(sys.argv)
    MainWindow().run()
