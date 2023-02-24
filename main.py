from View.Display import Display
from Database.DataBase import Database

d1 = Display()
db = Database(d1)

for i in range(4):
    print('let\'s create some notes...')
    db.create()
print('ok, testing features...\n')

db.delete(3)
db.find(3)
db.find(2)
db.update(1)

print('all notes\n')
db.list()
