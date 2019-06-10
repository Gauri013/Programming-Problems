def anagram(word_one , word_two):
    return "Anagram" if (sorted(word_one) == sorted(word_two)) else "Not"

word_one = input()
word_two = input()

print(anagram(word_one, word_two))

