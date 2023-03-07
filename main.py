from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QDialog
import sys
from passwordMenager import Ui_MainWindow
from saveasDialog import Ui_saveDialog
from imputDecKeyDialog import Ui_impDecKeyDialog
import random
# from cryptography import fernet

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        # ui setup and connections
        # self.setWindowTitle("apptitle")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        # mainbtns
        self.ui.toGeneratorBtn.clicked.connect(self.togenerator)
        self.ui.toSavedPassBtn.clicked.connect(self.tosavedpasswords)
        # === Generator Section ===
        #sets optional floor checkbox to invisble
        self.ui.floorCheckBox.setVisible(False) 
        # password generator btn
        self.ui.passwordGenerateBtn.clicked.connect(self.generatepassword)
        # slider connect
        self.ui.passwordlenghtSlider.valueChanged.connect(self.slider_moved) 
        #length not lenght, need to fix that later
        # updates the slider length
        self.ui.capitalCheckBox.stateChanged.connect(self.checkboxes_toggled)
        self.ui.lowercaseCheckBox.stateChanged.connect(self.checkboxes_toggled)
        self.ui.separatorsCheckBox.stateChanged.connect(self.checkboxes_toggled)
        self.ui.separatorsCheckBox.stateChanged.connect(self.separators_toggled)
        self.ui.digtsCheckBox.stateChanged.connect(self.checkboxes_toggled)
        self.ui.specialcharactersCheckBox.stateChanged.connect(self.checkboxes_toggled)
        # copybtn and savefpasswordbtn connect
        self.ui.copyPassBtn.clicked.connect(self.copyToClipboard)
        self.ui.savePassBtn.clicked.connect(self.lunchSaveDialog)
        # === Menager section ===
        # Tableinit
        self.loadPasswords()
        # secret key imput btn connect
        self.ui.imputDecryptionKeyButton.clicked.connect(self.lunchImputDecryptionKeyDialog)
        
    # page switch functions
    def togenerator(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)    
    def tosavedpasswords(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
    # === Generator section ===
    # slider functions
    def checkboxesSliderLength(self):
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
    # updates slider length if a checkbox is toggled
    def checkboxes_toggled(self):
        length = self.checkboxesSliderLength()
        self.ui.passwordlenghtSlider.setRange(0, length)
    # shows the use "_" if sepcheckbox is toggled
    def separators_toggled(self):
        if self.ui.separatorsCheckBox.isChecked():
            self.ui.floorCheckBox.setVisible(True)
        else:
            self.ui.floorCheckBox.setVisible(False)

    # updates password length is slider is moved
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
        password = ''.join(random.sample(characters, length)) 
        #sample will only use each symbol once
        self.ui.GeneratedPasswordEdit.setText(password)

    # copy to clipboard function
    def copyToClipboard(self):
        letxt = self.ui.GeneratedPasswordEdit.toPlainText() 
        # Textedit and lineedit are different and Textedit doest not use .text()
        # it uses toPlainText() method instead
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard) 
        #clears existing clipboard 
        cb.setText(letxt, mode=cb.Clipboard) 
        #assigns textedit text to clipboard 

    # save file dialog, saving the password to .txt
    def lunchSaveDialog(self):
        cond = self.ui.GeneratedPasswordEdit.toPlainText()
        if cond != "":
            saveDialog = QDialog()
            ui = Ui_saveDialog()
            ui.setupUi(saveDialog)
            saveDialog.show()
            # saveDialog.exec_()
            rsp = saveDialog.exec_()
            if rsp == QDialog.Accepted: 
                #if user clicks ok. USE: Accepted() not: accepted()
                sitet = str(ui.SiteLineEdit.text())
                usernamet = str(ui.usernameLineEdit.text())
                decryptionkeyt = str(ui.decryptionkeyLineEdit.text())
                passwd = self.ui.GeneratedPasswordEdit.toPlainText()
                # transform this section into a fuction in the future
                with open("passwords.txt", "a") as f:     
                    f.write(sitet+ "|" +usernamet+ "|" +passwd+"\n")
                self.loadPasswords() 
                #updates the table


    # === Menager section ===
    def lunchImputDecryptionKeyDialog(self):
        impDecKeyDialog = QDialog()
        ui = Ui_impDecKeyDialog()
        ui.setupUi(impDecKeyDialog)
        impDecKeyDialog.show()
        # impDecKeyDialog.exec_() #without exec_() the dialog will clsoe immediately
        rsp = impDecKeyDialog.exec_()
        if rsp == QDialog.Accepted: 
            #if user clicks ok. USE: Accepted() not: accepted()
            # secretkey = self.ui.imputDecryptionkeyLineEdit.text()
            secretkey1 = str(ui.imputDecryptionkeyLineEdit.text()) 
            #"()" is needed after .text() to work 
            # do not use self.ui when calling Qdialog winodow ui elements

    def loadPasswords(self):
        # data to put into the table        
        with open("passwords.txt", "r") as f:
            passwords = f.readlines()
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
            as_list = passw.split("|")
            self.ui.tableWidget.setItem(row_index, 0, QTableWidgetItem(str(as_list[0])))
            self.ui.tableWidget.setItem(row_index, 1, QTableWidgetItem(str(as_list[1])))
            self.ui.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(as_list[2].strip()))) 
            #strip gets rid of \n at the end
            row_index += 1


    # === Main program section ===
    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

"""
    === notes ===

    def saveThePassword(self,site, user, key):
        # with open("test.txt", "w") as f: #its better to use it like this because it will close the file if done like f = open("test.txt", "w") another function file.close() is needed after otherwise it will still be using it
        #     # modes "r" = read the file "w" overwrite the file -> if already exists it will clear and save the contents then "a" append mode if there is no file it will create it like w but it will not clear the conttes just add new content at the end
        #     mytext = self.ui.GeneratedPasswordEdit.toPlainText()
        #     f.write(mytext)
        with open("passwords.txt", "a"):
            passwd = self.ui.GeneratedPasswordEdit.toPlainText()
            f.write(site + "|" + user +"|"+passwd+"|"+key+ "\n")
"""