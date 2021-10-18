import configparser
import mysql.connector
import mysql.connector.errors
from mysql.connector import Error

def getconfig():
    config = configparser.ConfigParser()
    config.read("C:\\Users\\Punam\\workspace_python\\apidb\\utilities\\properties.ini")
    return config

consetting = {
    'host': getconfig()['SQL']['hostname'],
    'database': getconfig()['SQL']['database'],
    'user': getconfig()['SQL']['username'],
    'password': getconfig()['SQL']['password']
}

def getconnection():
    try:

        con= mysql.connector.connect(**consetting)
        if con.is_connected():
            print("Connected")
            return con
    except Error as e:
        print("not connected")


def getquery(query):
    con=getconnection()
    cursor= con.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    con.close()
    return row