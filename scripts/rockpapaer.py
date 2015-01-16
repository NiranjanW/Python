
def startGame() :
    choices = ['paper', 'rock', 'scissors']
    player = getUserChoice(choices)

def getUserChoice(alist):

    while True:
        user_input = raw_input('paper , rock or scissors ?' ).lower
        for i in range(len(alist)):
            if user_input in alist[i]:
                return user_input
            if user_input ==None:
                print 'please enter rock papaer or scissors'