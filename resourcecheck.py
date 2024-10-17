import os
import sys
import sqlite3 as sql


class ResourcesCheck:


    def check_db_resource():
        """
        Checking if database file exists in application files
        """
        if os.path.isfile("resources/94KEzWo.db"):

            return {'status':True,"message":"Databse exists"}
        
        else:
            #Resource not found

            return {'status':False,'message':"Database file was not found and will be auto generated"}
        
    def check_resource_file():
        """
        Checking if other resource files such as application icons exists
        as part of application filers
        """
        if os.path.isfile("resources/lock-computer.png")\
            and os.path.isfile("resources/shield.png"):
            
            return {"starus":True,"message":"All resources available"}
        
        else:

            return {"status":False, "message":"Some missing resources"}



    def generate_db():
        """
        This method is to be called in the event that the databse file does not exist
        this is tipically the case for first time usage of the application so make sure this
        method is called every time when the application is being run for the first time
        """
        try:

            db  = sql.connect("resources/94KEzWo.db")
            # Create a cursor object
            cursor = db.cursor()

            # SQL command to create a table
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                password TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                recovery TEXT UNIQUE 
            );
            ''' 
            # Execute the create table command
            cursor.execute(create_table_query)
            # Commit the changes
            db.commit()

            # Close the connection
            db.close()

            return {'status':True,'message':" Database was successfully generated"}
        
        except Exception as error:
            print(error)
            return {"status":False, "message":"Faied to generate database 2FA will not work"}
        

