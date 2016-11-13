from magic_cards_data import *
from tabulate import tabulate


conn = psycopg2.connect("dbname=magiccards user=chimble host=/tmp/")
cur = conn.cursor()


def show_all_cards():
    cur.execute("SELECT * FROM magiccards;")
    print(tabulate(cur.fetchall(), tablefmt="rst", headers=["id", "name",
          "type", "color", "cmc", "rarity", "price", "artist", "cardset"]))


def show_single_card():
    try:
        card_id = int(input("id? "))
        sql = "SELECT * FROM magiccards WHERE id = %s"
        cur.execute(sql, (card_id,))
        print(tabulate(cur, tablefmt="rst", headers=["id", "name", "type",
              "color", "cmc", "rarity", "price", "artist", "cardset"]))
    except:
        print("please enter integer ID. ")
        show_single_card()


def insert_card():
    sql = """INSERT INTO magiccards (name, type, color, cmc, rarity, price,
    artist, cardset) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    name_input = input("name? ")
    type_input = input("type? ")
    color_input = input("color? ")
    cmc_input = input("cmc? ")
    rarity_input = input("rarity? ")
    price_input = input("price? ")
    artist_input = input("artist? ")
    cardset_input = input("cardset? ")
    while True:
        try:
            if int(cmc_input) and float(price_input):
                cur.execute(sql, (name_input, type_input, color_input,
                            cmc_input, rarity_input, price_input,
                            artist_input, cardset_input))
                conn.commit()
                break
        except:
            print("use ints for cmc and floats for price.")
            break


def show_column_search():
    card_column = input("display by name, type, color, cmc, rarity, price, "
                        "artist, cardset? ")
    if card_column.lower() in ['name', 'type', 'color', 'cmc', 'rarity',
                               'price', 'artist', 'cardset']:
        card_value = input("choice of " + card_column.lower() + "? ").lower()
        sql = "SELECT * FROM magiccards WHERE " + card_column + " = %s"
        cur.execute(sql, (card_value,))
        print(tabulate(cur, tablefmt="rst", headers=["id", "name", "type",
              "color", "cmc", "rarity", "price", "artist", "cardset"]))
    else:
        print("please pick from appropriate columns. ")
        show_column_search()


def menu_stuff():
    choice = input("do you want to search by ID (1)? show all cards (2)? "
                   "add new card (3)? show cards by similarity (4)? ")
    if choice == '1':
        show_single_card()
    elif choice == '2':
        show_all_cards()
    elif choice == '3':
        insert_card()
    elif choice == '4':
        show_column_search()
    else:
        print("please choose 1, 2, 3, or 4. ")
        menu_stuff()
    menu_stuff()
menu_stuff()
