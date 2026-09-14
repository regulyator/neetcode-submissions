def get_longer_word(word1: str, word2: str) -> str:
    w1len = len(word1)
    w2len = len(word2)
    if w2len > w1len:
        return word2
    return word1



# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
