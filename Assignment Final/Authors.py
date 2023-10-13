from dbutils import result_as_dict
def get_all_authors(cursor):
    cursor.execute('select * from authors')
    results=result_as_dict(cursor)
    for result in results:
        print(result)

def remove_author(cursor,id):
    cursor.execute('DELETE from authors where author_id=?',id)
    print(f'{id} deleted')

def add_author(cursor,id,name,bio):
    cursor.execute('insert into authors (author_id,name,bio) VALUES (?,?,?)',id,name,bio)
    print(f'{id} added')

def author_by_id(cursor,id):
    cursor.execute('select * from authors where author_id=?',id)
    results= result_as_dict(cursor)
    for res in results:
            print(res)

def update_author(cursor,id,name=None,bio=None):
    if name != None and bio!=None:
        cursor.execute('UPDATE authors SET name=?,bio=? WHERE author_id=?',name,bio,id)
        print(f'{id} is updated with name {name} and bio {bio}')
    elif name==None and bio!=None:
        cursor.execute('UPDATE authors SET bio=? WHERE author_id=?',bio,id)
        print(f'{id} is updated with bio {bio}')
    elif bio==None and name!=None:
        cursor.execute('UPDATE Authors SET name=? WHERE author_id=?',name,id)
        print(f'{id} is updated with name {name} ')

def get_author_review(cursor,id):
    cursor.execute('''SELECT B.title, R.rating, R.review_text 
                      FROM Reviews R
                      JOIN Books B ON R.book_id = B.book_id
                      WHERE B.author_id = ?''',id)
    results=result_as_dict(cursor)
    for res in results:
            print(res)