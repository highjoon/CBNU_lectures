import sqlite3


def CreateDB(cur):
    query = "CREATE TABLE IF NOT EXISTS Players (PlayerID id INTEGER PRIMARY KEY, Pname VARCHAR(20), Position " \
            "VARCHAR(20)); "
    cur.execute(query)


def ViewDataAll(cur, conn):
    query = "SELECT * FROM Players"
    cur.execute(query)
    rows = cur.fetchall()
    conn.commit()
    if not rows:
        print("등록된 선수가 없습니다.\n")
    else:
        for r in rows:
            print("%d / %s / %s" % (r[0], r[1], r[2]))
        print("\n조회가 완료되었습니다.")


def ViewData(cur, conn):
    query_all = "SELECT * FROM Players"
    cur.execute(query_all)
    rows = cur.fetchall()
    if not rows:
        print("등록된 선수가 없습니다.\n")
    else:
        try:
            pid = str(input("선수 ID 입력 : "))
            query = "SELECT * FROM Players WHERE Players.PlayerID = {0}".format(pid)
            result = cur.execute(query)
            conn.commit()
            for x in rows:
                if pid != x[y]:
                    print("\n해당 선수 정보가 없습니다.\n")
                else:
                    for r in result:
                        print("%d / %s / %s" % (r[0], r[1], r[2]))
                    print("\n조회가 완료되었습니다.\n")
        except:
            print("\n잘못된 입력입니다.\n")


def InsertData(cur, conn, plist):
    try:
        pid = int(input("선수 ID 입력 : "))
        for x in plist:
            if x[0] == pid:
                print("\n이미 존재하는 선수입니다.\n")
                break
            else:
                pass
        pname = str(input("선수 이름 입력 : "))
        position = str(input("포지션 입력 : "))
        data = (pid, pname, position)
        query = "INSERT INTO Players (PlayerID, Pname,  Position) VALUES (?, ?, ?)"
        cur.executemany(query, (data,))
        print("\n입력이 완료되었습니다.\n")
        conn.commit()
        plist.append(data)
    except:
        print("\n오류가 발생했습니다.\n")


def UpdateData(cur, conn):
    pid = int(input("수정할 선수 ID 입력 : "))
    name = str(input("이름 수정 : "))
    position = str(input("포지션 수정 : "))
    query_name = 'UPDATE Players SET Pname = "{0}" WHERE PlayerID = {1}'.format(name, pid)
    query_position = 'UPDATE Players SET Position = "{0}" WHERE PlayerID = {1}'.format(position, pid)
    query_all = "SELECT * FROM Players"
    cur.execute(query_all)
    rows = cur.fetchall()
    if not rows:
        print("등록된 선수가 없습니다.\n")
    else:
        try:
            if pid not in rows:
                print("\n해당 선수 정보가 없습니다.\n")
            else:
                if name != '' and position == '':
                    cur.execute(query_name)
                    conn.commit()
                    print("\n수정이 완료되었습니다.\n")
                elif name == '' and position != '':
                    cur.execute(query_position)
                    conn.commit()
                    print("\n수정이 완료되었습니다.\n")
                elif name != '' and position != '':
                    cur.execute(query_name)
                    cur.execute(query_position)
                    conn.commit()
                    print("\n수정이 완료되었습니다.\n")
                else:
                    print("\n입력이 취소되었습니다.\n")
        except:
            print("\n오류가 발생했습니다.\n")


def DeleteData(cur, conn):
    query_all = "SELECT * FROM Players"
    cur.execute(query_all)
    rows = cur.fetchall()
    pid = int(input("삭제할 선수 ID 입력 : "))
    i = 0
    while i < len(rows):
        if pid not in rows[i]:
            print("\n해당 선수 정보가 없습니다.\n")
            i += 1
        break
    try:
        query = "DELETE FROM Players WHERE PlayerID = {0}".format(pid)
        cur.execute(query)
        print("삭제가 완료되었습니다.\n")
        conn.commit()
    except:
        print("해당 선수는 존재하지 않습니다.\n")


def main():
    conn = sqlite3.connect('ChungBukFC.db')
    cursor = conn.cursor()
    CreateDB(cursor)
    playerList = []

    while True:
        print("충북 FC 선수단 관리 프로그램")
        print("\n1.  선수단 전체 정보 조회")
        print("2.  선수 정보 조회")
        print("3.  선수 정보 추가")
        print("4.  선수 정보 수정")
        print("5.  선수 정보 삭제")
        print("6.  프로그램 종료\n")
        opt = int(input("메뉴를 선택해주세요 : "))
        print()

        if opt == 1:
            print("선수단 전체 정보 조회 메뉴 입니다.\n")
            ViewDataAll(cursor, conn)

        elif opt == 2:
            print("선수 정보 조회 메뉴 입니다.\n")
            ViewData(cursor, conn)

        elif opt == 3:
            print("선수 정보 추가 메뉴 입니다.\n")
            InsertData(cursor, conn, playerList)

        elif opt == 4:
            print("선수 정보 수정 메뉴 입니다.\n")
            UpdateData(cursor, conn)

        elif opt == 5:
            print("선수 정보 삭제 메뉴 입니다.\n")
            DeleteData(cursor, conn)

        elif opt == 6:
            print("프로그램이 종료되었습니다.\n")
            conn.close()
            break

        else:
            print("잘못된 입력입니다.\n")


if __name__ == '__main__':
    main()