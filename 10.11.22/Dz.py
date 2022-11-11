import pymysql
try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="",
        password="Cisco123@45@g",
        database="Basket",
        cursorclass=pymysql.cursors.DictCursor     )
    print("Okay")
# finally: connection.close()
except: print("error")
count = 0
while True:
  with connection.cursor() as cursor:
    log = input("Enter your login: ")
    passwd = input("Enter your password: ")
    select_all = f"SELECT Login,Passwd FROM `Auth` where Login = '{log}';"
    cursor.execute(select_all)
    result = cursor.fetchall()
    print(result)
    try:
        if result[0].get('Login') == log and result[0].get('Passwd') == passwd:
            print("You logged in!")
        else:
            count = +1
            print("Bad password!")
            continue
    except:
         print("Incorrect password!")
         break
    while True:
        sectorya = input("Choose app: print - Bask, print - Records, print - News: ")
        sectora = int(input("""Choose \t #1 Add info
         #2 Delete info 
         #3 Update info 
         #4 Print info BD
         #5 Exit: """))
        if sectora == 1:
            if sectorya == "Bask":
                add1 = input("Enter name product: ")
                add2 = input("Enter short infor prod: ")
                add3 = float(input("Enter cost prod: "))
                cursor.execute(f"INSERT INTO `Bask` (Nameprod, Infoprod, Costprod) VALUES ('{add1}','{add2}', '{add3}')")
                connection.commit()
            elif sectorya == "Records":
                add1 = input("Enter name person: ")
                add2 = input("Enter name of game: ")
                add3 = int(input("Enter rank: "))
                cursor.execute(
                    f"INSERT INTO `Record` (Nameplrec, Namerec, Placerec) VALUES ('{add1}','{add2}', '{add3}')")
                connection.commit()
            elif sectorya == "News":
                add1 = input("Enter name title-new: ")
                add2 = input("Enter information: ")
                add3 = input("Enter date publication: ")
                cursor.execute(
                    f"INSERT INTO `News` (Namenew, Infonew, Datenew) VALUES ('{add1}','{add2}', '{add3}')")
                connection.commit()
        elif sectora == 2:
            sectorb = int(input("Take #1 delete one #2 Delete all info: "))
            if sectorb == 1:
                if sectorya == "Bask":
                    print("<:Tag for delete in this sector: Nameprod, Infoprod, Costprod:>")
                    add1 = input("Enter Tag from BD: ")
                    add2 = input("Enter name product: ")
                    cursor.execute(f"DELETE FROM `Bask` WHERE {add1} = '{add2}';")
                    connection.commit()
                    print("Done!")
                elif sectorya == "Records":
                    print("<:Tag for delete in this sector: Nameplrec, Namerec, Placerec:>")
                    add1 = input("Enter Tag from BD: ")
                    add2 = input("Enter name person: ")
                    cursor.execute(f"DELETE FROM `Record` WHERE {add1} = '{add2}';")
                    connection.commit()
                    print("Done!")
                elif sectorya == "News":
                    print("<:Tag for delete in this sector: Namenew, Infonew, Datenew:>")
                    add1 = input("Enter Tag from BD: ")
                    add2 = input("Enter name news: ")
                    cursor.execute(f"DELETE FROM `News` WHERE {add1} = '{add2}';")
                    connection.commit()
                    print("Done!")
            elif sectorb == 2:
                if sectorya == "Bask":
                    cursor.execute(f"truncate `Bask`")
                    connection.commit()
                    print("Done!")
                elif sectorya == "Records":
                    cursor.execute(f"truncate `Record`")
                    connection.commit()
                    print("Done!")
                elif sectorya == "News":
                    cursor.execute(f"truncate `News`")
                    connection.commit()
                    print("Done!")
        elif sectora == 3:
            if sectorya == "Bask":
                print("<:Tag for redact in this sector: Nameprod, Infoprod, Costprod:>")
                seltype = input("What are you want redact: ")
                redactdat = input("Infor to replace: ")
                path = input("Enter id of person from BD: ")
                cursor.execute(f"UPDATE `Bask` SET {seltype} = '{redactdat}' WHERE id = {path}")
                connection.commit()
                print("Done!")
            elif sectorya == "Records":
                print("<:Tag for redact in this sector: Nameplrec, Namerec, Placerec:>")
                seltype = input("What are you want redact: ")
                redactdat = input("Infor to replace: ")
                path = input("Enter id of person from BD: ")
                cursor.execute(f"UPDATE `Record` SET {seltype} = '{redactdat}' WHERE id = {path}")
                connection.commit()
                print("Done!")
            elif sectorya == "News":
                print("<:Tag for redact in this sector: Namenew, Infonew, Datenew:>")
                seltype = input("What are you want redact: ")
                redactdat = input("Infor to replace: ")
                path = input("Enter id of person from BD: ")
                cursor.execute(f"UPDATE `News` SET {seltype} = '{redactdat}' WHERE id = {path}")
                connection.commit()
                print("Done!")
        elif sectora == 4:
            sectorb = int(input("Find #1 For all #2 For param: "))
            if sectorb == 1:
                if sectorya == "Bask":
                    cursor.execute("SELECT * FROM `Bask`;")
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
                elif sectorya == "Records":
                    cursor.execute("SELECT * FROM `Record`;")
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
                elif sectorya == "News":
                    cursor.execute("SELECT * FROM `News`;")
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
            elif sectorb == 2:
                if sectorya == "Bask":
                    sel = input("Print tag Infoprod - info, Costprod - Cost, * - All product name: ")
                    name = input("Take name product: ")
                    cursor.execute(f"SELECT {sel} FROM `Bask` where Nameprod = '{name}';")
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
                elif sectorya == "Records":
                    cursor.execute("SELECT Nameplrec,Placerec FROM `Record` where Placerec between 1 and 5;")
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
                elif sectorya == "News":
                    cursor.execute(f"SELECT * FROM `News` where Datenew >= '2022-10-29';")
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
        elif sectora == 5:
            print("Exit!")
            break