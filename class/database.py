#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="", database="projetPython")
cursor = conn.cursor()
conn.close()
