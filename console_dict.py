words = {}

def add_word(word, meaning):
    
    words[word] = meaning

    return f"Added {word}"


def update_meaning(word, meaning):

    if word in words:
        words[word] = meaning
        return f"{word} updated"
    else:
        return

def find_word(word):
    
    if word in words:
        return f'{word}:{words[word]}'
    else:
        return 'No such word'
    
