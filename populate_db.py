import sys

from PySide6.QtWidgets import QApplication

import init_paths
import sqlite_cmds as db

pillen = init_paths.mydbpath()
conn = db.create_connection(pillen)

pills = [
    ("Oxynorm Instant", "10 mg", 1.37),
    ("Redomex", "10 mg", 0.35),
    ("Trelegy Ellipta", "90 dos", 8.00),
    ("Deanxit Pi Pharma", "10 mg", 6.59),
    ("Laclimella", "1mg/2mg", 41.00),
    ("Tramadol", "150mg", 4.10),
    ("Pantomed", "40 mg", 2.84),
    ("Escitalopram", "10 mg", 3.59),
    ("Inderal", "40mg", 0.61),
    ("Steovit D3 Citroen", "500mg", 37.18),
    ("Closan, Comp", "10 mg", 15.62),
    ("Durogesic", "25mcg", 4.67),
    ("Atozet", "10mg/40mg", 8.04),
    ("Xgeva", "120mg", 8.00),
    ("Paracetemol Teva", "120", 1.20),
    ("Cymbalta", "60mg", 5.47),
    ("Lyrica", "150mg", 9.66),
    ("Lipantylnano", "145mg", 3.15),
    ("Arcoxia", "90mg", 6.33),
    ("Lyrica", "75mg", 6.07),
    ("Daflon", "120 x 500mg", 35.98),
    ("Adenuric", "80mg", 4.78),
    ("Jardiance", "10mg", 0.00),
    ("Etoricoxib", "60mg", 11.48),
    ("Celecoxib", "200mg", 1.29),
]
for pill in pills:
    db.add_pill(conn, pill)
conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sys.exit(app.exec())
