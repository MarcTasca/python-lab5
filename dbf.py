import pymysql

def show_tasks(db):
    sql = 'select * from tasks'
    cursor=db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return sorted(result)

def new_task(db,task):
    sql='insert into tasks (task)values (%s)'
    cursor=db.cursor()
    cursor.execute(sql,(task,))
    db.commit()

#return None if there is no task to remove
def remove_task(db,task):
    cursor = db.cursor()
    sql='delete from tasks where id=%s'
    cursor.execute(sql, (task,))
    db.commit()
    return task

def remove_all_tasks(db,string):
    removed=[]
    sql='select task from tasks'
    cursor=db.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()
    for item in result:
        for task in item:
            if string in task:
                remove_task(db,task)
                removed.append(task)
    return removed
