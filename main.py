import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt  # Add this import statement

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a QLineEdit widget for the display
        self.display = QLineEdit(self)
        self.display.setFixedHeight(40)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        # Create buttons for digits and operators
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create a grid layout for the buttons
        grid_layout = QGridLayout()
        row, col = 0, 0
        for button_text in buttons:
            button = QPushButton(button_text, self)
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Create a vertical layout for the display and buttons
        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(grid_layout)

        self.setLayout(layout)

        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('Simple Calculator')
        self.show()

    def on_button_click(self):
        # Handle button clicks
        button = self.sender()
        current_text = self.display.text()

        if button.text() == '=':
            try:
                result = str(eval(current_text))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        else:
            new_text = current_text + button.text()
            self.display.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('calculator.svg'))
    calc_app = CalculatorApp()
    sys.exit(app.exec_())
