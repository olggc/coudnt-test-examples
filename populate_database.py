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

def countJson(files):
    count = 0
    
    for file in files:
        count += 1
    return count
    
def main(argv):
    if len(argv) == 2:
        directory = argv[1]
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
                    print("%s data base successfully created.\n" % databaseName)
            else:
                db = client[databaseName]
                print("Acessing" + databaseName + " data base!")
            
            files = os.listdir(directory)
            n = countJson(files)
            for file in files:
                if file.endswith('.json'):
                    k += 1
                    jsonFile = pd.read_json(file,typ="series")
                    doc = db.create_document(jsonFile)
                    if doc.exists():
                        print("Document %s of %s Documents, successfully created." % (k,n))
        except:
            print("Something went wrong!")
        finally:
            client.disconnect()
            print("Disconnected!")
    else:
        print("Too many arguments!")
        
if __name__ == '__main__':
    main(sys.argv)
