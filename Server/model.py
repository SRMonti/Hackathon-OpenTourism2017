import sqlite3 as sql
import datetime

def insertMap(id, center_lat, center_lon, zoom):
    con = sql.connect("test.db")
    cur = con.cursor()
    reated = datetime.datetime.now()
    cur.execute("INSERT INTO map (id, reated, center_lat, center_lon, zoom) VALUES (?,?,?,?,?)", (id, reated, center_lat,center_lon, zoom))
    con.commit()
    con.close()

def retrieveMap():
    con = sql.connect("test.db")
    cur = con.cursor()
    cur.execute("SELECT id, reated, center_lat, center_lon, zoom FROM map")
    maps = cur.fetchall()
    con.close()
    return maps
