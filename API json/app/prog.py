# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:49:46 2022

@author: fifib
"""
import os
from flask import Flask, render_template, abort, url_for, json, jsonify, request
import json
import html
import sqlite3
app = Flask(__name__)



@app.route("/", methods=[ 'GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/sport", methods=[ 'GET', 'POST'])

def index2():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS sport(date TEXT, activite TEXT, ressenti TEXT)""")
    conn.commit()
    if request.method == 'POST':
        dates = request.form.get('date1')
        activites = request.form.get('activite1')
        ressentis = request.form.get("ressenti1")
        
        
        cursor.execute("""INSERT INTO sport(date, activite, ressenti) VALUES(?, ?, ?)""", (dates, activites, ressentis))
        conn.commit()
        conn.close()
        
    return render_template('sport.html')

@app.route("/travail", methods=[ 'GET', 'POST'])
def index3():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS travail(date TEXT, activite TEXT, ressenti TEXT)""")
    conn.commit()
    if request.method == 'POST':
        datet = request.form.get('date2')
        activitet = request.form.get('activite2')
        ressentit = request.form.get("ressenti2")
            
        cursor.execute("""INSERT INTO travail(date, activite, ressenti) VALUES(?, ?, ?)""", (datet, activitet, ressentit))
        conn.commit()
        conn.close()
    return render_template('travail.html')
    

@app.route("/jeu", methods=[ 'GET', 'POST'])
def index4():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS jeu(date TEXT, activite TEXT, ressenti TEXT)""")
    conn.commit()
    if request.method == 'POST':
        datej = request.form.get('date3')
        jeuj = request.form.get('jeu3')
        ressentij = request.form.get("ressenti3")
            
        cursor.execute("""INSERT INTO jeu(date, activite, ressenti) VALUES(?, ?, ?)""", (datej, jeuj, ressentij))
        conn.commit()
        conn.close()
    return render_template('jeu.html')

@app.route("/film", methods=[ 'GET', 'POST'])
def index5():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS film(date TEXT, activite TEXT, ressenti TEXT)""")
    conn.commit()
    if request.method == 'POST':
        datef = request.form.get('date4')
        filmf = request.form.get('film4')
        ressentif = request.form.get("ressenti4")
        
        
        cursor.execute("""INSERT INTO film(date, activite, ressenti) VALUES(?, ?, ?)""", (datef, filmf, ressentif))
        conn.commit()
        conn.close()
    return render_template('film.html')

@app.route("/autre", methods=[ 'GET', 'POST'])
def index6():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS autre(date TEXT, activite TEXT, ressenti TEXT)""")
    conn.commit()
    if request.method == 'POST':
        datea = request.form.get('date5')
        activitea = request.form.get('activite5')
        ressentia = request.form.get("ressenti5")
        
        
        cursor.execute("""INSERT INTO autre(date, activite, ressenti) VALUES(?, ?, ?)""", (datea, activitea, ressentia))
        conn.commit()
        conn.close()
    return render_template('autre.html')


@app.route("/qbe", methods=[ 'GET', 'POST'])
def index7():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        dateqbe = request.form.get('date6')
        
        cursor.execute("SELECT ressenti FROM sport WHERE date =?", (dateqbe,))
        average0 = int(cursor.fetchone()[0])
        cursor.execute("SELECT ressenti FROM travail WHERE date =?", (dateqbe,))
        average1 = int(cursor.fetchone()[0])
        cursor.execute("SELECT ressenti FROM jeu WHERE date =?", (dateqbe,))
        average2 = int(cursor.fetchone()[0])
        cursor.execute("SELECT ressenti FROM film WHERE date =?", (dateqbe,))
        average3 = int(cursor.fetchone()[0])
        cursor.execute("SELECT ressenti FROM autre WHERE date =?", (dateqbe,))
        average4 = int(cursor.fetchone()[0])
        averagetot = (average0 + average1 + average2 + average3 + average4) / 5
        data = ["", ""]
        data[0] = dateqbe
        data[1] = averagetot
        conn.close()
        return render_template('result.html', data=data)
    return render_template('qbe.html')

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.run(host='localhost', debug=True)