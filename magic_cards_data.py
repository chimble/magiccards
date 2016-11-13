import psycopg2
from tabulate import tabulate

conn = psycopg2.connect("dbname=magiccards user=chimble host=/tmp/")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS magiccards (id serial PRIMARY KEY, name text, type text, color text, cmc integer, rarity text, price real);")
cur.execute("SELECT * FROM magiccards;")
#print(tabulate(cur.fetchall(), tablefmt="fancy_grid"))


# cur.execute("INSERT INTO magiccards (name, type, color, cmc, rarity, price) VALUES ('lightning bolt', 'instant', 'red', 1, 'common', 2.99);")
# cur.execute("INSERT INTO magiccards (name, type, color, cmc, rarity, price) VALUES ('island', 'land', 'colorless', 0, 'common', 0.01);")
# cur.execute("INSERT INTO magiccards (name, type, color, cmc, rarity, price) VALUES ('jace the mindsculptor', 'planeswalker', 'blue', 4.00, 'mythic', 75);")
# cur.execute("INSERT INTO magiccards (name, type, color, cmc, rarity, price) VALUES ('tarmogoyf', 'creature', 'green', 2, 'rare', 130.00);")
# cur.execute("INSERT INTO magiccards (name, type, color, cmc, rarity, price) VALUES ('damnation', 'sorcery', 'black', 4, 'rare', 63.00);")
# cur.execute("INSERT INTO magiccards (name, type, color, cmc, rarity, price) VALUES ('blood moon', 'enchantment', 'red', 3, 'rare', 42.00);")
# cur.execute("INSERT INTO magiccards (name, type, color, cmc, rarity, price) VALUES ('vendilion clique', 'creature', 'blue', 3, 'rare', 30.00);")
# cur.execute("INSERT INTO magiccards (name, type, color, cmc, rarity, price) VALUES ('path to exile', 'instant', 'white', 1, 'uncommon', 11.00);")

conn.commit()
