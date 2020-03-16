import getpass
from player import Player

def printMenu():
    print("1. Instructions")
    print("2. Settings")
    print("3. Players")
    print("4. Play")
    print("5. Credits")



def main():
    from Calvin import Calvin
    narrator = Calvin()
    players = []
    
    def addPlayer():
        nameT = input("Name: ")
        print("Password: ")
        p = getpass.getpass()
        temp = Player(nameT, p)
        players.append(temp)

    addPlayer()

    narrator.say("Hi, this is a test. " + players[0].name)

    for p in players:
        print(p.name, p.pwd, p.live)

if __name__ == '__main__':
    main()
