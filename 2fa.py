from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame,QLabel, QPushButton, QLineEdit
from PyQt5 import uic,QtWidgets, QtCore
from resources import resources_rc
from set import SetUser
from resourcecheck import ResourcesCheck
from auth import Authentication
import sys

#Checking some resources
check_1 = ResourcesCheck.check_db_resource()
check_2 = ResourcesCheck.generate_db()

if check_1['status']:
    print(check_1['message'])
    pass
else:
    if check_2['status']:

        print(check_2['message']) #for debuging
        class MyApp(QtWidgets.QMainWindow):
            def __init__(self):
                super().__init__()
                # Load the UI file
                uic.loadUi('config.ui', self)
                self.password = self.findChild(QLineEdit,"password")
                self.confirm = self.findChild(QLineEdit, "confirm_password")
                self.email = self.findChild(QLineEdit, "email")
                self.message = self.findChild(QLabel,"error_message")
                self.savebutton = self.findChild(QPushButton,"save_button")
                self.confirm.returnPressed.connect(self.set_details)
                self.message.hide()
                self.savebutton.clicked.connect(self.set_details)

                #transparent and frameless window
                self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
                self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

            def set_details(self):

                if self.password.text() == self.confirm.text():
                
                    try:
                        result = SetUser({'password':self.password.text(),'email':self.email.text(),'recovery':'None'}).now()
                        if result['status']:
                            self.message.setText(f"{result['message']}")
                            QtWidgets.QApplication.quit()
                            pass
                        else:
                            self.message.setText(f"{result['message']} {result['debug_msg']}")
                            self.message.show()
                    except Exception as error:
                        pass

                else:

                    self.confirm.setStyleSheet("""
                        QLineEdit {
                            border: 2px solid;
                            border-color: #B70000FF;
                            padding: 5px;
                            background-color:white;
                        }
                    """)

                    self.message.setStyleSheet("""
                        QLabel {
                            background-color:white;
                            color:red;
                        }
                    """)
                    self.message.setText("Passwords do not match!")
                    self.message.show()


            def confirm_check(self):


                pass

        app = QtWidgets.QApplication(sys.argv)
        window = MyApp()
        window.show()
        sys.exit(app.exec_())
        

    else:
        print(check_2['message'])
        pass



class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the UI file
        uic.loadUi('main.ui', self)
        self.password = self.findChild(QLineEdit,"_2fa_input")
        self.password.returnPressed.connect(self.authenticat)
        self.message = self.findChild(QLabel,"message_label")
        self.message.hide()

        #transparent and frameless window
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def authenticat(self):

        result = Authentication(self.password.text()).authenticat()

        if result['status']:
            QtWidgets.QApplication.quit()
        else:
            self.message.setText(f"{result['message']}")
            self.message.show()
            pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())