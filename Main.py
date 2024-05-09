import requests

def get_player_stats(username):
    api_url = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={username}"
    response = requests.get(api_url)
    if response.status_code == 200:
        stats = response.text.split("\n")
        return stats
    else:
        return None

def main():
    username = input("Anna pelaajan käyttäjänimi: ")
    player_stats = get_player_stats(username)
    if player_stats:
        print(f"Total level: " + player_stats[0].split(",")[1])
        print(f"Total experience: " + player_stats[0].split(",")[2])

        print(f"Attack level: " + player_stats[1].split(",")[1])
        print(f"Attack experience: " + player_stats[1].split(",")[2])

        print(f"Defence level: " + player_stats[2].split(",")[1])
        print(f"Defence experience: " + player_stats[2].split(",")[2])

        print(f"Strength level: " + player_stats[3].split(",")[1])
        print(f"Strength experience: " + player_stats[3].split(",")[2])

        print(f"Hitpoints level: " + player_stats[4].split(",")[1])
        print(f"Hitpoints experience: " + player_stats[4].split(",")[2])

        print(f"Ranged level: " + player_stats[5].split(",")[1])
        print(f"Ranged experience: " + player_stats[5].split(",")[2])

        print(f"Prayer level: " + player_stats[6].split(",")[1])
        print(f"Prayer experience: " + player_stats[6].split(",")[2])

        print(f"Magic level: " + player_stats[7].split(",")[1])
        print(f"Magic experience: " + player_stats[7].split(",")[2])

        print(f"Cooking level: " + player_stats[8].split(",")[1])
        print(f"Cooking experience: " + player_stats[8].split(",")[2]) 

        print(f"Woodcutting level: " + player_stats[9].split(",")[1])
        print(f"Woodcutting experience: " + player_stats[9].split(",")[2])

        print(f"Fletching level: " + player_stats[10].split(",")[1])
        print(f"Fletching experience: " + player_stats[10].split(",")[2])

        print(f"Fishing level: " + player_stats[11].split(",")[1])
        print(f"Fishing experience: " + player_stats[11].split(",")[2])

        print(f"Firemaking level: " + player_stats[12].split(",")[1])
        print(f"Firemaking experience: " + player_stats[12].split(",")[2])

        print(f"Crafting level: " + player_stats[13].split(",")[1])
        print(f"Crafting experience: " + player_stats[13].split(",")[2])

        print(f"Smithing level: " + player_stats[14].split(",")[1])
        print(f"Smithing experience: " + player_stats[14].split(",")[2])

        print(f"Mining level: " + player_stats[15].split(",")[1])
        print(f"Mining experience: " + player_stats[15].split(",")[2])

        print(f"Herblore level: " + player_stats[16].split(",")[1])
        print(f"Herblore experience: " + player_stats[16].split(",")[2])    

        print(f"Agility level: " + player_stats[17].split(",")[1])
        print(f"Agility experience: " + player_stats[17].split(",")[2])

        print(f"Thieving level: " + player_stats[18].split(",")[1])
        print(f"Thieving experience: " + player_stats[21].split(",")[2])

        print(f"Slayer level: " + player_stats[18].split(",")[1])
        print(f"Slayer experience: " + player_stats[22].split(",")[2])

        print(f"Farming level: " + player_stats[19].split(",")[1])
        print(f"Farming experience: " + player_stats[19].split(",")[2])

        print(f"Runecrafting level: " + player_stats[20].split(",")[1])
        print(f"Runecrafting experience: " + player_stats[20].split(",")[2])

        print(f"Hunter level: " + player_stats[21].split(",")[1])
        print(f"Hunter experience: " + player_stats[21].split(",")[2])

        print(f"Construction level: " + player_stats[22].split(",")[1])
        print(f"Construction experience: " + player_stats[22].split(",")[2])

    else:
        print("Pelaajan tietoja ei voitu hakea.")

if __name__ == "__main__":
    main()
