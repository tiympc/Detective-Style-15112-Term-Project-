import random
import string
import enchant
import numpy
import html2text

from questionsGen import *


# As the wave / currDifficulty increases, then the number of bad strings must decrease
# since the probability of accidentally dragging a good string increases. Therefore,
# I decreased the probability of a style error according to the currDifficulty so that the
# game got harder towards the end. In order to decrease the probalility, I read
# a research paper on Dynamic Game Difficulty Balancing (DGDB) and created
# an AI that adjusted the difficulty of the game (in real time) based on the
# user's skill currDifficulty, ensuring an equilibrium between the difficulty of the game
# and the enjoyement while playing it.

##################################

def randomVariable(currDifficulty):
    # FOR THE VARIABLE NAMES

    rand = ""
    length = random.randint(1, 7)
    english = enchant.Dict("en_US")
    if length == 1:
        return random.choice(string.ascii_lowercase)
    else:
        for char in range(length):
            rand = rand + random.choice(string.ascii_letters)
        if english.suggest(rand) == []:
            return randomVariable(currDifficulty)
        result = random.choice(english.suggest(rand))
        punctSet = {"'", "!", '""', "#", "$", "%", "&", "(", ")", "*", "+", ",",
        "-", ".", ":", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^",
        "_", "`", "{", "|", "}", "~"}
        for c in result:
            if c in punctSet:
                return randomVariable(currDifficulty)
        if " " in result:
            return randomVariable(currDifficulty)
        elif result[0] in string.ascii_uppercase:
            restString = result[1:]
            firstLetter = result[0].lower()
            result = firstLetter + restString
        elif english.check(result) != True:
            return randomVariable(currDifficulty)
        elif result in {"if", "elif", "else", "for", "return", "equal", "def",
        "functCall", "mod", "operand"}:
            return randomVariable(currDifficulty)
    count = 0
    if len(result) > 3:
        for c in range(len(result) - 1):
            if result[c] in string.ascii_uppercase and \
            result[c+1] in string.ascii_uppercase:
                count += 1
        if count >= 2:
            return randomVariable(currDifficulty)
    else:
        for c in result:
            if c in string.ascii_lowercase:
                count += 1
        if count == 1:
            return randomVariable(currDifficulty)
    normalOrSnake = numpy.random.choice(["normal", "snake"], p=[currDifficulty,
    1 - currDifficulty])
    if normalOrSnake == "normal":
        return randomVariable(currDifficulty)
    else:
        first = result
        result = first + "_" + randomVariableHelper()
    return result

def randomVariableHelper():
    rand = ""
    length = random.randint(1, 7)
    english = enchant.Dict("en_US")
    if length == 1:
        return random.choice(string.ascii_lowercase)
    else:
        for char in range(length):
            rand = rand + random.choice(string.ascii_letters)
        if english.suggest(rand) == []:
            return randomVariableHelper()
        result = random.choice(english.suggest(rand))
        for c in string.punctuation:
            if c in result:
                return randomVariableHelper()
        if " " in result:
            return randomVariableHelper()
        elif result[0] in string.ascii_uppercase:
            restString = result[1:]
            firstLetter = result[0].lower()
            result = firstLetter + restString
        elif english.check(result) != True:
            return randomVariableHelper()
        elif result in {"if", "elif", "else", "for", "return", "equal", "def",
        "functCall", "mod", "operand"}:
            return randomVariableHelper()
        count = 0
        for c in range(len(result) - 1):
            if count == 2:
                return randomVariableHelper()
            if result[c] in string.ascii_uppercase and \
            result[c+1] in string.ascii_uppercase:
                count += 1
    return result

def builtFunctionGen(currDifficulty):
    result = ""
    builtTypes = ["num", "typevariable", "string", "oflist"]
    chosen = random.choice(builtTypes)
    if chosen == "num":
        option = random.choice(["number", "variable"])
        if option == "number":
            result = "abs(" + str(random.randint(-1000, 0)) + ")"
        else:
            result = "abs(" + randomVariable(currDifficulty) + ")"
    elif chosen == "typevariable":
        option = random.choice(["dict(", "tuple(", "set("])
        result = option + randomVariable(currDifficulty) + ")"
    elif chosen == "string":
        option = "input"
        if option == "input":
            result = randomVariable(currDifficulty) + " = " + option + '("' + questionGenerator() + '")'
    elif chosen == "oflist":
        options = random.choice(["max(", "min(", "len(", "sorted(", "sum("])
        if options == "max(":
            result = options + randomVariable(currDifficulty) + "List)"
        elif options == "min(":
            result = options + randomVariable(currDifficulty) + "List)"
        elif options == "len(":
            result = options + randomVariable(currDifficulty) + "List)"
        elif options == "sorted(":
            result = options + randomVariable(currDifficulty) + "List)"
        else:
            result = options + randomVariable(currDifficulty) + "List)"
    return result

