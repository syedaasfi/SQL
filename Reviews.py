from dbutils import result_as_dict

def get_all_reviews(cursor):
    cursor.execute('select * from users')
    results=result_as_dict(cursor)
    for res in results:
            print(res)