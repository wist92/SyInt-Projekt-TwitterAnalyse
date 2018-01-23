import pymysql
import datetime


class DbHandler():
    db = pymysql.connect(host="", port=3306, user="", passwd="", db="")
    cursor = db.cursor()
    cursor2 = db.cursor()

    # Funktion zum Schließen der Datenbankverbindung
    def close_conn(self):
        DbHandler.cursor.close()
        DbHandler.db.close()

    # Testfunktion für die Verbindung, gibt Datenbankversion aus
    def get_version(self):
        DbHandler.cursor.execute("SELECT VERSION()")
        data = DbHandler.cursor.fetchone()
        print("Database version : %s " % data)

    # Einfuegen einer Auswertung in die Twitter-Tabelle
    # Param: session  - eindeutige ID für diese Auswertung
    #        hashtag  - haeufigster Hashtag
    #        location - haeufigster Ort
    def set_data(self, session, hashtag, location):
        now = datetime.datetime.now()
        sql = "INSERT INTO twitter (session, hashtag, location, timestamp) VALUES (%s, %s, %s, %s)"
        DbHandler.cursor.execute(sql, (session, hashtag, location, now.strftime("%Y-%m-%d %H:%M:%S")))
        DbHandler.db.commit()

    # Gibt alle Eintraege der Twitter-Tabelle aus
    def get_all(self):
        DbHandler.cursor.execute("SELECT * FROM twitter")
        for r in DbHandler.cursor:
            print(str(r))