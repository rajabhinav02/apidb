import mysql.connector
from utilities.Configuration import *


def addbook(query):
    row = getquery(query)
    body = {}
    body['name'] = row[0]
    body['isbn'] = row[1]
    body['aisle'] = row[2]
    body['author'] = row[3]
    # body={
    #     'name': row[0],
    #     'isbn': row[1],
    #     'aisle': row[2],
    #     'author': row[3]
    # }

    return body


def delbook(id):
    bodyd = {

        "ID": id

    }
    return bodyd
