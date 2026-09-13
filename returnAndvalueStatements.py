#tiny bit modification of the return values and return statements
# I was trying to have interaction using the provided code in the example
# I know there was better variation to do this that maybe I will uncover it soon
# as I move through the materials
# this will be much more better if this is a sequence of answers
#this code works by choosing random numbers with corresponding question.

import random #showing highlights but not necessarily wrong

def getAnswer(answerNumber):
    if answerNumber == 1:
            return input('Who are you?:')
    elif answerNumber == 2:
        return input('Are you from here?:')
    elif answerNumber == 3:
        return input('So, where do you live?:')
    elif answerNumber == 4:
        return input('Who is your parents?:')
    elif answerNumber == 5:
        return input('Good to know!')


print(getAnswer(random.randint(1, 5)))
