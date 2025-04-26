#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 19:12:19 2025

@author: robertfjellin_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'qwerty123'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34368
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print ("Connection was successful!")

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                # Insert data in animals collection
                result = self.database.animals.insert_one(data)  # data should be dictionary   
                # Return true using acknowledged
                return result.acknowledged
            except Exception:
                # Return false if insertion failed
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        try:
            # Use find method to locate documents matching data
            result = self.database.animals.find(data)
            # Convert results to list
            animals_list = list(result)
            return animals_list
        except Exception:
            return[]
        
# Method for Update
    def update(self, data, newData):
        try:
            # Using update_many to update all data matching the data argument
            result = self.database.animals.update_many(data, {"$set": newData})
            # return count of modified documents
            return result.modified_count;
        except Exception:
            return 0
    
# Method for Delete
    def delete(self, data):
        try:
            # Delete all documents matching data
            result = self.database.animals.delete_many(data)
            return result.deleted_count
        except Exception:
            return 0
            
            
            
        