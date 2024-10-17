import os
import sys
import sqlite3 as sql
import bcrypt




class Authentication:

    def __init__(self, password):
        self.password = password
        self.db = sql.connect("resources/94KEzWo.db")
        self.cursor = self.db.cursor()

        
    def authenticat(self):
        password = self.password

        print("password:",password,"type:", type(password))
        query = """SELECT password FROM user WHERE id = ?"""
        data = self.cursor.execute(query,(1,))
        result = data.fetchone()

        if bcrypt.checkpw(self.password.encode('utf-8'), result[0]):
            
            return {'status':True, 'message':"Success"}
    
        else:
            # self.message.setText("Password can not be empty")
            # self.message.setStyleSheet("QLabel { background-color: red; color: white;border-radius:5px; width:5cm; }")
            # self.message.show()
            #QtWidgets.QApplication.quit()
            return {'status':False, 'message': "Failed to verify"}
        
        if password != 'password':
            self.message.setText("Incorrect password")
            self.message.setStyleSheet("QLabel { background-color: red; color: white;border-radius:5px; width:5cm; }")
            self.message.show()
            #QtWidgets.QApplication.quit()