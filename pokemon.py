import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon(name):
    """Retrieve Pokémon data from the PokéAPI."""

    url = f"{BASE_URL}{name.lower()}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        return None

    data = response.json()

    return {
        "name": data["name"].title(),
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"].title() for t in data["types"]],
        "abilities": [a["ability"]["name"].title() for a in data["abilities"]],
        "stats": {
            s["stat"]["name"].title(): s["base_stat"]
            for s in data["stats"]
        },
    }


def show_pokemon(pokemon):
    """Display information about a Pokémon."""

    print("\n==============================")
    print(f"Name      : {pokemon['name']}")
    print(f"Height    : {pokemon['height']}")
    print(f"Weight    : {pokemon['weight']}")
    print(f"Types     : {', '.join(pokemon['types'])}")
    print(f"Abilities : {', '.join(pokemon['abilities'])}")

    print("\nBase Stats")

    for stat, value in pokemon["stats"].items():
        print(f"{stat:<12}: {value}")

    print("==============================\n")


def compare_pokemon(first, second):
    """Compare two Pokémon."""

    print("\n========== Pokémon Comparison ==========")
    print(f"{first['name']} vs {second['name']}\n")

    print(f"Height : {first['height']} | {second['height']}")
    print(f"Weight : {first['weight']} | {second['weight']}")

    print("\nBase Stats")

    for stat in first["stats"]:
        print(
            f"{stat:<12}"
            f"{first['stats'][stat]:>4}"
            f" | "
            f"{second['stats'][stat]:>4}"
        )

    print("========================================\n")


def main():
    """Run the Pokédex application."""

    while True:
        print("===== POKÉDEX MENU =====")
        print("1. Search Pokémon")
        print("2. Compare Pokémon")
        print("3. Quit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            name = input("\nEnter Pokémon name: ")

            pokemon = get_pokemon(name)

            if pokemon:
                show_pokemon(pokemon)
            else:
                print("\nPokémon not found.\n")

        elif choice == "2":
            first_name = input("\nFirst Pokémon: ")
            second_name = input("Second Pokémon: ")

            first = get_pokemon(first_name)
            second = get_pokemon(second_name)

            if first and second:
                compare_pokemon(first, second)
            else:
                print("\nOne or both Pokémon could not be found.\n")

        elif choice == "3":
            print("\nThanks for using the Pokédex!")
            break

        else:
            print("\nPlease choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main()