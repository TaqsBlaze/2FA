import sys
import os
import sqlite3 as sql
import bcrypt


class SetUser:

    def __init__(self,details:dict):
        self.details = details
        self.db = sql.connect("resources/94KEzWo.sqlite3")
        self.cursor = self.db.cursor()


    def now(self):

        try:
            query = '''
            INSERT INTO user (password, email, recovery) VALUES (?,?,?)
            '''

            salt = bcrypt.gensalt(rounds = 5)
            hash = bcrypt.hashpw(self.details['password'].encode('utf-8'), salt = salt)
            details = (hash,self.details['email'],self.details['recovery'])

            self.cursor.execute(query,details)

            self.db.commit()
            self.db.close()

            return {"status":True, "message":"2FA was set successfully"}
        except Exception as error:
            print(error)
            return {"status":False, "message":"Failed to set your 2FA", "debug_msg":f"{error}", "debug":True} #Set debug to false to turn off debugging message in the application