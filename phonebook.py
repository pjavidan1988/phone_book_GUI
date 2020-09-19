from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PIL import Image
import os
import sys
import sqlite3

defaultImage = 'icons\PinClipart.com_short-person-clip-art_579234.png'
person_id = None
con = sqlite3.connect('phones.db')
cur = con.cursor()


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Phonebook')
        self.setWindowIcon(QIcon('icons\PngItem_5233379.png'))
        self.setGeometry(350, 80, 750, 600)
        self.UI()

        self.show()

    def UI(self):
        self.MainDesign()
        self.Layouts()
        self.getPhonebook()
        self.defaultDisplaye()

    def MainDesign(self):
        self.setStyleSheet("background-color:white;font-size:12pt;font-family:cursive")
        self.phonebookList = QListWidget()
        self.phonebookList.itemClicked.connect(self.singleClick)
        self.phonebookList.setStyleSheet(
            "padding: 2px;\n"
            "border-style: solid;\n"
            "border: 1px solid gray;\n"
            "border-radius: 8px;\n"
            "font-size: 18pt;\n"
        )
        self.btnNew = QPushButton('New')
        self.btnNew.clicked.connect(self.addPhonebook)
        self.btnNew.setStyleSheet(
            "   background: #3D94F6;\n"
            "   background-image: -webkit-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -moz-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -ms-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -o-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: linear-gradient(to bottom, #3D94F6, #1E62D0);\n"
            "   -webkit-border-radius: 20px;\n"
            "   -moz-border-radius: 20px;\n"
            "   border-radius: 12px;\n"
            "   color: #FFFFFF;\n"
            "   font-family: Open Sans;\n"
            "   font-size: 15px;\n"
            "   font-weight: 100;\n"
            "   padding: 5px;\n"
            "   box-shadow: 1px 1px 20px 0px #000000;\n"
            "   -webkit-box-shadow: 1px 1px 20px 0px #000000;\n"
            "   -moz-box-shadow: 1px 1px 20px 0px #000000;\n"
            "   text-shadow: 1px 1px 20px #000000;\n"
            "   border: solid #337FED 1px;\n"
            "   text-decoration: none;\n"
            "   display: inline-block;\n"
            "   cursor: pointer;\n"
            "   text-align: center;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   border: solid #337FED 1px;\n"
            "   background: #1E62D0;\n"
            "   background-image: -webkit-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -moz-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -ms-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -o-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: linear-gradient(to bottom, #1E62D0, #3D94F6);\n"
            "   -webkit-border-radius: 20px;\n"
            "   -moz-border-radius: 20px;\n"
            "   border-radius: 12px;\n"
            "   text-decoration: none;\n"
        )
        self.btnUpdate = QPushButton('Update')
        self.btnUpdate.clicked.connect(self.updatePerson)
        self.btnUpdate.setStyleSheet(
            "   background: #3D94F6;\n"
            "   background-image: -webkit-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -moz-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -ms-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -o-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: linear-gradient(to bottom, #3D94F6, #1E62D0);\n"
            "   -webkit-border-radius: 20px;\n"
            "   -moz-border-radius: 20px;\n"
            "   border-radius: 12px;\n"
            "   color: #FFFFFF;\n"
            "   font-family: Open Sans;\n"
            "   font-size: 15px;\n"
            "   font-weight: 100;\n"
            "   padding: 5px;\n"
            "   box-shadow: 1px 1px 20px 0px #000000;\n"
            "   -webkit-box-shadow: 1px 1px 20px 0px #000000;\n"
            "   -moz-box-shadow: 1px 1px 20px 0px #000000;\n"
            "   text-shadow: 1px 1px 20px #000000;\n"
            "   border: solid #337FED 1px;\n"
            "   text-decoration: none;\n"
            "   display: inline-block;\n"
            "   cursor: pointer;\n"
            "   text-align: center;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   border: solid #337FED 1px;\n"
            "   background: #1E62D0;\n"
            "   background-image: -webkit-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -moz-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -ms-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -o-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: linear-gradient(to bottom, #1E62D0, #3D94F6);\n"
            "   -webkit-border-radius: 20px;\n"
            "   -moz-border-radius: 20px;\n"
            "   border-radius: 12px;\n"
            "   text-decoration: none;\n"
        )

        self.btnDelete = QPushButton('Delete')
        self.btnDelete.clicked.connect(self.deletePerson)
        self.btnDelete.setStyleSheet(
            "   background: #3D94F6;\n"
            "   background-image: -webkit-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -moz-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -ms-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -o-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: linear-gradient(to bottom, #3D94F6, #1E62D0);\n"
            "   -webkit-border-radius: 20px;\n"
            "   -moz-border-radius: 20px;\n"
            "   border-radius: 12px;\n"
            "   color: #FFFFFF;\n"
            "   font-family: Open Sans;\n"
            "   font-size: 15px;\n"
            "   font-weight: 100;\n"
            "   padding: 5px;\n"
            "   box-shadow: 1px 1px 20px 0px #000000;\n"
            "   -webkit-box-shadow: 1px 1px 20px 0px #000000;\n"
            "   -moz-box-shadow: 1px 1px 20px 0px #000000;\n"
            "   text-shadow: 1px 1px 20px #000000;\n"
            "   border: solid #337FED 1px;\n"
            "   text-decoration: none;\n"
            "   display: inline-block;\n"
            "   cursor: pointer;\n"
            "   text-align: center;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   border: solid #337FED 1px;\n"
            "   background: #1E62D0;\n"
            "   background-image: -webkit-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -moz-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -ms-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -o-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: linear-gradient(to bottom, #1E62D0, #3D94F6);\n"
            "   -webkit-border-radius: 20px;\n"
            "   -moz-border-radius: 20px;\n"
            "   border-radius: 12px;\n"
            "   text-decoration: none;\n"
        )

    def Layouts(self):
        ########################Layouts##################################
        self.mainLayout = QHBoxLayout()
        self.leftLayout = QFormLayout()
        self.rightMainLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightBottomLayout = QHBoxLayout()
        ########################add child layout to main layout##############
        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)

        self.mainLayout.addLayout(self.leftLayout, 50)
        self.mainLayout.addLayout(self.rightMainLayout, 50)
        ###########################adding widget to layout####################
        self.rightTopLayout.addWidget(self.phonebookList)
        self.rightBottomLayout.addWidget(self.btnNew)
        self.rightBottomLayout.addWidget(self.btnUpdate)
        self.rightBottomLayout.addWidget(self.btnDelete)

        #######################setting main window layout######################
        self.setLayout(self.mainLayout)
        ##########################connect to add phonebook class################

    def addPhonebook(self):
        self.NewPhonebook = addPhonebook()
        self.close()
        ##############################get phonebook##############################

    def getPhonebook(self):
        query = 'SELECT id,name,surname FROM phones'
        phones = cur.execute(query).fetchall()
        for phonebook in phones:
            self.phonebookList.addItem(str(phonebook[0]) + " - " + phonebook[1] + " " + phonebook[2])

        ###########################default Display###############################
    def defaultDisplaye(self):
        img = QLabel()
        img.setPixmap(QPixmap('icons\PinClipart.com_short-person-clip-art_579234.png'))
        name = QLabel()
        surname = QLabel()
        phone = QLabel()
        email = QLabel()
        address = QLabel()
        self.leftLayout.setVerticalSpacing(12)
        self.leftLayout.addRow('', img)
        self.leftLayout.addRow('Name :', name)
        self.leftLayout.addRow('Surname :', surname)
        self.leftLayout.addRow('Phone :', phone)
        self.leftLayout.addRow('Email :', email)
        self.leftLayout.addRow('Address :', address)

        ###################################display first record####################
    def displayFirstRecord(self):
        query = 'SELECT * FROM phones ORDER BY ROWID ASC LIMIT 1'
        phones = cur.execute(query).fetchone()
        img = QLabel()
        img.setPixmap(QPixmap("images/" + phones[5]))
        name = QLabel(phones[1])
        surname = QLabel(phones[2])
        phone = QLabel(phones[3])
        email = QLabel(phones[4])
        address = QLabel(phones[6])
        self.leftLayout.setVerticalSpacing(12)
        self.leftLayout.addRow('', img)
        self.leftLayout.addRow('Name :', name)
        self.leftLayout.addRow('Surname :', surname)
        self.leftLayout.addRow('Phone :', phone)
        self.leftLayout.addRow('Email :', email)
        self.leftLayout.addRow('Address :', address)

        ######################################single clicked##########################
    def singleClick(self):
        for i in reversed(range(self.leftLayout.count())):  # clear person
            widget = self.leftLayout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        phone = self.phonebookList.currentItem().text()
        id = phone.split('-')[0]
        query = ('SELECT * FROM phones WHERE id=?')
        person = cur.execute(query, (id,)).fetchone()  # single item tuple
        img = QLabel()
        img.setPixmap(QPixmap("images/" + person[5]))
        name = QLabel()
        name.setText(person[1])
        surname = QLabel()
        surname.setText(person[2])
        phone = QLabel()
        phone.setText(person[3])
        email = QLabel()
        email.setText(person[4])
        address = QLabel()
        address.setText(person[6])
        self.leftLayout.setVerticalSpacing(12)
        self.leftLayout.addRow('', img)
        self.leftLayout.addRow('Name :', name)
        self.leftLayout.addRow('Surname :', surname)
        self.leftLayout.addRow('Phone :', phone)
        self.leftLayout.addRow('Email :', email)
        self.leftLayout.addRow('Address :', address)

        ###########################################Delete#################################
    def deletePerson(self):
        if self.phonebookList.selectedItems():
            person = self.phonebookList.currentItem().text()
            id = person.split('-')[0]
            mbox = QMessageBox.question(self, 'Warning', 'Are you sure to delete this person ?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if mbox == QMessageBox.Yes:
                try:
                    query = 'DELETE FROM phones WHERE id=?'
                    cur.execute(query, (id,))
                    con.commit()

                    QMessageBox.information(self, 'Info', 'person has been deleted')
                    self.close()
                    self.main = Main()

                except:
                    QMessageBox.critical(self, 'Warning', 'person has not been deleted')

        else:
            QMessageBox.critical(self, 'Warning', 'please select a person to delete')
        ########################################update######################################

    def updatePerson(self):
        global person_id
        if self.phonebookList.selectedItems():
            person = self.phonebookList.currentItem().text()
            person_id = person.split('-')[0]
            self.updateWindow = updatePhonebook()
            self.close()

        else:
            QMessageBox.critical(self, 'Warning', 'please select a person to update')

        #################################update class#######################################


class updatePhonebook(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Update Phonebook')
        self.setWindowIcon(QIcon('icons\icons8-add-80.png'))
        self.setGeometry(500, 80, 400, 600)
        self.UI()

        self.show()

    def UI(self):
        self.getPerson()
        self.MainDesign()
        self.addPhonebookLayouts()

    def closeEvent(self, event):
        self.main = Main()

    def getPerson(self):
        global person_id
        query = 'SELECT * FROM phones WHERE id=?'

        phone = cur.execute(query, (person_id,)).fetchone()

        self.name = phone[1]
        self.surname = phone[2]
        self.phone = phone[3]
        self.email = phone[4]
        self.image = phone[5]
        self.address = phone[6]

    def MainDesign(self):
        ###################################top widgets#####################################
        self.setStyleSheet("background-color:white;font-size:12pt;font-family:Times")
        self.addNewPhonebookLable = QLabel('UPDATE  PERSON')
        self.addNewPhonebookLable.setStyleSheet('font-size: 25pt; font-family: Impact, Charcoal, sans-serif')
        self.imgAdd = QLabel()
        self.imgAdd.setPixmap(QPixmap(f'images/{self.image}'))
        #####################################bottom widgets###############################
        self.nameLable = QLabel('Name : ')
        self.nameLineEdite = QLineEdit()
        self.nameLineEdite.setText(self.name)
        self.nameLineEdite.setStyleSheet(
            "padding: 2px;\n"
            "border-style: solid;\n"
            "border: 1px solid gray;\n"
            "border-radius: 8px;\n"
        )

        self.nameLable.setStyleSheet('font-size: 12pt; font-family: "Lucida Console", Courier, monospace')

        self.surnameLable = QLabel('Surname : ')
        self.surnameLineEdite = QLineEdit()
        self.surnameLineEdite.setText(self.surname)
        self.surnameLineEdite.setStyleSheet(
            "padding: 2px;\n"
            "border-style: solid;\n"
            "border: 1px solid gray;\n"
            "border-radius: 8px;\n"
        )
        self.surnameLable.setStyleSheet('font-size: 12pt; font-family: "Lucida Console", Courier, monospace')

        self.phoneLable = QLabel('Phone : ')
        self.phoneLineEdite = QLineEdit()
        self.phoneLineEdite.setText(self.phone)
        self.phoneLineEdite.setStyleSheet(
            "padding: 2px;\n"
            "border-style: solid;\n"
            "border: 1px solid gray;\n"
            "border-radius: 8px;\n"
        )
        self.phoneLable.setStyleSheet('font-size: 12pt; font-family: "Lucida Console", Courier, monospace')

        self.emailLable = QLabel('Email : ')
        self.emailLineEdite = QLineEdit()
        self.emailLineEdite.setText(self.email)
        self.emailLineEdite.setStyleSheet(
            "padding: 2px;\n"
            "border-style: solid;\n"
            "border: 1px solid gray;\n"
            "border-radius: 8px;\n"
        )

        self.emailLable.setStyleSheet('font-size: 12pt; font-family: "Lucida Console", Courier, monospace')

        self.imgLable = QLabel('Add image : ')

        self.btnImg = QPushButton('Browse')
        self.btnImg.clicked.connect(self.addImage)

        self.btnImg.setStyleSheet(
            "   background: #3D94F6;\n"
            "   background-image: -webkit-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -moz-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -ms-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -o-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: linear-gradient(to bottom, #3D94F6, #1E62D0);\n"
            "   -webkit-border-radius: 20px;\n"
            "   -moz-border-radius: 20px;\n"
            "   border-radius: 12px;\n"
            "   color: #FFFFFF;\n"
            "   font-family: Open Sans;\n"
            "   font-size: 15px;\n"
            "   font-weight: 100;\n"
            "   padding: 5px;\n"
            "   box-shadow: 1px 1px 20px 0px #000000;\n"
            "   -webkit-box-shadow: 1px 1px 20px 0px #000000;\n"
            "   -moz-box-shadow: 1px 1px 20px 0px #000000;\n"
            "   text-shadow: 1px 1px 20px #000000;\n"
            "   border: solid #337FED 1px;\n"
            "   text-decoration: none;\n"
            "   display: inline-block;\n"
            "   cursor: pointer;\n"
            "   text-align: center;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   border: solid #337FED 1px;\n"
            "   background: #1E62D0;\n"
            "   background-image: -webkit-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -moz-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -ms-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -o-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: linear-gradient(to bottom, #1E62D0, #3D94F6);\n"
            "   -webkit-border-radius: 20px;\n"
            "   -moz-border-radius: 20px;\n"
            "   border-radius: 12px;\n"
            "   text-decoration: none;\n"
        )
        self.imgLable.setStyleSheet('font-size: 12pt; font-family: "Lucida Console", Courier, monospace')

        self.addressLable = QLabel('Address : ')
        self.addressTextEdite = QTextEdit()
        self.addressTextEdite.setText(self.address)
        self.addressTextEdite.setStyleSheet(
            "padding: 2px;\n"
            "border-style: solid;\n"
            "border: 1px solid gray;\n"
            "border-radius: 8px;\n"
        )
        self.addressLable.setStyleSheet('font-size: 12pt; font-family: "Lucida Console", Courier, monospace')

        self.btnUpdate = QPushButton('Update')
        self.btnUpdate.clicked.connect(self.updatePhonebook)
        self.btnUpdate.setStyleSheet(
            "   background: #3D94F6;\n"
            "   background-image: -webkit-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -moz-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -ms-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -o-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: linear-gradient(to bottom, #3D94F6, #1E62D0);\n"
            "   -webkit-border-radius: 20px;\n"
            "   -moz-border-radius: 20px;\n"
            "   border-radius: 12px;\n"
            "   color: #FFFFFF;\n"
            "   font-family: Open Sans;\n"
            "   font-size: 15px;\n"
            "   font-weight: 100;\n"
            "   padding: 5px;\n"
            "   box-shadow: 1px 1px 20px 0px #000000;\n"
            "   -webkit-box-shadow: 1px 1px 20px 0px #000000;\n"
            "   -moz-box-shadow: 1px 1px 20px 0px #000000;\n"
            "   text-shadow: 1px 1px 20px #000000;\n"
            "   border: solid #337FED 1px;\n"
            "   text-decoration: none;\n"
            "   display: inline-block;\n"
            "   cursor: pointer;\n"
            "   text-align: center;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   border: solid #337FED 1px;\n"
            "   background: #1E62D0;\n"
            "   background-image: -webkit-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -moz-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -ms-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -o-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: linear-gradient(to bottom, #1E62D0, #3D94F6);\n"
            "   -webkit-border-radius: 20px;\n"
            "   -moz-border-radius: 20px;\n"
            "   border-radius: 12px;\n"
            "   text-decoration: none;\n"
        )

    def addPhonebookLayouts(self):
        ############################layouts######################
        self.mainLayout = QVBoxLayout()
        self.toLayout = QVBoxLayout()
        self.bottomlayout = QFormLayout()
        #############add child layouts to main layouts###########
        self.mainLayout.addLayout(self.toLayout)
        self.mainLayout.addLayout(self.bottomlayout)
        ###########################adding widget to toplayout####
        self.toLayout.addWidget(self.addNewPhonebookLable)
        self.toLayout.setAlignment(self.addNewPhonebookLable, Qt.AlignCenter)
        self.toLayout.addWidget(self.imgAdd)
        self.toLayout.setAlignment(self.imgAdd, Qt.AlignCenter)
        ###########################adding widget to bottomlayout##
        self.bottomlayout.addRow(self.nameLable, self.nameLineEdite)
        self.bottomlayout.addRow(self.surnameLable, self.surnameLineEdite)
        self.bottomlayout.addRow(self.phoneLable, self.phoneLineEdite)
        self.bottomlayout.addRow(self.emailLable, self.emailLineEdite)
        self.bottomlayout.addRow(self.imgLable, self.btnImg)
        self.bottomlayout.addRow(self.addressLable, self.addressTextEdite)
        self.bottomlayout.addRow('', self.btnUpdate)
        ################setting main window layout#################
        self.setLayout(self.mainLayout)

    def addImage(self):
        global defaultImage
        size = (200, 200)
        self.fileName, ok = fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '',
                                                                       'Image Files (*.jpg *.png)')

        if ok:
            defaultImage = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save(f'images/{defaultImage}')

        ######################################add Phonebook###########

    def updatePhonebook(self):
        global defaultImage
        global person_id
        name = self.nameLineEdite.text()
        surname = self.surnameLineEdite.text()
        phone = self.phoneLineEdite.text()
        email = self.emailLineEdite.text()
        img = defaultImage
        address = self.addressTextEdite.toPlainText()

        if name and surname and phone != '':
            try:
                query = 'UPDATE phones set  name=?, surname=?, phone=?,email=?,img=?,address=? WHERE id=?'
                cur.execute(query, (name, surname, phone, email, img, address, person_id))
                con.commit()
                QMessageBox.information(self, 'SUCCESS', 'person has been updated')
                self.close()
                self.main = Main()
            except:
                QMessageBox.critical(self, 'WARNING', 'person has not been updated')

        else:
            QMessageBox.warning(self, 'WARNING', 'Fields can not be empty')

        ##################################addPhonebook class##############


class addPhonebook(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Phonebook')
        self.setWindowIcon(QIcon('icons\icons8-add-80.png'))
        self.setGeometry(500, 80, 400, 600)
        self.UI()

        self.show()

    def UI(self):
        self.addMainDesign()
        self.addPhonebookLayouts()

    def closeEvent(self, event):
        self.main = Main()

    def addMainDesign(self):
        ###################################top widgets#######################
        self.setStyleSheet("background-color:white;font-size:12pt;font-family:Times")
        self.addNewPhonebookLable = QLabel('NEW  PERSON')
        self.addNewPhonebookLable.setStyleSheet('font-size: 25pt; font-family: Impact, Charcoal, sans-serif')
        self.imgAdd = QLabel()
        self.imgAdd.setPixmap(QPixmap('icons\PinClipart.com_short-person-clip-art_579234.png'))
        #####################################bottom widgets###############################
        self.nameLable = QLabel('Name : ')
        self.nameLineEdite = QLineEdit()
        self.nameLineEdite.setStyleSheet(
            "padding: 2px;\n"
            "border-style: solid;\n"
            "border: 1px solid gray;\n"
            "border-radius: 8px;\n"
        )
        self.nameLineEdite.setPlaceholderText('Enter name')
        self.nameLable.setStyleSheet('font-size: 12pt; font-family: "Lucida Console", Courier, monospace')

        self.surnameLable = QLabel('Surname : ')
        self.surnameLineEdite = QLineEdit()
        self.surnameLineEdite.setStyleSheet(
            "padding: 2px;\n"
            "border-style: solid;\n"
            "border: 1px solid gray;\n"
            "border-radius: 8px;\n"
        )
        self.surnameLineEdite.setPlaceholderText('Enter surname')
        self.surnameLable.setStyleSheet('font-size: 12pt; font-family: "Lucida Console", Courier, monospace')

        self.phoneLable = QLabel('Phone : ')
        self.phoneLineEdite = QLineEdit()
        self.phoneLineEdite.setStyleSheet(
            "padding: 2px;\n"
            "border-style: solid;\n"
            "border: 1px solid gray;\n"
            "border-radius: 8px;\n"
        )
        self.phoneLineEdite.setPlaceholderText('Enter phone number')
        self.phoneLable.setStyleSheet('font-size: 12pt; font-family: "Lucida Console", Courier, monospace')

        self.emailLable = QLabel('Email : ')
        self.emailLineEdite = QLineEdit()
        self.emailLineEdite.setStyleSheet(
            "padding: 2px;\n"
            "border-style: solid;\n"
            "border: 1px solid gray;\n"
            "border-radius: 8px;\n"
        )
        self.emailLineEdite.setPlaceholderText('Enter email')
        self.emailLable.setStyleSheet('font-size: 12pt; font-family: "Lucida Console", Courier, monospace')

        self.imgLable = QLabel('Add image : ')
        self.btnImg = QPushButton('Browse')
        self.btnImg.clicked.connect(self.addImage)
        self.btnImg.setStyleSheet(
            "   background: #3D94F6;\n"
            "   background-image: -webkit-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -moz-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -ms-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -o-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: linear-gradient(to bottom, #3D94F6, #1E62D0);\n"
            "   -webkit-border-radius: 20px;\n"
            "   -moz-border-radius: 20px;\n"
            "   border-radius: 12px;\n"
            "   color: #FFFFFF;\n"
            "   font-family: Open Sans;\n"
            "   font-size: 15px;\n"
            "   font-weight: 100;\n"
            "   padding: 5px;\n"
            "   box-shadow: 1px 1px 20px 0px #000000;\n"
            "   -webkit-box-shadow: 1px 1px 20px 0px #000000;\n"
            "   -moz-box-shadow: 1px 1px 20px 0px #000000;\n"
            "   text-shadow: 1px 1px 20px #000000;\n"
            "   border: solid #337FED 1px;\n"
            "   text-decoration: none;\n"
            "   display: inline-block;\n"
            "   cursor: pointer;\n"
            "   text-align: center;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   border: solid #337FED 1px;\n"
            "   background: #1E62D0;\n"
            "   background-image: -webkit-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -moz-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -ms-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -o-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: linear-gradient(to bottom, #1E62D0, #3D94F6);\n"
            "   -webkit-border-radius: 20px;\n"
            "   -moz-border-radius: 20px;\n"
            "   border-radius: 12px;\n"
            "   text-decoration: none;\n"
        )
        self.imgLable.setStyleSheet('font-size: 12pt; font-family: "Lucida Console", Courier, monospace')

        self.addressLable = QLabel('Address : ')
        self.addressTextEdite = QTextEdit()
        self.addressTextEdite.setStyleSheet(
            "padding: 2px;\n"
            "border-style: solid;\n"
            "border: 1px solid gray;\n"
            "border-radius: 8px;\n"
        )
        self.addressTextEdite.setPlaceholderText('Enter address')
        self.addressLable.setStyleSheet('font-size: 12pt; font-family: "Lucida Console", Courier, monospace')

        self.btnAdd = QPushButton('Add')
        self.btnAdd.clicked.connect(self.addPhonebook)
        self.btnAdd.setStyleSheet(
            "   background: #3D94F6;\n"
            "   background-image: -webkit-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -moz-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -ms-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: -o-linear-gradient(top, #3D94F6, #1E62D0);\n"
            "   background-image: linear-gradient(to bottom, #3D94F6, #1E62D0);\n"
            "   -webkit-border-radius: 20px;\n"
            "   -moz-border-radius: 20px;\n"
            "   border-radius: 12px;\n"
            "   color: #FFFFFF;\n"
            "   font-family: Open Sans;\n"
            "   font-size: 15px;\n"
            "   font-weight: 100;\n"
            "   padding: 5px;\n"
            "   box-shadow: 1px 1px 20px 0px #000000;\n"
            "   -webkit-box-shadow: 1px 1px 20px 0px #000000;\n"
            "   -moz-box-shadow: 1px 1px 20px 0px #000000;\n"
            "   text-shadow: 1px 1px 20px #000000;\n"
            "   border: solid #337FED 1px;\n"
            "   text-decoration: none;\n"
            "   display: inline-block;\n"
            "   cursor: pointer;\n"
            "   text-align: center;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "   border: solid #337FED 1px;\n"
            "   background: #1E62D0;\n"
            "   background-image: -webkit-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -moz-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -ms-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: -o-linear-gradient(top, #1E62D0, #3D94F6);\n"
            "   background-image: linear-gradient(to bottom, #1E62D0, #3D94F6);\n"
            "   -webkit-border-radius: 20px;\n"
            "   -moz-border-radius: 20px;\n"
            "   border-radius: 12px;\n"
            "   text-decoration: none;\n"
        )

    def addPhonebookLayouts(self):
        ############################layouts######################
        self.mainLayout = QVBoxLayout()
        self.toLayout = QVBoxLayout()
        self.bottomlayout = QFormLayout()
        #############add child layouts to main layouts###########
        self.mainLayout.addLayout(self.toLayout)
        self.mainLayout.addLayout(self.bottomlayout)
        ###########################adding widget to toplayout####
        self.toLayout.addWidget(self.addNewPhonebookLable)
        self.toLayout.setAlignment(self.addNewPhonebookLable, Qt.AlignCenter)
        self.toLayout.addWidget(self.imgAdd)
        self.toLayout.setAlignment(self.imgAdd, Qt.AlignCenter)
        ###############adding widget to bottomlayout#############
        self.bottomlayout.addRow(self.nameLable, self.nameLineEdite)
        self.bottomlayout.addRow(self.surnameLable, self.surnameLineEdite)
        self.bottomlayout.addRow(self.phoneLable, self.phoneLineEdite)
        self.bottomlayout.addRow(self.emailLable, self.emailLineEdite)
        self.bottomlayout.addRow(self.imgLable, self.btnImg)
        self.bottomlayout.addRow(self.addressLable, self.addressTextEdite)
        self.bottomlayout.addRow('', self.btnAdd)
        ################setting main window layout###############
        self.setLayout(self.mainLayout)
        ####################Browse Image#########################

    def addImage(self):
        global defaultImage
        size = (128, 128)
        self.fileName, ok = fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '',
                                                                       'Image Files (*.jpg *.png)')

        if ok:
            defaultImage = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save(f'images/{defaultImage}')

    ######################################add Phonebook############

    def addPhonebook(self):
        global defaultImage
        name = self.nameLineEdite.text()
        surname = self.surnameLineEdite.text()
        phone = self.phoneLineEdite.text()
        email = self.emailLineEdite.text()
        img = defaultImage
        address = self.addressTextEdite.toPlainText()

        if name and surname and phone != '':
            try:
                query = 'INSERT INTO phones (name,surname,phone,email,img,address) VALUES(?,?,?,?,?,?)'
                cur.execute(query, (name, surname, phone, email, img, address))
                con.commit()
                QMessageBox.information(self, 'SUCCESS', 'new person has been added')
                self.close()
                self.main = Main()
            except:
                QMessageBox.critical(self, 'WARNING', 'new person has not been added')
                QMessageBox.setWindowIcon(QIcon('icons\icons8-brake-warning-80.png'))

        else:
            QMessageBox.warning(self, 'WARNING', 'Fields can not be empty')


def main():
    APP = QApplication(sys.argv)
    window = Main()
    sys.exit(APP.exec_())


if __name__ == '__main__':
    main()
