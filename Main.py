import tkinter as tk
from tkinter import ttk
import requests

def get_player_stats(username):
    api_url = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={username}"
    response = requests.get(api_url)
    if response.status_code == 200:
        stats = response.text.split("\n")
        return stats
    else:
        return None

def get_ge_price(item_name):
    api_url = f"https://prices.runescape.wiki/api/v1/osrs/latest?id={item_name}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[item_name]["overall"]
    return None

def search_player():
    username = entry_username.get()
    player_stats = get_player_stats(username)
    if player_stats:
        show_stats_window(player_stats)
    else:
        show_error("Player data not found.")

def search_item():
    item_name = combo_item.get()
    item_price = get_ge_price(item_name)
    if item_price:
        show_item_price(item_name, item_price)
    else:
        show_error("Item data not found.")

def show_stats_window(stats):
    stats_window = tk.Toplevel(root)
    stats_window.title("Player Stats")
    stats_window.geometry("300x750")
    stats_text = "\n".join(
        ["Total level: " + stats[0].split(",")[1],
        "Total experience: " + stats[0].split(",")[2],
        "Attack level: " + stats[1].split(",")[1],
        "Attack experience: " + stats[1].split(",")[2],
        "Defence level: " + stats[2].split(",")[1],
        "Defence experience: " + stats[2].split(",")[2],
        "Strength level: " + stats[3].split(",")[1],
        "Strength experience: " + stats[3].split(",")[2],
        "Hitpoints level: " + stats[4].split(",")[1],
        "Hitpoints experience: " + stats[4].split(",")[2],
        "Ranged level: " + stats[5].split(",")[1],
        "Ranged experience: " + stats[5].split(",")[2],
        "Prayer level: " + stats[6].split(",")[1],
        "Prayer experience: " + stats[6].split(",")[2],
        "Magic level: " + stats[7].split(",")[1],
        "Magic experience: " + stats[7].split(",")[2],
        "Cooking level: " + stats[8].split(",")[1],
        "Cooking experience: " + stats[8].split(",")[2],
        "Woodcutting level: " + stats[9].split(",")[1],
        "Woodcutting experience: " + stats[9].split(",")[2],
        "Fletching level: " + stats[10].split(",")[1],
        "Fletching experience: " + stats[10].split(",")[2],
        "Fishing level: " + stats[11].split(",")[1],
        "Fishing experience: " + stats[11].split(",")[2],
        "Firemaking level: " + stats[12].split(",")[1],
        "Firemaking experience: " + stats[12].split(",")[2],
        "Crafting level: " + stats[13].split(",")[1],
        "Crafting experience: " + stats[13].split(",")[2],
        "Smithing level: " + stats[14].split(",")[1],
        "Smithing experience: " + stats[14].split(",")[2],
        "Mining level: " + stats[15].split(",")[1],
        "Mining experience: " + stats[15].split(",")[2],
        "Herblore level: " + stats[16].split(",")[1],
        "Herblore experience: " + stats[16].split(",")[2],
        "Agility level: " + stats[17].split(",")[1],
        "Agility experience: " + stats[17].split(",")[2],
        "Thieving level: " + stats[18].split(",")[1],
        "Thieving experience: " + stats[18].split(",")[2],
        "Slayer level: " + stats[19].split(",")[1],
        "Slayer experience: " + stats[19].split(",")[2],
        "Farming level: " + stats[20].split(",")[1],
        "Farming experience: " + stats[20].split(",")[2],
        "Runecrafting level: " + stats[21].split(",")[1],
        "Runecrafting experience: " + stats[21].split(",")[2],
        "Hunter level: " + stats[22].split(",")[1],
        "Hunter experience: " + stats[22].split(",")[2],
        "Construction level: " + stats[23].split(",")[1],
        "Construction experience: " + stats[23].split(",")[2]]

    )
    label_stats = tk.Label(stats_window, text=stats_text)
    label_stats.pack()

def show_item_price(item_name, item_price):
    item_window = tk.Toplevel(root)
    item_window.title("Item Price")
    price_text = f"The price of {item_name.capitalize()} is {item_price:,} coins."
    label_price = tk.Label(item_window, text=price_text)
    label_price.pack()

def show_error(message):
    error_window = tk.Toplevel(root)
    error_window.title("Error")
    label_error = tk.Label(error_window, text=message)
    label_error.pack()

