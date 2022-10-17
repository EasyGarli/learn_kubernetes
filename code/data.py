import os
import psycopg2

def get_account_data(username):
    print(username)
    if username:
        try:
            connection = psycopg2.connect(user=os.environ.get('DB_USERNAME'),
                                    password=os.environ.get('DB_PASSWORD'),
                                    host=os.environ.get('DB_ADDRESS'),
                                    port=os.environ.get('DB_PORT'),
                                    database=os.environ.get('DB_NAME'))
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM accounts WHERE username='{}'".format(username))
            record = str(cursor.fetchone()).split(',')
            return "{} {}".format(record[1], record[3])
        except:
            return "Something go wrong"
    else:
        return "No username"