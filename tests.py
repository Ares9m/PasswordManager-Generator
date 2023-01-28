# with open("passwords.txt","r") as f:
#     lines = f.readlines()
#     print(lines)

# import json
  
# # reading the data from the file
# with open("passwords.txt","r") as f:
#     data = f.read()
  
# print("Data type before reconstruction : ", type(data))
      
# # reconstructing the data as a dictionary
# js = json.loads(data)
  
# print("Data type after reconstruction : ", type(js))
# print(js)

#     def loadPasswords(self):
#         # data to put into the table
#         # passwords = []
#             # {"site": "facebook", "username": "ares", "password": "1234567890"},
#             # {"site": "youtube", "username": "ares99m", "password": "1234567890bbb"},
#             # {"site": "google", "username": "arekmucha99@gmail.com", "password": "1234567890asd"},
#         # ]
        
#         with open("passwords.txt", "r") as f:
#             passwords = f.readlines()

        
#         # naming the headers and setting the columns
#         self.ui.tableWidget.setRowCount(len(passwords))
#         self.ui.tableWidget.setColumnCount(3)
#         self.ui.tableWidget.setHorizontalHeaderLabels(("site","Username/email", "Password"))
#         # stretching the table
#         header = self.ui.tableWidget.horizontalHeader()       
#         header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
#         header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
#         header.setSectionResizeMode(2, QHeaderView.Stretch)
#         # inserting the data
#         row_index = 0
#         for passw in passwords:
#             self.ui.tableWidget.setItem(row_index, 0, QTableWidgetItem(str(passw["site"])))
#             self.ui.tableWidget.setItem(row_index, 1, QTableWidgetItem(str(passw["username"])))
#             self.ui.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(passw["password"])))
#             row_index += 1


#     def lunchSaveDialog(self):
#         cond = self.ui.GeneratedPasswordEdit.toPlainText()
#         if cond != "":
#             saveDialog = QDialog()
#             ui = Ui_saveDialog()
#             ui.setupUi(saveDialog)
#             saveDialog.show()
#             # saveDialog.exec_()
#             rsp = saveDialog.exec_()
#             if rsp == QDialog.Accepted: #if user clicks ok btn | USE: "Accepted" not "accepted" capital A
#                 sitet = str(ui.SiteLineEdit.text())
#                 usernamet = str(ui.usernameLineEdit.text())
#                 decryptionkeyt = str(ui.decryptionkeyLineEdit.text())
#                 passwd = self.ui.GeneratedPasswordEdit.toPlainText()
#                 with open("passwords.txt", "a") as f:     # might need to transform this section into a seprate fuction in the future
#                     f.write("{\"site\": \""+ sitet +"\", \"username\": \""+ usernamet +"\", \"password\": \""+passwd+ "\"}," +"\n")
# sitet = "123"
# usernamet = "ggg"
# passwd = "hh111"

# with open("passwords.txt", "a") as f:     # might need to transform this section into a seprate fuction in the future

#     f.write(sitet+ "|" +usernamet+ "|" +passwd+ "\n")

# with open("passwords.txt", "r") as grilled_cheese:
# 	lines = grilled_cheese.readlines()
# 	print(lines)

# quantities = []
# ingredients = []
# passwod = []

# for l in lines:
#     as_list = l.split("|",)
#     quantities.append(as_list[0])
#     ingredients.append(as_list[1])
#     passwod.append(as_list[2])

# print(quantities)
# print(ingredients)
# print(passwod)

from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# simplekey = get_random_bytes(32) # this generates static slat to encript data
# print(simplekey)
salt = b'\xf9z\xab\xe8-4}\xd6\x1b\xb5\xc4\xfc\xd4kT\xc8\xce\xc8R\xb0q&\xc4YqpO\x1f=\xb2-\xce'

password = "mypassword"

key = PBKDF2(password, salt, dkLen=32)

message = b"yeya"

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

print(ciphered_data)

with open("encrypted.bin", "wb") as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

with open("encrypted.bin", "rb") as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)


    # # save file dialog, saving the password to .txt + encrypting it
    # def lunchSaveDialog(self):
    #     cond = self.ui.GeneratedPasswordEdit.toPlainText()
    #     if cond != "":
    #         saveDialog = QDialog()
    #         ui = Ui_saveDialog()
    #         ui.setupUi(saveDialog)
    #         saveDialog.show()
    #         # saveDialog.exec_()
    #         rsp = saveDialog.exec_()
    #         if rsp == QDialog.Accepted: #if user clicks ok btn | USE: "Accepted" not "accepted" capital A
    #             sitet = str(ui.SiteLineEdit.text())
    #             usernamet = str(ui.usernameLineEdit.text())
    #             decryptionkeyt = str(ui.decryptionkeyLineEdit.text())
    #             passwd = self.ui.GeneratedPasswordEdit.toPlainText()
    #             with open("passwords.txt", "a") as f:     # might need to transform this section into a seprate fuction in the future
    #                 f.write(sitet+ "|" +usernamet+ "|" +passwd+"\n")
    #             self.loadPasswords() #updates the table

    # def loadPasswords(self):
    #     # data to put into the table        
    #     with open("passwords.txt", "r") as f:
    #         passwords = f.readlines()
    #     # naming the headers and setting the columns
    #     self.ui.tableWidget.setRowCount(len(passwords))
    #     self.ui.tableWidget.setColumnCount(3)
    #     self.ui.tableWidget.setHorizontalHeaderLabels(("site","Username/email", "Password"))
    #     # stretching the table
    #     header = self.ui.tableWidget.horizontalHeader()       
    #     header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
    #     header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
    #     header.setSectionResizeMode(2, QHeaderView.Stretch)
    #     # inserting the data
    #     row_index = 0
    #     for passw in passwords:
    #         as_list = passw.split("|")
    #         self.ui.tableWidget.setItem(row_index, 0, QTableWidgetItem(str(as_list[0])))
    #         self.ui.tableWidget.setItem(row_index, 1, QTableWidgetItem(str(as_list[1])))
    #         self.ui.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(as_list[2].strip()))) #strip gets rid of \n at the end
    #         row_index += 1

    # Test functions section

    # def saveThePassword(self,site, user, key):
    #     # with open("test.txt", "w") as f: #its better to use it like this because it will close the file if done like f = open("test.txt", "w") another function file.close() is needed after otherwise it will still be using it
    #     #     # modes "r" = read the file "w" overwrite the file -> if already exists it will clear and save the contents then "a" append mode if there is no file it will create it like w but it will not clear the conttes just add new content at the end
    #     #     mytext = self.ui.GeneratedPasswordEdit.toPlainText()
    #     #     f.write(mytext)
    #     with open("passwords.txt", "a"):
    #         passwd = self.ui.GeneratedPasswordEdit.toPlainText()
    #         f.write(site + "|" + user +"|"+passwd+"|"+key+ "\n")