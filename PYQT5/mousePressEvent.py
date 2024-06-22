import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor


class Window(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui()
        
        self.x = 10
        self.y = 10 
        
    def ui(self):
        
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("mousePressEvent")  
        
    def mousePressEvent(self, e): #the rectangle goes where mouse is pressed
        
        self.x = e.x()
        self.y = e.y()
        
        self.repaint()
        
    def paintEvent(self, e):
        
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(147,112,219))
        qp.drawRect(self.x,self.y,50,50)
        qp.end()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())