def search4letters(phrase: str, letters: str='aeiou') ->set:
    """Search for letters in a supplied phrase"""
    return set(letters).intersection(set(phrase))


    
