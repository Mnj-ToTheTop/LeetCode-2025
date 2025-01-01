# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()      
        x = len(searchWord)
        # Spliting the sentence into words.
        # Getting the length of the searchword.
        for y in range(len(words)):
            # if length of word < length of search word, it can't have the searchword as a prefix.
            # checking if the word has the searchWord.
            if len(words[y])>=x and words[y][:x] == searchWord:
                return y + 1
        return -1
