# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:43:41 2021

@author: olang
"""

import sys, os
import pandas as pd
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

def main(argv):
    if len(argv) == 2:
        dire = argv[1]
        k = 0
        serviceUsername = input("username: ")
        servicePassword = input("password: ")
        serviceHost = input("host: ")
        databaseName = input("data base name: ")
        serviceURL = 'https://' + serviceUsername + ':' + servicePassword + '@' + serviceHost
        
        try:
            client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
            client.connect()
            print("Connected!")

            
            if databaseName not in client.all_dbs():
                print("Creating " + databaseName + " data base!")
                db = client.create_database(databaseName)
                if db.exists():
                    print("'{0}' data base successfully created.\n".format(databaseName))
            else:
                db = client[databaseName]
                    
            for file in os.listdir(dire):
                if file.endswith('.json'):
                    k += 1
                    jsonFile = pd.read_json(file,typ="series")
                    doc = db.create_document(jsonFile)
                    if doc.exists():
                        print("Document '{0}' successfully created.".format(k))
        except:
            print("Something went wrong!")
        finally:
            client.disconnect()
            print("Disconnected!")
    else:
        print("Too many arguments!")
        
if __name__ == '__main__':
    main(sys.argv)
