# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:36:56 2021

@author: olang
"""
import sys, os, json
import pandas as pd
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from cloudant.query import Query

def main(argv):
    if len(argv) > 0:  
        doc_list = []
        serviceUsername = input("username: ")
        servicePassword = input("password: ")
        serviceHost = input("host: ")
        databaseName = input("data base name: ")
        serviceURL = 'https://' + serviceUsername + ':' + servicePassword + '@' + serviceHost
        
        property_name = input("property name (if you provide a list use ';' to separate names): ")
        property_value = input("property value (if you provide a list use ';' to separate values): ")
        property_name_list = property_name.split(';');
        property_value_list = property_value.split(';');
        
        if len(property_name_list) != len(property_value_list):
            print('If property name is a list so property value must be a list of the same length!\n')
            
            property_name = input("property name (if you provide a list use ';' to separate names): ")
            property_value = input("property value (if you provide a list use ';' to separate values): ")
            property_name_list = property_name.split(';');
            property_value_list = property_value.split(';');

        try:
            client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
            client.connect()
            print('Client conected to cloudant!\n')
            if databaseName not in client.all_dbs():
                print("Database doesnt exist!\n")
            else:
                db = client[databaseName]
                print('Client connected to database: %s\n' % databaseName )          
      
                selector = dict((property_name_list[i],property_value_list[i]) for i in range(len(property_name_list)))
                pretty_selector = json.dumps(selector, indent = 4, ensure_ascii=False)
                print("Searching for... \n%s\n" % pretty_selector)
                query = Query(db, selector=selector)
                for doc in query()['docs']:
                    if doc not in doc_list:
                        doc_list.append(doc)
                        pretty_doc = json.dumps(doc, indent = 4, ensure_ascii=False)
                        print(pretty_doc)
                    else:
                        continue
                if len(doc_list) < 1:
                    print('No documents with specific propriesties found!\n')
        finally:
            client.disconnect()
    else:
        print("Too many or too little arguments!\n")
               
if __name__ == '__main__':
    main(sys.argv)