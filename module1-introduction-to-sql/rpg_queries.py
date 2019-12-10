import sqlite3
import rpg_queries

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = 'SELECT Count(character_id) From charactercreator_character;'
print("Total characters:", curs.execute(query).fetchall())
print("Clerics: ", curs.execute('SELECT Count(character_ptr_id) From charactercreator_cleric;').fetchall())
print("Fighters: ", curs.execute('SELECT Count(character_ptr_id) From charactercreator_fighter;').fetchall())
print("Mages: ", curs.execute('SELECT Count(character_ptr_id) From charactercreator_mage;').fetchall())
print("Necromancers:", curs.execute('SELECT Count(mage_ptr_id) From charactercreator_necromancer;').fetchall())
print("Thieves: ", curs.execute('SELECT Count(character_ptr_id) From charactercreator_thief;').fetchall())
x = curs.execute('SELECT Count(item_id) From armory_item;').fetchall()
y = curs.execute('SELECT Count(item_ptr_id) From armory_weapon;').fetchall()
print("Total items: ", x)
print("Items that are weapons: ", y)
print("Items that are not weapons: ", x[0][0] - y[0][0])
print("Items each character has: (character id, # of items)", curs.execute('select character_id, count(item_id) from charactercreator_character_inventory group by character_id limit 20;').fetchall())
print("Weapons each character has: (character id, # of weapons)", curs.execute('SELECT character_id,COUNT(item_ptr_id) FROM armory_weapon as aw, armory_item as ai, charactercreator_character_inventory as cci WHERE aw.item_ptr_id = ai.item_id AND ai.item_id = cci.item_id GROUP BY character_id LIMIT 20;').fetchall())


curs.close()
conn.commit()

import pandas as pd
print('\n\nAssignment 2')
df = pd.read_csv('buddymove_holidayiq.csv')
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs2 = conn.cursor()
#df.to_sql('review', conn)
print("Total rows: ", curs2.execute('SELECT Count(index) From review;').fetchall())
print("users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category: ", conn.execute('SELECT Nature, Shopping FROM buddy WHERE Nature > 100 AND Shopping > 100').fetchall())
