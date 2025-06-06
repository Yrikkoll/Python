import requests
from bs4 import BeautifulSoup

def count_free_games():
    url = "https://store.epicgames.com/ru/free-games"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Request Error.")
        return 0

    soup = BeautifulSoup(response.text, "html.parser")
    return len(soup.find_all(string="Free"))

def main():
   
    current = count_free_games()

    
    try:
        with open("last_week_count.txt", "r") as f:
            previous = int(f.read().strip())
    except FileNotFoundError:
        previous = 0

    print(f"On previous week was: {previous} free games")
    print(f"On this week: {current} free games")

    if current > previous:
        print("The number of free games increased.")
    elif current < previous:
        print("The number of free games decreased .")
    else:
        print("The number of free game didn't change.")

    
    with open("last_week_count.txt", "w") as f:
        f.write(str(current))

if __name__ == "__main__":
    main()