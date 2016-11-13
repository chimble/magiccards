from magic_cards_data import *


def show_all_cards():
    cur.execute("SELECT * FROM magiccards;")
    print(tabulate(cur.fetchall(), tablefmt="rst", headers = ["id", "name", "type", "color", "cmc", "rarity", "price"]))
#show_all_cards()

def show_single_card():
    user_id = int(input("id?"))
    sql = "SELECT * FROM magiccards WHERE id = %s"
    cur.execute(sql, (user_id,))
    print(tabulate(cur, tablefmt="fancy_grid", headers = ["id", "name", "type", "color", "cmc", "rarity", "price"]))
#show_single_card()

def insert_card():
    sql = "INSERT INTO magiccards (name, type, color, cmc, rarity, price) VALUES (%s, %s, %s, %s, %s, %s)"
    name_input = input("name? ")
    type_input = input("type? ")
    color_input = input("color? ")
    cmc_input = input("cmc? ")
    rarity_input = input("rarity? ")
    price_input = input("price? ")
    cur.execute(sql, (name_input, type_input, color_input, cmc_input, rarity_input, price_input))
    conn.commit()
#insert_card()

def show_column_choice():
    cur.execute("SELECT name, color FROM magiccards WHERE color LIKE '%blue';")
    print(tabulate(cur, tablefmt="fancy_grid", headers = ["id", "name", "type", "color", "cmc", "rarity", "price"]))

def menu_stuff():
    choice = int(input("do you want to search by ID (1)? show all cards (2)? add new card (3)?"))
    if choice == 1:
        show_single_card()
    if choice == 2:
        show_all_cards()
    if choice == 3:
        insert_card()
    menu_stuff()
menu_stuff()
#show_column_choice()
#show_all_cards()
