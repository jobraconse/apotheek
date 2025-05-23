import os

from PySide6.QtCore import QDir, QStandardPaths

from sqlite_cmds import create_db


def mydbpath():
    save_dir = (
        QStandardPaths.locate(
            QStandardPaths.StandardLocation.AppConfigLocation,
            "",
            QStandardPaths.LocateOption.LocateDirectory,
        )
        + "apotheek/"
    )
    db_file = save_dir + "apotheek.sqlite"
    mdir = QDir()
    if not mdir.exists(save_dir):
        mdir.mkpath(save_dir)

    if not os.path.exists(db_file):  # noqa: PTH110
        create_db(db_file)

    return db_file


def mypdfpath():
    save_dir = QStandardPaths.locate(
        QStandardPaths.StandardLocation.DesktopLocation,
        "",
        QStandardPaths.LocateOption.LocateDirectory,
    )
    pdf_file = save_dir + "output.pdf"
    return pdf_file
