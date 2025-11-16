def search4vowels(word: str) -> set:
    """ Return any vowels in the supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
        

