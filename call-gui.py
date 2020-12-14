import sys
from  PyQt5.QtWidgets import QDialog , QApplication, QFileDialog
from try_image import *
from PyQt5.QtGui import QPixmap
from segmentation_demo import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.chooseImage.clicked.connect(self.choose_process_image)
        self.ui.processButton.clicked.connect(self.show_image)
        self.show()
    
    def choose_process_image(self):
        fname = QFileDialog.getOpenFileName(self,'Open file','/home/samyak/Downloads',"Image files (*.jpg)")
        imagePath = fname[0]
        self.ui.inputImage.setPixmap(QPixmap(imagePath))
        #print(imagePath)
        xyz(imagePath)
    def show_image(self):
        self.ui.outputImage.setPixmap(QPixmap('out_img.jpg'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())


