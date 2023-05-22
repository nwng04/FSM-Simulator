def checkValid(RegEx):
    return True

def main():
    RegEx = input("Please input your regular expression: ")
    while checkValid(RegEx) == False:
        print("You entered an invalid input")
        RegEx = input("Please enter a valid expression: ") #Give user requirements/what they did wrong