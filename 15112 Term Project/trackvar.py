# from 112 lecture notes
# tracks some variables that change in a file
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)


def keepTrackOfMe1(track):
    writeFile("nameVar.txt", track)

def keepTrackOfMe2(track):
    result = track
    writeFile("totgrace.txt", str(result))

def whatAmI2():
    file = readFile("totgrace.txt")
    graceDayList = file
    return int(graceDayList)

def whatAmI1():
    file = readFile("nameVar.txt")
    return file
