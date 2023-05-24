#Regular Expressions Format:
#Acceptable Characters: 10()*|.
#Rules: 
#Can't put * at the 0th index
#Brackets should come in pairs and start bracket should appear before end bracket
#If empty brackets appear, they should be ignored [e.g. 101()001 => 101001]
#. is the empty symbol


def checkValid(RegEx):
    NumberofStartedBrackets = 0
    setOfValidChars = ["1","0","(",")","*","|"]
    for i,char in enumerate(RegEx):
        if char not in setOfValidChars:
            return False
        if char == "(":
            NumberofStartedBrackets += 1
        elif char == ")":
            if NumberofStartedBrackets > 0:
                NumberofStartedBrackets -= 1
            else:
                return False
        elif char == "*":
            if i == 0:
                return False
    if NumberofStartedBrackets > 0:
        return False
    else:
        return True

def checkString(RegEx):
    print("Current Regular Expression Statement: " + RegEx)
    InputString = input("Enter your string you would like to check [M to return to main menu]: ")
    if InputString == "M":
        return
    """Place Check Algorithm Here"""
    return True

def inputStatement():
    RegEx = input("Please input your regular expression: ")
    while checkValid(RegEx) == False:
        print("You entered an invalid input")
        RegEx = input("Please enter a valid expression: ") #Give user requirements/what they did wrong
    return RegEx