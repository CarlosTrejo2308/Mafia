import getpass
from player import Player

def main():
    def addPlayer():
        nameT = input("Name: ")
        print("Password: ")
        p = getpass.getpass()
        temp = Player(nameT, p)
        players.append(temp)

    from Calvin import Calvin
    narrator = Calvin()
    players = []
    addPlayer()

    for p in players:
        print(p.name, p.pwd, p.live)

if __name__ == '__main__':
    main()
