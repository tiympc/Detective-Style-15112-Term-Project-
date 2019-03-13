# The Dyanmic Game Difficulty Balancing AI was created with the inspiration of
# Fuzzy Cognitive Maps (FCM). I created a map that showed the components of the game
# and what each component's relationship with other components were.
# Below is a link to an image of an example FCM (it's not spam, I promise)
# https://i.ytimg.com/vi/HNEfGppZptU/maxresdefault.jpg
# I concluded that the game difficulty could be assesed by taking into account
# the wave level, the number of graceDays the user has received over the game,
# the time the user takes to complete a level, and the number of boosts
# available for the user to toggle.
# With this in mind, I mapped each individual variable to other variables
# and assigned a value, -1 (for a strong inverse relationship),
# +1 (for a strong direct relationship), -0.5 (for an intermediate inverse
# relationship), and +0.5 (for an intermediate direct relationship)

# The function below takes in all of these variables and with the help of a simple
# algorithm that I wrote, returns the difficulty of the game for that level,
# used to determine the probability used in randomStyle.py

# The resulting difficulty value ranges from 0.1 to 0.9 and starts at 0.1
def dynamicDifficulty(numTime, numLevel, numBoosts, numGraceDays, currDifficulty):
    if numLevel == 1:
        return 0.1
    else:
        # positive means higher value leads to game being easy for user so make
        # make it harder
        numTimeFactor = -3
        numLevelFactor = 5
        numBoostsFactor = 10
        numGraceDaysFactor = 5
        result = numTime * numTimeFactor + numLevel * numLevelFactor + numBoosts \
        * numBoostsFactor + numGraceDays * numGraceDaysFactor
        result = result / 1000
        currDifficulty += result
        return currDifficulty
