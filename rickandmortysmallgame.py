import random

def start_game():
    print("Welcome to the Rick and Morty Multiverse Adventure")
    print("You're Rick Sanchez, and of course, Morty is with you, as usual")
    print("Your portal gun broke down, and now you're stuck in some random dimension")
    print("Fix your portal gun and get out of here")
    print("\nTime to get schwifty\n")
    choose_action()

def choose_action():
    while True:
        print("What’s the plan")
        print("1. Search for parts to fix the portal gun")
        print("2. Talk to Morty")
        print("3. Fight some aliens")
        print("4. Jump through a random portal (This could go horribly wrong)")
        
        choice = input("Choose an action (1/2/3/4): ")
        if choice == "1":
            search_parts()
        elif choice == "2":
            talk_to_morty()
        elif choice == "3":
            fight_aliens()
        elif choice == "4":
            use_random_portal()
        else:
            print("Come on, Morty, pick a valid option\n")

def search_parts():
    print("\nYou start rummaging through the area for anything useful")
    outcome = random.choice(["found", "nothing", "ambushed"])
    if outcome == "found":
        print("You found a piece for the portal gun That’s a win")
    elif outcome == "nothing":
        print("Nada Just a bunch of weird stuff")
    else:
        print("Oh great, you’ve been ambushed by aliens Time to fight\n")
        fight_aliens()

def talk_to_morty():
    responses = [
        "Morty: Rick, are you sure this is a good idea",
        "Morty: I’m really not feeling good about this, Rick",
        "Morty: Can we PLEASE go home now",
    ]
    print("\n" + random.choice(responses) + "\n")

def fight_aliens():
    print("\nAliens pop out of nowhere and start attacking")
    success = random.choice([True, False])
    if success:
        print("You fought them off Alien loot is yours now")
    else:
        print("They were too much for you maybe next time, Rick\n")

def use_random_portal():
    print("\nYou aim the portal gun and fire off a random portal")
    outcome = random.choice(["new_dimension", "same_dimension", "danger"])
    if outcome == "new_dimension":
        print("You made it to another dimension Freedom")
    elif outcome == "same_dimension":
        print("Whoops, you’re back in the same place this is just getting depressing")
    else:
        print("You ended up in a dimension full of monsters Time to RUN\n")

if __name__ == "__main__":
    start_game()
