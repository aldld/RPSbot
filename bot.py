# Main RPS Bot class
# Contains methods for determining best move, &c.

from random import randint

# Codes for individual throws
ROCK     = 0
PAPER    = 1
SCISSORS = 2

class Bot():
    """ Throw history is stored as a list with the following format:
        [{'human': 0, 'bot': 1}, {'human': 2, 'bot': 0} ... ]
    """
    throwHistory = []

    def getRandomThrow():
        """ Return a random throw from the bot. """
        return randint(ROCK, SCISSORS)

    @staticmethod
    def getThrow():
        """ Predict next throw based on a history matching algorithm
            Should run in something like O(n^2), where n is the number
            of past throws.
        """

        previousThrow = Bot.throwHistory[-1]
        
        # List of candidate throws
        # {'index': index in throwHistory, 'rating': throw rating}
        candidateThrows = []

        # Search for throws in history matching previous throw.
        throwIndex = 0
        while throwIndex < len(Bot.throwHistory) - 1:
            throwSet = Bot.throwHistory[throwIndex]
            throwRating = 0

            # TODO: revise throw ratings
            if throwSet['human'] == previousThrow['human']:
                throwRating += 1
            if throwSet['bot'] == previousThrow['bot']:
                throwRating += 1

            if throwRating > 0:
                candidateThrows.append({'index': throwIndex, 'rating': throwRating})

            throwIndex += 1

        # If no candidates found, pick a random throw.
        if not candidateThrows: return Bot.getRandomThrow()

        # Step back through history to look for patterns.
        # TODO: Increment throw rating for each match like above (currently lines 40-43)
        candidate = 0
        while candidate < len(candidateThrows):
            historyPos = candidateThrows[candidate]['index']
            offset = 1
            while historyPos >= 0:
                compare = Bot.throwHistory[-offset]
                compareTo = Bot.throwHistory[historyPos]

                if compare['human'] == compareTo['human']:
                    candidateThrows[candidate]['rating'] += 1
                if compare['bot'] == compareTo['bot']:
                    candidateThrows[candidate]['rating'] += 1

                historyPos -= 1
                offset += 1

            candidate += 1

        # Return throw that beats human throw after the candidate with the highest rating.
        topCandidate = candidateThrows[0]
        for candidate in candidateThrows:
            if candidate['rating'] >= topCandidate['rating']:
                topCandidate = candidate

        predictedThrow = Bot.throwHistory[topCandidate['index']]['human']
        if predictedThrow == ROCK: return PAPER
        if predictedThrow == PAPER: return SCISSORS
        if predictedThrow == SCISSORS: return ROCK

