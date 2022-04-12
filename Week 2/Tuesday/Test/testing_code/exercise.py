def reverse_list(arr):
    arr.reverse()
    return arr

def is_vowel(letter):
    vowels = ["a", "e", "o", "i", "u"]

    for i in vowels:
        if letter == i:
            return True

def number_of_vowels(sentence):
    vowels = ["a", "e", "o", "i", "u"]

    res = []
    res[:] = sentence.lower()

    count = 0

    for i in res:
        for k in vowels:
            if i == k:
                count += 1

    return count

def length_of_words(sentence):
    splitting = sentence.split(' ')
    res = []

    for i in splitting:
        count = len(i)
        res.append(count)

    return res

