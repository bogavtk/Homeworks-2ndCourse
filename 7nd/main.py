import psycopg2


try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='q1w2e3r4',
        database='hw7',
        port='5432'
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        try:
            with connection.cursor() as cursor:
                sql = "CREATE TABLE Test_table (name varchar(40) not null, address varchar(70) not null)"
                cursor.execute(sql)
                print("[INFO] Test table created successfully")

        except Exception as _ex:
            pass

        finally:
            with connection.cursor() as cursor:

                sql = "DELETE FROM Test_table"
                cursor.execute(sql)

                sql = "INSERT INTO Test_table (name, address) VALUES ('Sasha', 'Kremlevskaya'), ('Bogdan', 'Yapeeva')"
                cursor.execute(sql)

                sql = "SELECT name, address FROM Test_table"
                cursor.execute(sql)
                print(cursor.fetchall())

                sql = "UPDATE Test_table SET name = 'Marat' WHERE name = 'Bogdan' "
                cursor.execute(sql)

                sql = "SELECT name, address FROM Test_table"
                cursor.execute(sql)
                print('\n', cursor.fetchall())

                sql = "DELETE FROM Test_table WHERE name = 'Liner' "
                cursor.execute(sql)

                sql = "SELECT name, address FROM Test_table"
                cursor.execute(sql)
                print('\n', cursor.fetchall())

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)

finally:
    if connection:
        connection.close()