import sqlite3
import sys

from PySide6.QtWidgets import QMessageBox


def show_msg(title, msg):
    mbox = QMessageBox()
    mbox.setWindowTitle(title)
    mbox.setText(msg)
    mbox.exec()


def create_db(dbname):
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS 'pillen' (
        'id'	INTEGER NOT NULL UNIQUE,
        'naam'	TEXT,
        'volume'	TEXT,
        'prijs'	float,
        'lnaam' TEXT,
        PRIMARY KEY('id' AUTOINCREMENT)
        );
    """
    conn = sqlite3.connect(dbname)
    query = create_table_sql
    conn.execute(query)
    populate_db(conn)
    conn.close()


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        show_msg("Database error", e)
        sys.exit(0)
    return conn


def add_pill(conn, pill):
    sql = """ INSERT INTO pillen(naam, volume, prijs, lnaam)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, pill)
    conn.commit()
    show_msg("Pil toevoegen", "Pil werd toegevoegd")


def populate_db(conn):
    sql = """ INSERT INTO pillen(naam, volume, prijs, lnaam)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    pillen = [
        ("Oxynorm Instant", "10 mg", 1.37, "Oxynorm Instant - 10 mg"),
        ("Redomex", "10 mg", 0.35, "Redomex - 10 mg"),
        ("Trelegy Ellipta", "90 dos", 8.00, "Trelegy Ellipta - 90 dos"),
        ("Deanxit Pi Pharma", "10 mg", 6.59, "Deanxit Pi Pharma - 10 mg"),
        ("Laclimella", "1mg/2mg", 41.00, "Laclimella - 1mg/2mg"),
        ("Tramadol", "150mg", 4.10, "Tramadol - 150mg"),
        ("Pantomed", "40 mg", 2.84, "Pantomed - 40 mg"),
        ("Escitalopram", "10 mg", 3.59, "Escitalopram - 10 mg"),
        ("Inderal", "40mg", 0.61, "Inderal - 40mg"),
        ("Steovit D3 Citroen", "500mg", 37.18, "Steovit D3 Citroen - 500mg"),
        ("Closan", "10 mg", 15.62, "Closan - 10 mg"),
        ("Durogesic", "25mcg", 4.67, "Durogesic - 25mcg"),
        ("Atozet", "10mg/40mg", 8.04, "Atozet - 10mg/40mg"),
        ("Xgeva", "120mg", 8.00, "Xgeva - 120mg"),
        ("Paracetemol Teva", "120", 1.20, "Paracetemol Teva - 120"),
        ("Cymbalta", "60mg", 5.47, "Cymbalta - 60mg"),
        ("Lyrica", "150mg", 9.66, "Lyrica - 150mg"),
        ("Lipantylnano", "145mg", 3.15, "Lipantylnano - 145mg"),
        ("Arcoxia", "90mg", 6.33, "Arcoxia - 90mg"),
        ("Lyrica", "75mg", 6.07, "Lyrica - 75mg"),
        ("Daflon", "120 x 500mg", 35.98, "Daflon - 120 x 500mg"),
        ("Adenuric", "80mg", 4.78, "Adenuric - 80mg"),
        ("Jardiance", "10mg", 0.00, "Jardiance - 10mg"),
        ("Etoricoxib", "60mg", 11.48, "Etoricoxib - 60mg"),
        ("Celecoxib", "200mg", 1.29, "Celecoxib - 200mg"),
    ]

    for pil in pillen:
        cur.execute(sql, pil)
        conn.commit()


def get_pills(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM pillen ORDER BY naam")
    rows = cur.fetchall()
    return rows


# Function to update data in the table
def update_data(conn, update_sql):
    try:
        c = conn.cursor()
        c.execute(update_sql)
        conn.commit()
        print("Data updated successfully")
    except sqlite3.Error as e:
        print(e)


def update_pill(conn, update_sql):
    cur = conn.cursor()
    cur.execute(update_sql)
    conn.commit()
    show_msg("Update pillen", "Pill updated successfully")


def delete_pill(conn, ids):
    sql = "DELETE FROM pillen WHERE id=?"
    cur = conn.cursor()
    cur.execute(sql, (ids,))
    conn.commit()
    show_msg("Pil verwijderd", "Pill deleted successfully")
