import pymysql


def get_result(sql):
    database = pymysql.connect("localhost", "root", password, "KDD")
    cursor = database.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    database.close()
    return result


def commit_sql(sql):
    database = pymysql.connect("localhost", "root", password, "KDD")
    cursor = database.cursor()
    cursor.execute(sql)
    database.commit()
    cursor.close()
    database.close()


def batch_commit(sql_array):
    database = pymysql.connect("localhost", "root", password, "KDD")
    cursor = database.cursor()
    error = []
    for i in range(len(sql_array)):
        try:
            cursor.execute(sql_array[i])
        except:
            error.append(str(i + 1))
    database.commit()
    cursor.close()
    database.close()
    return error


password = "094213"
