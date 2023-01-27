from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QDialog
import sys
from passwordMenager import Ui_MainWindow
from saveasDialog import Ui_saveDialog
from imputDecKeyDialog import Ui_impDecKeyDialog
import random

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        # self.setWindowTitle('Password Help')
        # wyswitla startowa strone to jest wysztko co potrzebne zeby dodac .ui
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        # mainbtns
        self.ui.toGeneratorBtn.clicked.connect(self.togenerator)
        self.ui.toSavedPassBtn.clicked.connect(self.tosavedpasswords)
        # v Generator Section! v
        # password generator btn!
        self.ui.passwordGenerateBtn.clicked.connect(self.generatepassword)
        # slider connect
        self.ui.passwordlenghtSlider.valueChanged.connect(self.slider_moved) #length not lenght -> need to fix that later
        # updates the slider lenght
        self.ui.capitalCheckBox.stateChanged.connect(self.checkboxes_toggled)
        self.ui.lowercaseCheckBox.stateChanged.connect(self.checkboxes_toggled)
        self.ui.separatorsCheckBox.stateChanged.connect(self.checkboxes_toggled)
        self.ui.digtsCheckBox.stateChanged.connect(self.checkboxes_toggled)
        self.ui.specialcharactersCheckBox.stateChanged.connect(self.checkboxes_toggled)
        # copybtn and savefpasswordbtn connect
        self.ui.copyPassBtn.clicked.connect(self.copyToClipboard)
        self.ui.savePassBtn.clicked.connect(self.lunchSaveDialog)
        # v Menager section! v
        # Tableinit
        self.loadPasswords()
        # secret key imput btn connect
        self.ui.imputDecryptionKeyButton.clicked.connect(self.lunchImputDecryptionKeyDialog)
        secretkey = ''
        



    # page switch functions
    def togenerator(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)    
    def tosavedpasswords(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
    # v Generator section! v
    # slider functions
    def checkboxesSliderLenght(self):
        lettersL = 24
        digitsL = 10
        specialsL = 22
        sepL = 1
        defL = 0
        if self.ui.capitalCheckBox.isChecked():
            defL += lettersL
        if self.ui.lowercaseCheckBox.isChecked():
            defL += lettersL
        if self.ui.separatorsCheckBox.isChecked():
            defL += sepL
        if self.ui.digtsCheckBox.isChecked():
            defL += digitsL
        if self.ui.specialcharactersCheckBox.isChecked():
            defL += specialsL
        return(defL)

    def checkboxes_toggled(self):
        lenght = self.checkboxesSliderLenght()
        self.ui.passwordlenghtSlider.setRange(0, lenght)

    def slider_moved(self):
        new_value = str(self.ui.passwordlenghtSlider.value())
        self.ui.lenghtCounterLabel.setText(new_value)
        
    # checkboxes functions
    def chekboxesGeneratorRundown(self):
        usingthose = ''
        capitalletters = 'ABCDEFGHIJKLMNOPRSTUWXYZ'
        lowercaseletters = capitalletters.lower()
        separatorsregular = ' '
        separatofloor = '_'
        digitsused = '1234567890'
        specials = '!@#$%^&*()\{\}[]/.,:;\\\'\"'
        if self.ui.capitalCheckBox.isChecked():
            usingthose += capitalletters
        if self.ui.lowercaseCheckBox.isChecked():
            usingthose += lowercaseletters
        if self.ui.separatorsCheckBox.isChecked():
            if self.ui.floorCheckBox.isChecked():
                usingthose += separatofloor
            else:
                usingthose += separatorsregular
        if self.ui.digtsCheckBox.isChecked():
            usingthose += digitsused
        if self.ui.specialcharactersCheckBox.isChecked():
            usingthose += specials
        return(usingthose)

    # Generator logic
    def generatepassword(self):
        length = self.ui.passwordlenghtSlider.value()
        characters = self.chekboxesGeneratorRundown()
        password = ''.join(random.sample(characters, length)) #sample will only use each symbol once
        self.ui.GeneratedPasswordEdit.setText(password)

    # copy to clipboard function
    def copyToClipboard(self):
        letxt = self.ui.GeneratedPasswordEdit.toPlainText() # Textedit and lineedit are different and Textedit doest not have .text() and you need too use toPlainText() method
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard) #clears existing clipboard 
        cb.setText(letxt, mode=cb.Clipboard) #assigns textedit text to clipboard 

    # save file dialog
    def lunchSaveDialog(self):
        saveDialog = QDialog()
        ui = Ui_saveDialog()
        ui.setupUi(saveDialog)
        saveDialog.show()
        # saveDialog.exec_()
        rsp = saveDialog.exec_()
        if rsp == QDialog.Accepted: #if user clicks ok. USE: Accepted() not accepted()!
            # sitetem = str(self.ui.SiteLineEdit.text())
            # usernametem = str(self.ui.usernameLineEdit.text())
            # decryptionkeytem = str(self.ui.decryptionkeyLineEdit.text())
            self.ui.GeneratedPasswordEdit.setText("password saved!")
        else:
            self.ui.GeneratedPasswordEdit.setText("password NOT saved!")



    # saving the password to txt
    # Test function
    def saveThePassword(self):
        with open("test.txt", "w") as f:
            mytext = self.ui.GeneratedPasswordEdit.toPlainText()
            f.write(mytext)

    # v Menager section v

    def lunchImputDecryptionKeyDialog(self):
        impDecKeyDialog = QDialog()
        uik = Ui_impDecKeyDialog()
        uik.setupUi(impDecKeyDialog)
        impDecKeyDialog.show()
        # impDecKeyDialog.exec_() #without exec_() the dialog will clsoe immediately
        rsp = impDecKeyDialog.exec_()
        if rsp == QDialog.Accepted: #if user clicks ok. USE: Accepted() not accepted()!
            # secretkey = self.ui.imputDecryptionkeyLineEdit.text()
            self.ui.GeneratedPasswordEdit.setText(self.uik.imputDecryptionkeyLineEdit.text())

        

    def loadPasswords(self):
        # data to put into the table
        passwords = [
            {"site": "facebook", "username": "ares", "password": "1234567890"},
            {"site": "youtube", "username": "ares99m", "password": "1234567890bbb"},
            {"site": "google", "username": "arekmucha99@gmail.com", "password": "1234567890asd"},
        ]
        # naming the headers and setting the columns
        self.ui.tableWidget.setRowCount(len(passwords))
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(("site","Username/email", "Password"))
        # stretching the table
        header = self.ui.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        # inserting the data
        row_index = 0
        for passw in passwords:
            self.ui.tableWidget.setItem(row_index, 0, QTableWidgetItem(str(passw["site"])))
            self.ui.tableWidget.setItem(row_index, 1, QTableWidgetItem(str(passw["username"])))
            self.ui.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(passw["password"])))
            row_index += 1


    # v Main program section v
    # kinda important, mainwindow wont display without this function!
    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())