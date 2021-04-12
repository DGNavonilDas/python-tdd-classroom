class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        vowels = "aeiouAEIOU"
        return character in vowels

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        items = sentence.split(' ')
        ans = ''
        for word in items:
            if len(word) > len(ans):
                ans = word

        return ans

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        items = text.split(' ')
        ans = [len(x) for x in items]
        return ans