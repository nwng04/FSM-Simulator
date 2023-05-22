import RegExAnalyser as Rea


def mainmenu():
    print("Actions:\n[1] Enter Regular Expression\n[2] Check String Validity\n[3] Quit")
    entered = input()
    while entered not in ["1","2","3"]:
        print("Please enter a valid choice [1,2,3]")
        entered = input()
    return entered


def main():
    print("Welcome to the Finite State Machine Simulator!")
    while True:
        option = mainmenu()
        if option == "1":
            Rea.main()
        elif option == "3":
            quit()
