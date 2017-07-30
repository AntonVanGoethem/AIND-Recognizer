import warnings
from asl_data import SinglesData


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    prob_dict = {}
    best_logL = float("-inf")
    # TODO implement the recognizer
    # return probabilities, guesses
    test_sequences = list(test_set.get_all_Xlengths().values())
    for test_X, test_Xlength in test_sequences:
        for word, model in models.items():
            try:   
                logL = model.score(test_X, test_Xlength)
            except:
                logL = float("-inf")
            prob_dict[word] = logL
        probabilities.append(prob_dict)
        for probability in probabilities:     
            for word, logL in probability.items():
                if logL > best_logL:
                    best_logL = logL
                    best_guess = word
        guesses.append(best_guess)
    return probabilities, guesses