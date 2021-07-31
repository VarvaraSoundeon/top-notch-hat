import itertools as iterator

#счетчик игроков
PlayerCount = 0
#число слов на игрока
WordsPerPlayer = 1

class Player(object):

    def __init__(self, id, words, stats):
        self.id = id
        self.words = words
        self.stats = stats
    
    def __repr__(self):
        return "Player id = " + str(self.id) + "; words = " + str(self.words) + "; stats = " + str(self.stats)


def inputWords(count):
    WordsList = []
    print("Enter "+str(count)+" Words, please:")
    for i in range(count):
        Word = input("\n"+str(i+1)+": ")
        WordsList.append([Word,0])
    return WordsList

def createPlayer(id):
    playerWords = inputWords(WordsPerPlayer)
    player = Player(id, playerWords, [0,0])
    return player

def matchMaking(ids):
    permutations = list(iterator.permutations(ids,2))
    matches, j = [], 0
    maxPairs, step = len(permutations), len(ids)
    for i in range(maxPairs):
        if i !=0 and i%(step-1) == 0:
            j = j + 1
        matches.append(permutations[j + (i%(step-1))*step])
    return matches

if __name__ == "__main__":
    PlayerList = []
    while True:
        answer = input("Create a player? Y/N: ")
        if answer == "Y":
            PlayerList.append(createPlayer(PlayerCount))
            PlayerCount = max(PlayerList, key=lambda x: x.id).id + 1
        else:
            ids = list(x.id for x in PlayerList)
            order = matchMaking(ids)
            quit()