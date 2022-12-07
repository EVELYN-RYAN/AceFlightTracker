import pandas as pd
import sqlite3
import numpy as np
from aceflighttracker.settings import DATABASES

def importCSVfile():
    #Create the dataframe for sqlite
    conn = sqlite3.connect(DATABASES['default']['NAME'])
    df_sqlite = pd.read_sql_query("SELECT * from Flight", conn)
    #create the dataframe for csv (Import)
    df_csv = pd.read_csv("tracker/importFiles/flight_tracker.csv")
    #Grab the name of all of the columns
    colObj_sqlite = df_sqlite.columns
    colNames = []
    for colName in colObj_sqlite:
        colNames.append(colName)
    #Grab the info from each column
    colValues_csv = []
    colValues_sqlite = []
    for val in range(0,len(colNames)):
        colValues_csv.append(df_csv.iloc[:,val].tolist())
        colValues_sqlite.append(df_sqlite.iloc[:,val].tolist())
    #Grab the flightid that is different
    dif1 = np.setdiff1d(colValues_csv[0], colValues_sqlite[0])
    dif2 = np.setdiff1d(colValues_sqlite[0], colValues_csv[0])
    newFlightIdVal = list(np.concatenate((dif1, dif2)))
    newFLightIdLoc = []
    for i in range(0,len(colValues_csv[0])):
        for x in range(0,len(newFlightIdVal)):
            if newFlightIdVal[x] == colValues_csv[0][i]:
                newFLightIdLoc.append(i)
                newFlightIdVal.pop(x)
                break
        if len(newFlightIdVal) == 0:
            break
    # Create the Insert SQL Statement
    # Create column section
    sqlColumns = ""
    for i in range(0,len(colNames)):
        sqlColumns = sqlColumns + '"' + colNames[i] + '"' + ","
    #remove the last comma
    sqlColumns = sqlColumns[:-1]
    cursor = conn.cursor()
    loopCount = 0
    for id in newFLightIdLoc:
        sqlInsert = "INSERT INTO Flight(" + sqlColumns + ") "
        sqlInsert = sqlInsert + "Values ("
        for x in range(0,len(colNames)):
            changeToString = ""
            if type(colValues_csv[x][id]) == type("String") or pd.isna(colValues_csv[x][id]):
                changeToString = '"' + str(colValues_csv[x][id]) + '"'
                sqlInsert = sqlInsert + changeToString + ","
            else:
                sqlInsert = sqlInsert + str(colValues_csv[x][id]) + ","
        sqlInsert = sqlInsert[:-1]
        sqlInsert = sqlInsert + ");"
        print(sqlInsert)
        loopCount += 1
        print(loopCount)
        cursor.execute(sqlInsert)
    conn.commit()
    conn.close()
