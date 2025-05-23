import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QApplication, QMainWindow

import create_pdf
import form
import init_paths as i
import sqlite_cmds as db

pillen = i.mydbpath()
pdfpath = i.mypdfpath()


class Window(QMainWindow, form.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.center()
        self.add_pillen_aan_lijst(self.lwPillen)
        self.add_pillen_aan_lijst(self.lwUpdaten)
        self.add_pillen_aan_lijst(self.lwVerwijderen)
        self.stackedWidget.setCurrentIndex(0)
        self.btnNaarRechts.clicked.connect(self.naar_rechts)
        self.btnNaarLinks.clicked.connect(self.naar_links)
        self.btnBestellen.clicked.connect(self.doe_bestelling)
        self.actionBestellen.triggered.connect(self.tab_bestellen)
        self.actionUpdate.triggered.connect(self.tab_updaten)
        self.actionToevoegen.triggered.connect(self.tab_toevoegen)
        self.actionVerwijderen.triggered.connect(self.tab_verwijderen)
        self.btnPrintBestelling.clicked.connect(self.print_bestelling)
        self.btnUpdaten.clicked.connect(self.update_in_db)
        self.btnToevoegenDatabase.clicked.connect(self.pil_toevoegen_aan_db)
        self.btnVerwijderen.clicked.connect(self.verwijder_pil_uit_db)
        self.lwUpdaten.itemSelectionChanged.connect(self.tab_updaten)
        self.lwVerwijderen.itemSelectionChanged.connect(self.tab_verwijderen)

    def verwijder_pil_uit_db(self):
        # self.stackedWidget.setCurrentIndex(5)
        ids = self.lineEditVerwijderID.text()
        conn = db.create_connection(pillen)
        db.delete_pill(conn, ids)
        conn.close()

        self.lineEditVerwijderNaam.setText("")
        self.lineEditVerwijderVolume.setText("")
        self.lineEditVerwijderPrijs.setText("")
        self.lineEditVerwijderID.setText("")

    def pil_toevoegen_aan_db(self):
        self.stackedWidget.setCurrentIndex(4)
        naam = self.lineEditToevoegenNaam.text()
        volume = self.lineEditToevoegenVolume.text()
        prijs = self.lineEditTotPrijs.text()
        lnaam = f"{naam} - {volume}"
        conn = db.create_connection(pillen)
        db.add_pill(conn, (naam, volume, prijs, lnaam))
        conn.close()
        self.reset_lists()
        self.lineEditToevoegenNaam.setText("")
        self.lineEditToevoegenVolume.setText("")
        self.lineEditTotPrijs.setText("")

    def center(self):
        center_point = QGuiApplication.screens()[0].geometry().center()
        self.move(center_point - self.frameGeometry().center())

    def reset_lists(self):
        self.lwBestellen.clear()
        self.lwPillen.clear()
        self.lwVerwijderen.clear()
        self.add_pillen_aan_lijst(self.lwPillen)
        self.add_pillen_aan_lijst(self.lwUpdaten)
        self.add_pillen_aan_lijst(self.lwVerwijderen)

    def print_bestelling(self):
        text = []
        for index in range(self.lwBestellen.count()):
            item = self.lwBestellen.item(index)
            if item is not None:
                text.append(item.text())
        prijs = self.lineEditTotPrijs.text()
        create_pdf.create_pdf(pdfpath, text, prijs)
        self.reset_lists()
        self.stackedWidget.setCurrentIndex(0)

    def tab_toevoegen(self):
        self.stackedWidget.setCurrentIndex(4)

    def tab_verwijderen(self):
        self.stackedWidget.setCurrentIndex(5)
        selected_items = self.lwVerwijderen.selectedItems()
        if selected_items:  # Check if the list is not empty
            selected_text = selected_items[0].text()
            conn = db.create_connection(pillen)
            rows = db.get_pills(conn)
            for pil in rows:
                if pil[4] == selected_text:
                    self.lineEditVerwijderID.setText(str(pil[0]))
                    self.lineEditVerwijderNaam.setText(pil[1])
                    self.lineEditVerwijderVolume.setText(pil[2])
                    self.lineEditVerwijderPrijs.setText(str(pil[3]))
            conn.close()

    def update_in_db(self):
        ids = self.lineEditUpdateID.text()
        naam = self.lineEditUpdateNaam.text()
        volume = self.lineEditUpdateVolume.text()
        prijs = self.lineEditUpdatePrijs.text()
        lnaam = f"{naam} - {volume}"

        conn = db.create_connection(pillen)
        c = conn.cursor()
        sql = """UPDATE pillen SET naam=?, volume=?, prijs=?, lnaam=? WHERE id=?"""
        c.execute(sql, (naam, volume, prijs, ids, lnaam))
        conn.commit()
        conn.close()

        self.lineEditUpdateID.setText("")
        self.lineEditUpdateNaam.setText("")
        self.lineEditUpdateVolume.setText("")
        self.lineEditUpdatePrijs.setText("")
        db.show_msg("Database Update", naam + " werd opgewaardeerd")

    def tab_updaten(self):
        self.stackedWidget.setCurrentIndex(3)
        selected_items = self.lwUpdaten.selectedItems()
        if selected_items:  # Check if the list is not empty
            selected_text = selected_items[0].text()
            conn = db.create_connection(pillen)
            rows = db.get_pills(conn)
            for pil in rows:
                if pil[4] == selected_text:
                    self.lineEditUpdateID.setText(str(pil[0]))
                    self.lineEditUpdateNaam.setText(pil[1])
                    self.lineEditUpdateVolume.setText(pil[2])
                    self.lineEditUpdatePrijs.setText(str(pil[3]))
            conn.close()

    def tab_bestellen(self):
        self.stackedWidget.setCurrentIndex(1)
        self.reset_lists()

    def doe_bestelling(self):
        bestellen = []
        prijs = 0
        self.stackedWidget.setCurrentIndex(2)
        for index in range(self.lwBestellen.count()):
            item = self.lwBestellen.item(index)
            if item is not None:
                bestellen.append(item.text())
                self.plainTextEdit.appendPlainText(item.text())

        conn = db.create_connection(pillen)
        file = db.get_pills(conn)
        for pills in file:
            lnaam = pills[4]
            if bestellen.__contains__(lnaam):
                prijs += float(pills[3])
        rounded_price = round(prijs, 2)
        self.lineEditTotPrijs.setText(str(rounded_price))
        conn.close()

    def naar_links(self):
        selected_items = self.lwBestellen.selectedItems()
        if selected_items:
            self.lwBestellen.takeItem(
                self.lwBestellen.row(selected_items[0]),
            )

    def naar_rechts(self):
        selected_items = self.lwPillen.selectedItems()
        if selected_items:
            selected_text = selected_items[0].text().strip()
            self.lwBestellen.addItem(selected_text)

    def add_pillen_aan_lijst(self, lijst):
        conn = db.create_connection(pillen)
        result = db.get_pills(conn)
        for row in result:
            pil = row[4]
            lijst.addItem(pil)
        conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
