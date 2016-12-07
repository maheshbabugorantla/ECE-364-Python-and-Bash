from PySide.QtCore import *
from PySide.QtGui import *

from calculator import *

class simpleMath(QMainWindow,Ui_Calculator):

    def __init__(self, parent=None):
        super(simpleMath, self).__init__(parent)
        self.setupUi(self)

        self.operand1 = 0
        self.operand2 = 0
        self.keyStrokes = 1
        self.numStrokes = 0
        self.operator = "+" # Default Operator
        self.expr = ""
        self.newFlag = 0 # To check if an operator is pressed
        self.decimalFlag = 0

        # flags for take input input operands
        self.opflag1 = 0

        #self.numStrokes = 0

        self.txtDisplay.setText("0.")

        # Connecting all the Buttons

        # To pass an argument in the slot we need to construct a lambda expression because
        # in general clicked() accepts a callable object as its argument. The Lambda expression
        # which is basically an anonymous function, is one such callable object.

        # Numbers
        self.btn0.clicked.connect(lambda: self.displayInput("0"))
        self.btn1.clicked.connect(lambda: self.displayInput("1"))
        self.btn2.clicked.connect(lambda: self.displayInput("2"))
        self.btn3.clicked.connect(lambda: self.displayInput("3"))
        self.btn4.clicked.connect(lambda: self.displayInput("4"))
        self.btn5.clicked.connect(lambda: self.displayInput("5"))
        self.btn6.clicked.connect(lambda: self.displayInput("6"))
        self.btn7.clicked.connect(lambda: self.displayInput("7"))
        self.btn8.clicked.connect(lambda: self.displayInput("8"))
        self.btn9.clicked.connect(lambda: self.displayInput("9"))

        # Decimal Dot
        self.btnDot.clicked.connect(lambda: self.displayInput("."))

        # Operators
        self.btnPlus.clicked.connect(lambda: self.compute("+"))
        self.btnMinus.clicked.connect(lambda: self.compute("-"))
        self.btnMultiply.clicked.connect(lambda: self.compute("*"))
        self.btnDivide.clicked.connect(lambda: self.compute("/"))

        # Result
        self.btnEqual.clicked.connect(lambda: self.displayResult())

        # Clear the Result
        self.btnClear.clicked.connect(lambda: self.compute("C"))


    def displayInput(self, val):

        if self.newFlag == 0:
            self.expr += val

        else:
            self.newFlag = 0 # Resetting the Flag
            self.expr = val


        self.numStrokes += 1
        self.txtDisplay.setText(self.expr)

        # Debug
        print(self.expr)

    def compute(self, operator):

        self.newFlag = 1

        if operator == "C":

            if len(self.expr) <= 1:
                self.txtDisplay.setText("0.")
                self.operand1 = 0
                self.operand2 = 0
                self.keyStrokes = 0
                self.numStrokes = 0
                self.opflag1 = 0
                return
            else:
                self.expr = self.expr[:-1] # This makes sure that we delete the last entered digit
                self.txtDisplay.setText(self.expr)

        print("keyStrokes: " + str(self.keyStrokes))

        # Choosing which operand to store
        if self.opflag1 == 0:
            self.operand1 = int(self.expr)
            #self.numStrokes += 1
            print("Operand1 = " + str(self.operand1))

        else:
            self.operand2 = int(self.expr)
            self.keyStrokes += 1
            #self.numStrokes += 1
            print("Operand2 = " + str(self.operand2))

        # Choosing operator
        if operator == "+":
            print("Inside +")

            if self.keyStrokes == 2:
                self.operand1 += self.operand2
                self.txtDisplay.setText(str(self.operand1))
                self.keyStrokes = 1

            else:
                self.operator = operator

            self.opflag1 = 1 # Time to get new Operand

        elif operator == "-": # Think of Negation

            print("Inside -")

            if self.keyStrokes == 2:
                self.operand1 -= self.operand2
                self.txtDisplay.setText(str(self.operand1))
                self.keyStrokes = 1

            else:
                self.operator = operator
                #self.keyStrokes += 1

            self.opflag1 = 1 # Time to get new Operand

        elif operator == "*":

            print("Inside *")

            if self.keyStrokes == 2:
                self.operand1 *= self.operand2
                self.txtDisplay.setText(str(self.operand1))
                self.keyStrokes = 1

            else:
                self.operator = operator

            self.opflag1 = 1

        elif operator == "/":

                print("Inside /")

                if self.keyStrokes == 2:
                    self.operand1 /= self.operand2
                    self.txtDisplay.setText(str(self.operand1))
                    self.keyStrokes = 1

                else:
                    self.operator = operator

                self.opflag1 = 1

    def displayResult(self):
        self.keyStrokes = 1 # Resetting the Keystrokes
        print("= Sign")

        if(self.operator == "+"):
            self.operand1 += self.operand2
            self.txtDisplay.setText(str(self.operand1))

def main():
    currentApp = QApplication([])
    currentForm = simpleMath()
    currentForm.show()
    currentApp.exec_()

if __name__ == '__main__':
    main()