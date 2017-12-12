import sqlite3

conn = sqlite3.connect('tut.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot (unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(145543423,'2016-01-04','Python',5)")
    conn.commit()
    c.close()
    conn.close()
    
    
create_table()
data_entry()