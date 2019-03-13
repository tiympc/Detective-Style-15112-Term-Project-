import random
# used to create random input strings of code. Used html source to get quetsions
# from site.
# takes questions from https://www.conversationstarters.com/101.htm
# i did not come up with the questions myself.
# reads the html file, finds questions
def questionGenerator():
    html = open("questions.html").read()
    newLineSet = set()
    for line in html.splitlines():
        if "What" in line or "Do" in line or "Where" in line or "If" in line or \
        "Are" in line or "What's" in line or "Were" in line or "Have" in line or \
        "Who" in line or "Would" in line or "How" in line:
            newLine = line[4:len(line) - 5:]
            newLineSet.add(newLine)
    for element in newLineSet.copy():
        if (element.startswith("What") or element.startswith("Do") or \
        element.startswith("Where") or element.startswith("If") or \
        element.startswith("Are") or element.startswith("What's") or \
        element.startswith("Were") or element.startswith("Have") or \
        element.startswith("Who") or element.startswith("Would") or \
        element.startswith("How")) and len(element) <= 30:
            continue
        else:
            newLineSet.remove(element)
    QuestionList = list(newLineSet)
    return random.choice(QuestionList)
