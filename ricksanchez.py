import time

def explorecave():
    print("Morty: This looks dangerous. Let's please get out!")
    while True:
        whatrickgonnado = input("go deeper or go back: ")
        if whatrickgonnado == "go deeper":
            print("You get lost even more, you and Morty panic and lose air and die. Hard luck!")
            break
        elif whatrickgonnado == "go back":
            print("You are now at starting point")
            return True
        else:
            print("Invalid choice. Choose 'go deeper' or 'go back'.")


def makefluidoutoftrash():
    print("You: Morty we are not gonna fucking die this way, Lets find the resources needed to make fluid")
    time.sleep(4)
    print("Search cave walls for limestone")
    time.sleep(4)
    print("Good we have limestone, now all we need left for our fluid is some sulfur")
    time.sleep(7)
    print("Search for sulfur near steaming rock formations")
    time.sleep(3)
    print("You: we got both morty Lets fucking go dude, Listen uh morty dont tell your mom this happened okay?")
    time.sleep(5)
    print("Morty: Uh ok d-d-dude im just happy we're out")
    time.sleep(3)
    print("GAME OVER YOU WIN")

def killmorty():
    areyousurebro = input("Narrator: You wanna kill your own fucking grandson? Are you fucking retarded?: ")
    if areyousurebro == "yes":
        print("You killed Morty out of frustration, 3 days later you die from being thirsty")
        return True
    elif areyousurebro == "no":
        return False

name = input("Let's play a game! What's your name friend?: ")
print(f"Hi {name}, Let's shut the fuck up and start this game!!!!!")
time.sleep(3)

print("You are Rick Sanchez!! Currently you're drunk and of course Morty is with you being a whiny bitch.")
time.sleep(5)
print("You are stuck in a cave and you're out of fluid for your portal gun.")
time.sleep(5)

print("Morty: Rick, I'm scared, I'm only 14, I can't fucking die yet, please get us out 😭")
time.sleep(5)
print("You: Shut the fuck up Morty if you wanna get out of this fucking cave")
time.sleep(5)

print("You have 3 choices")
time.sleep(2)

while True:
    print("What do you as Rick Sanchez want to do?: ")
    choices = input("1. explore the cave \n2. create fluid out of shit \n3. kill Morty \nYour choice: ").strip()

    if choices == "1":
        if explorecave():
            continue
        break
    elif choices == "2":
        makefluidoutoftrash()
        break
    elif choices == "3":
        if not killmorty():
            continue
        break
    else:
        print("Pick a valid choice!")
        time.sleep(2)
