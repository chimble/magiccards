import psycopg2

conn = psycopg2.connect("dbname=magiccards user=chimble host=/tmp/")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS magiccards (id serial PRIMARY KEY,
            name text, type text, color text, cmc integer, rarity text,
            price real, artist text, cardset text);""")


def put_data_in():
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('lightning bolt', 'instant',
                'red', 1, 'common', 2.99, 'christopher rush', 'alpha');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('island', 'land', 'colorless',
                0, 'common', 0.01, 'mark poole', 'alpha');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('jace the mindsculptor',
                'planeswalker', 'blue', 4.00, 'mythic', 75, 'jason chan',
                'worldwake');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('tarmogoyf', 'creature',
                'green', 2, 'rare', 130.00, 'justin murray',
                'future sight');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('damnation', 'sorcery',
                'black', 4, 'rare', 63.00, 'kev walker', 'planar chaos');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('blood moon', 'enchantment',
                'red', 3, 'rare', 42.00, 'tom wanerstrand', 'the dark');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('vendilion clique', 'creature',
                'blue', 3, 'rare', 30.00, 'michael sutfin', 'morningtide');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('path to exile', 'instant',
                'white', 1, 'uncommon', 11.00, 'todd lockwood', 'conflux');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('platinum emperion',
                'creature', 'colorless', 8, 'mythic', 20.66, 'chris rahn',
                'scars of mirrodin');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('counterbalance',
                'enchantment', 'blue', 2, 'uncommon', 18.79, 'john zeleznik',
                'coldsnap');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('ensnaring bridge', 'artifact',
                'colorless', 3, 'rare', 37.35, 'pete venters',
                'stronghold');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('demonic tutor', 'sorcery',
                'black', 2, 'uncommon', 335.99, 'douglas schuler',
                'alpha');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('pact of the titan',
                'instant', 'red', 0, 'rare', 5.90, 'raymond swanland',
                'future sight');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('primeval titan', 'creature',
                'green', 6, 'mythic', 9.25, 'aleksi briclot', 'm11');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('city of brass', 'land',
                'colorless', 0, 'uncommon', 124.29, 'mark tedin',
                'arabian nights');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('forked bolt', 'sorcery',
                'red', 1, 'uncommon', 0.72, 'tomasz jedruszek',
                'rise of the eldrazi');""")
    cur.execute("""INSERT INTO magiccards (name, type, color, cmc, rarity,
                price, artist, cardset) VALUES ('grim monolith', 'artifact',
                'colorless', 2, 'rare', 48.52, 'chippy', 'urzas legacy');""")

if __name__ == '__main__':
    put_data_in()

conn.commit()
cur.close()
conn.close()
