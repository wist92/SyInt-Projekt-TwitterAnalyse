import pymysql
import datetime

class dbHandler():
  db = pymysql.connect(host="", port=3306, user="", passwd="", db="" )
  cursor = db.cursor()
  cursor2 = db.cursor()

  # Funktion zum Schließen der Datenbankverbindung
  def closeConn(self):
    dbHandler.cursor.close()
    dbHandler.db.close()

  # Testfunktion für die Verbindung, gibt Datenbankversion aus
  def getVersion(self):
    dbHandler.cursor.execute("SELECT VERSION()")
    data = dbHandler.cursor.fetchone()
    print ("Database version : %s " % data)


  # Einfuegen einer Auswertung in die Twitter-Tabelle
  # Param: session  - eindeutige ID für diese Auswertung
  #        hashtag  - haeufigster Hashtag
  #        location - haeufigster Ort
  def setData(self, session, hashtag, location):
    now = datetime.datetime.now()
    sql = "INSERT INTO twitter (session, hashtag, location, timestamp) VALUES (%s, %s, %s, %s)"
    dbHandler.cursor.execute(sql, (session, hashtag, location, now.strftime("%Y-%m-%d %H:%M:%S")))
    dbHandler.db.commit()

  # Gibt alle Eintraege der Twitter-Tabelle aus
  def getAll(self):
    dbHandler.cursor.execute("SELECT * FROM twitter")
    for r in dbHandler.cursor:
      print(str(r))

  # gibt das Land/ die Laender mit den meisten Tweets zurück
  #def getMaxLocation(self):
  #  dic = {}
  #  sqlLoc = "SELECT DISTINCT location FROM tweets"
  #  sqlCnt = "SELECT COUNT(*) FROM tweets WHERE location = %s"

  #  dbHandler.cursor.execute(sqlLoc)
  #  data = dbHandler.cursor.fetchall()
  # print("Data: "+str(data))

  # for r in dbHandler.cursor:
  #    print(str(r))
  #    dbHandler.cursor2.execute(sqlCnt, (str(r)))
  #    for t in dbHandler.cursor2:
  #      print("Hi: "+str(t))

  #  dic = {"Germany": 3, "Poland": 4, "Ireland":4}
  #  maxVal = max(dic.values())
  # maxKeys = [k for k, v in dic.items() if v == maxVal]
  #  print("Anzahl: " + str(maxVal) + " Länder: " + str(maxKeys))

  #def main():
  #  print("Daten vor Insert:")
  #  x = dbHandler()
  #  x.getAll()
  #  print("Daten nach Insert:")
  #  x.setData("003", "Pudding", "Ireland")
  #  x.getAll()
    #x.getMaxLocation()

  #  x.closeConn()

  #if __name__ == "__main__":
  #  main()
