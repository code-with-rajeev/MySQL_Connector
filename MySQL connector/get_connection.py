# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 22:37:40 2020

@author: ACER
"""

import time
import mysql.connector as a


def connector(user=false,password=false):
    global a
    print("executing ___grps_connector____ ")
    time.sleep(1)
    print("connecting grps to Mysql \n This may take a while...")
    time.sleep(1)
    x = None
    user_ = user if user else input("\nplease enter your username: ")
    password_ = password if password else input("\nplease enter your password: ")

    try:
        x = a.connect(user = user_, password = password_)
    except Exception as y:
        print(f"\nGRPS_CONN_FAILUE_ERROR : \n{y}")
        choice= input("\n want to reconnect[y/n]")
        if choice in ["Y","y"]:
            print("reconnecting...\n")
            connector()
        elif choice in ["N","n"]:
            print("cancelled")
            return None
        else:
            print("invalid option")
            connector()
    return x
connect = connector
if __name__ == "__main__":
    print(connector())
