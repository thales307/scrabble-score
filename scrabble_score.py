def score(word):

    VALUES = {
        **dict.fromkeys(list('AEIOULNRST'), 1),
        **dict.fromkeys(list('DG'), 2),
        **dict.fromkeys(list('BCMP'), 3),
        **dict.fromkeys(list('FHVWY'), 4),
        **dict.fromkeys(list('K'), 5),
        **dict.fromkeys(list('JX'), 8),
        **dict.fromkeys(list('QZ'), 10),
    }

    return sum((VALUES[letter] for letter in word.upper()))