def generatesString(currDifficulty):

    # FOR THE TYPE OF CODE: now you have to decide if the code will be an
    # if statement, elif, else, for, return, variable setting, def,
    # function call such as pygame.init(), or module call once this is decided you have to
    # additionally decide what will be written after that
    good = True
    type = random.choice(["if", "elif", "else", "for", "return", "equal", "def", "functCall", "mod", "operand", "built", "print", "alone"])
    result = ""
    individualProb = currDifficulty / 6
    numPossible = numpy.random.choice(["-1", "0", "0.5", "1", "2", "10", str(random.randint(1, 1000))],
    p=[individualProb, individualProb, individualProb, individualProb, individualProb, individualProb, 1 - 6 * individualProb])
    if type == "if":
        typeOperand = random.choice([" == ", " >= ", " > ", " <= ", " < "])
        result = "if " + randomVariable(currDifficulty) + typeOperand + numPossible + ":"
    elif type == "elif":
        typeOperand = random.choice([" == ", " >= ", " > ", " <= ", " < "])
        result = "elif " + randomVariable(currDifficulty) + typeOperand + numPossible + ":"
    elif type == "else":
        singleOrMult = numpy.random.choice(["single", "mult"], p=[0.2, 0.8])
        if singleOrMult == "single":
            result = "else:"
        elif singleOrMult == "mult":
            endOption = random.choice(["returnSomething", "equalSomething", "callSomething"])
            if endOption == "returnSomething":
                result = "else: return " + numpy.random.choice([randomVariable(currDifficulty), numPossible], p=[0.75, 0.25])
            elif endOption == "equalSomething":
                randomVariable1 = randomVariable(currDifficulty)
                randomVariable2 = randomVariable(currDifficulty)
                result = "else: " + randomVariable1 + " = " + randomVariable2
            elif endOption == "callSomething":
                result = "else: " + randomVariable(currDifficulty) + "()"
    elif type == "for":
        var = numpy.random.choice(["char", "line", random.choice(string.ascii_lowercase)], p=[0.2, 0.2, 0.6])
        result = "for " + var + " in range(len(" + randomVariable(currDifficulty) + ":"
    elif type == "return":
        returnTypes = numpy.random.choice(["returnVariable", "returnNumber"],
        p=[0.75, 0.25])
        if returnTypes == "returnVariable":
            result = "return " + randomVariable(currDifficulty)
        else:
            result = "return " + numpy.random.choice(["-1", "0", "0.5", "1", "2", "10", str(random.randint(1,1000))],
            p=[.125, .125, .125, .125, .125, .125, .25])
    elif type == "equal":
        equalTypes = numpy.random.choice([randomVariable(currDifficulty), numPossible], p=[0.75, 0.25])
        result = randomVariable(currDifficulty) + " = " + equalTypes
    elif type == "def":
        result = "def " + randomVariable(currDifficulty) + "():"
    elif type == "functCall":
        result = randomVariable(currDifficulty) + "()"
    elif type == "mod":
        stringMethods = ["capitalize()", "casefold()", "count()", "endswith()", "find()",
        "index()", "isalnum()", "isalpha()", "isdecimal()", "isdigit()", "islower()",
        "isnumeric()", "isspace()", "isupper()", "join()", "lower()", "replace()", "split()",
        "splitlines()", "startswith()", "upper()"]
        listMethods = ["append()", "clear()", "copy()", "count()", "extend()",
        "index()", "insert()", "pop()", "remove()", "reverse()", "sort()"]
        setMethods = ["add()", "clear()", "copy()", "difference()", "discard()",
        "intersection()", "issubset()", "issuperset()", "pop()", "remove()", "union()",
        "update()"]
        dictMethods = ["clear()", "copy()", "fromkeys()", "get()", "items()",
        "keys()", "pop()", "setdefault()", "update()", "values()"]
        tupMethods = ["count()", "index()"]
        choice = [stringMethods, listMethods, setMethods, dictMethods, tupMethods]
        randomtxtChoice = random.choice(choice)
        randomFinalChoice = random.choice(randomtxtChoice)
        result = randomVariable(currDifficulty) + "." + randomFinalChoice
    elif type == "operand":
        simpOrNot = random.choice(["simple", "complex"])
        numOrNot = random.choice(["number", "variable"])
        goodOrBad = numpy.random.choice(["good", "bad"], p=[currDifficulty,
        1 - currDifficulty])
        if goodOrBad == "bad":
            good = False
            if simpOrNot == "simple":
                badFormat = random.choice([" =", "= " ])
                if numOrNot == "number":
                    result = randomVariable(currDifficulty) + badFormat + numPossible
                else:
                    result = randomVariable(currDifficulty) + badFormat + randomVariable(currDifficulty)
            else:
                badFormat = random.choice([" +=", "+= ", " -=", "-= ", "*= ", " *=",
                "/= ", " /=", " %", "% ", "// ", " //", " **", "** "])
                if numOrNot == "number":
                    result = randomVariable(currDifficulty) + badFormat + numPossible
                else:
                    result = randomVariable(currDifficulty) + badFormat + randomVariable(currDifficulty)
        else:
            if simpOrNot == "simple":
                if numOrNot == "number":
                    result = randomVariable(currDifficulty) + " = " + numPossible
            else:
                badFormat = random.choice([" += ", " -= ", " *= ", " /= ", " % ", " // ", " ** "])
                if numOrNot == "number":
                    result = randomVariable(currDifficulty) + badFormat + numPossible
                else:
                    result = randomVariable(currDifficulty) + badFormat + randomVariable(currDifficulty)
    elif type == "print":
        option = random.choice(["number", "variable", "question"])
        if option == "number":
            result = type + "(" + str(random.randint(1,1000)) + ")"
        elif option == "variable":
            result = type + "(" + randomVariable(currDifficulty) + ")"
        else:
            result = type + '("' + questionGenerator() + '")'
    elif type == "built":
        result = builtFunctionGen(currDifficulty)
    elif type == "alone":
        option = random.choice(["dict(", "tuple(", "hash(", "set("])
        if result == "hash(":
            result = randomVariable(currDifficulty) + " = " + option + str(random.randint(1,1000)) + ")"
        else:
            result = randomVariable(currDifficulty) + " = " + option + ")"
    if "_" in result:
        good = False
    for c in result:
        if c in string.digits and c not in ["-1", "0", "0.5", "1", "2", "10"]:
            good = False
    if result == "":
        return generatesString(currDifficulty)
    return (result, good)