# GUI
root = tk.Tk()
root.title("OSRS Tool")
root.geometry("300x200")

label_username = tk.Label(root, text="Enter username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

button_search_player = tk.Button(root, text="Search Player", command=search_player)
button_search_player.pack()

label_item = tk.Label(root, text="Select item:")
label_item.pack()
item_list = ["Bronze arrow", "Iron arrow", "Steel arrow"]  # Lisää esineitä tarvittaessa
combo_item = ttk.Combobox(root, values=item_list)
combo_item.pack()

button_search_item = tk.Button(root, text="Search Item", command=search_item)
button_search_item.pack()

root.mainloop()


# def main():
#     username = input("Anna pelaajan käyttäjänimi: ")
#     player_stats = get_player_stats(username)
#     if player_stats:
#         print(f"Total level: " + player_stats[0].split(",")[1])
#         print(f"Total experience: " + player_stats[0].split(",")[2])

#         print(f"Attack level: " + player_stats[1].split(",")[1])
#         print(f"Attack experience: " + player_stats[1].split(",")[2])

#         print(f"Defence level: " + player_stats[2].split(",")[1])
#         print(f"Defence experience: " + player_stats[2].split(",")[2])

#         print(f"Strength level: " + player_stats[3].split(",")[1])
#         print(f"Strength experience: " + player_stats[3].split(",")[2])

#         print(f"Hitpoints level: " + player_stats[4].split(",")[1])
#         print(f"Hitpoints experience: " + player_stats[4].split(",")[2])

#         print(f"Ranged level: " + player_stats[5].split(",")[1])
#         print(f"Ranged experience: " + player_stats[5].split(",")[2])

#         print(f"Prayer level: " + player_stats[6].split(",")[1])
#         print(f"Prayer experience: " + player_stats[6].split(",")[2])

#         print(f"Magic level: " + player_stats[7].split(",")[1])
#         print(f"Magic experience: " + player_stats[7].split(",")[2])

#         print(f"Cooking level: " + player_stats[8].split(",")[1])
#         print(f"Cooking experience: " + player_stats[8].split(",")[2]) 

#         print(f"Woodcutting level: " + player_stats[9].split(",")[1])
#         print(f"Woodcutting experience: " + player_stats[9].split(",")[2])

#         print(f"Fletching level: " + player_stats[10].split(",")[1])
#         print(f"Fletching experience: " + player_stats[10].split(",")[2])

#         print(f"Fishing level: " + player_stats[11].split(",")[1])
#         print(f"Fishing experience: " + player_stats[11].split(",")[2])

#         print(f"Firemaking level: " + player_stats[12].split(",")[1])
#         print(f"Firemaking experience: " + player_stats[12].split(",")[2])

#         print(f"Crafting level: " + player_stats[13].split(",")[1])
#         print(f"Crafting experience: " + player_stats[13].split(",")[2])

#         print(f"Smithing level: " + player_stats[14].split(",")[1])
#         print(f"Smithing experience: " + player_stats[14].split(",")[2])

#         print(f"Mining level: " + player_stats[15].split(",")[1])
#         print(f"Mining experience: " + player_stats[15].split(",")[2])

#         print(f"Herblore level: " + player_stats[16].split(",")[1])
#         print(f"Herblore experience: " + player_stats[16].split(",")[2])    

#         print(f"Agility level: " + player_stats[17].split(",")[1])
#         print(f"Agility experience: " + player_stats[17].split(",")[2])

#         print(f"Thieving level: " + player_stats[18].split(",")[1])
#         print(f"Thieving experience: " + player_stats[21].split(",")[2])

#         print(f"Slayer level: " + player_stats[18].split(",")[1])
#         print(f"Slayer experience: " + player_stats[22].split(",")[2])

#         print(f"Farming level: " + player_stats[19].split(",")[1])
#         print(f"Farming experience: " + player_stats[19].split(",")[2])

#         print(f"Runecrafting level: " + player_stats[20].split(",")[1])
#         print(f"Runecrafting experience: " + player_stats[20].split(",")[2])

#         print(f"Hunter level: " + player_stats[21].split(",")[1])
#         print(f"Hunter experience: " + player_stats[21].split(",")[2])

#         print(f"Construction level: " + player_stats[22].split(",")[1])
#         print(f"Construction experience: " + player_stats[22].split(",")[2])

#     else:
#         print("Pelaajan tietoja ei voitu hakea.")

