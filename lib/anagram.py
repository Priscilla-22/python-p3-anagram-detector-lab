# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        return [
            letter
            for letter in list
            if sorted(letter) == sorted(self.word) and letter != self.word
        ]


words = Anagram("listen")
print(words.match(["enlists", "google", "inlets", "banana"]))
