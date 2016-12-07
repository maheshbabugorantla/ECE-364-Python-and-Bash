import sys
import re

from PySide.QtGui import *
from BasicUI import *


class Consumer(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.clearButton.clicked.connect(lambda: self.clearFields())

        # Detecting Text Entry into all the Text Fields
        self.firstNameLineEdit.textChanged.connect(lambda: self.activateSave())
        self.lastNameLineEdit.textChanged.connect(lambda: self.activateSave())
        self.addressLineEdit.textChanged.connect(lambda: self.activateSave())
        self.cityLineEdit.textChanged.connect(lambda: self.activateSave())
        self.stateLineEdit.textChanged.connect(lambda: self.activateSave())
        self.zipLineEdit.textChanged.connect(lambda: self.activateSave())
        self.emailLineEdit.textChanged.connect(lambda: self.activateSave())

        self.saveToTargetButton.clicked.connect(lambda: self.saveData())
        self.loadButton.clicked.connect(lambda: self.loadData())

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** This method is required for unit tests! ***
        """

        with open(filePath,"r") as fp:

            fileData = fp.read()

            self.firstNameLineEdit.setText(re.findall(r"<FirstName>(.*)<\/FirstName>",fileData)[0])
            self.lastNameLineEdit.setText(re.findall(r"<LastName>(.*)<\/LastName>",fileData)[0])
            self.addressLineEdit.setText(re.findall(r"<Address>(.*)<\/Address>",fileData)[0])
            self.cityLineEdit.setText(re.findall(r"<City>(.*)<\/City>",fileData)[0])
            self.stateLineEdit.setText(re.findall(r"<State>(.*)<\/State>",fileData)[0])
            self.zipLineEdit.setText(re.findall(r"<ZIP>(.*)<\/ZIP>",fileData)[0])
            self.emailLineEdit.setText(re.findall(r"<Email>(.*)<\/Email>",fileData)[0])

    def activateSave(self):
        self.saveToTargetButton.setEnabled(True)
        self.loadButton.setEnabled(False)
        self.errorInfoLabel.setText("")

    def saveData(self):

        if len(self.firstNameLineEdit.text()) == 0:
            self.errorInfoLabel.setText("Error: Enter FirstName")
            return

        elif len(self.lastNameLineEdit.text()) == 0:
            self.errorInfoLabel.setText("Error: Enter LastName")
            return

        elif len(self.addressLineEdit.text()) == 0:
            self.errorInfoLabel.setText("Error: Enter Address")
            return

        elif len(self.cityLineEdit.text()) == 0:
            self.errorInfoLabel.setText("Error: Enter City")
            return

        elif len(self.stateLineEdit.text()) == 0:
            self.errorInfoLabel.setText("Error: Enter State")
            return

        elif len(self.zipLineEdit.text()) == 0:
            self.errorInfoLabel.setText("Error: Enter ZipCode")
            return

        elif len(self.emailLineEdit.text()) == 0:
            self.errorInfoLabel.setText("Error: Enter Email")
            return

        else:
            status = self.validateInput()

            if not status:
                self.saveDataToFile()

    def saveDataToFile(self):

        with open("target.xml","w") as fp:
            fp.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<user>")
            fp.write("\n\t<FirstName>{0}</FirstName>".format(self.firstNameLineEdit.text()))
            fp.write("\n\t<LastName>{0}</LastName>".format(self.lastNameLineEdit.text()))
            fp.write("\n\t<Address>{0}</Address>".format(self.addressLineEdit.text()))
            fp.write("\n\t<City>{0}</City>".format(self.cityLineEdit.text()))
            fp.write("\n\t<State>{0}</State>".format(self.stateLineEdit.text()))
            fp.write("\n\t<ZIP>{0}</ZIP>".format(self.zipLineEdit.text()))
            fp.write("\n\t<Email>{0}</Email>".format(self.emailLineEdit.text()))
            fp.write("\n</user>")
            fp.write("\n")

    def validateInput(self):

        if self.stateLineEdit.text() not in self.states:
            self.errorInfoLabel.setText("Error: Invalid State Entry")
            return 1

        elif len(self.zipLineEdit.text()) != 5:
            self.errorInfoLabel.setText("Error: Invalid ZipCode")
            return True

        elif len(self.zipLineEdit.text()) == 5:

            digits = {'0','1','2','3','4','5','6','7','8','9'}
            for val in self.zipLineEdit.text():
                if val not in digits:
                  self.errorInfoLabel.setText("Error: Invalid ZipCode")
                  return True

        if len(re.findall(r"\w+\@\w+\.\w+",self.emailLineEdit.text())) != 1:
            self.errorInfoLabel.setText("Error: Invalid Email")
            return True

        return False

    def clearFields(self):

        # Clearing all the fields
        self.firstNameLineEdit.setText("")
        self.lastNameLineEdit.setText("")
        self.addressLineEdit.setText("")
        self.cityLineEdit.setText("")
        self.stateLineEdit.setText("")
        self.zipLineEdit.setText("")
        self.emailLineEdit.setText("")
        self.errorInfoLabel.setText("")

        self.saveToTargetButton.setEnabled(False)
        self.loadButton.setEnabled(True)

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if __name__ == "__main__":

    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
