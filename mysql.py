import MySQLdb
import time


class Mysql:

    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    def __init__(self):
        try:
            self.db = MySQLdb.connect('localhost', 'root', '######', 'TESTDB')
            self.cur = self.db.cursor()
        except MySQLdb.Error,e:
             print self.getCurrentTime(), "database connection error reason %d: %s" % (e.args[0], e.args[1])

    def insertData(self, table, my_dict):
        try:
            self.db.set_character_set('utf8')
            cols = ', '.join(my_dict.keys())
            values = '"," '.join(my_dict.values())
            sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, cols, '"'+values+'"')
            try:
                result = self.cur.execute(sql)
                insert_id = self.db.insert_id()
                self.db.commit()
                #check if executed successfully
                if result:
                    return insert_id
                else:
                    return 0
            except MySQLdb.Error,e:
                #rollback when failure
                self.db.rollback()
                #PK unique, cannot insert
                if "key 'PRIMARY'" in e.args[1]:
                    print self.getCurrentTime(), "data already exists. Didn't insert data"
                else:
                    print self.getCurrentTime(), "Insert data fail. Reason %d: %s" % (e.args[0], e.args[1])
        except MySQLdb.Error, e:
            print self.getCurrentTime(), "Database failure. Reason %d: %s" % (e.args[0], e.args[1])
