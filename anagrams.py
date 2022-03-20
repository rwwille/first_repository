def anagrams(word, words):
    first = []
    anagrams = []
    [first.append(_) for _ in word]
    first.sort()

    for x in words:
        second = []
        [second.append(_) for _ in x]
        second.sort()
        if first == second:
            anagrams.append(x)
    return anagrams


print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))


def anagrams(word, words):
    return [item for item in words if sorted(item) == sorted(word)]
