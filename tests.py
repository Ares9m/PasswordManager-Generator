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

with open("passwords.txt", "r") as grilled_cheese:
	lines = grilled_cheese.readlines()
	print(lines)

quantities = []
ingredients = []
passwod = []

for l in lines:
    as_list = l.split("|",)
    quantities.append(as_list[0])
    ingredients.append(as_list[1])
    passwod.append(as_list[2])

print(quantities)
print(ingredients)
print(passwod)
