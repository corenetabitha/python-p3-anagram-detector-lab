# your code goes here!
class Anagram:
    def __init__(self, word):
        """Initialize with a word to match anagrams against"""
        self.word = word.lower()
        self.sorted_word = sorted(self.word)  
    
    def match(self, possible_anagrams):
        """Return matching anagrams from the list"""
        return [anagram for anagram in possible_anagrams 
                if self._is_anagram(anagram)]
    
    def _is_anagram(self, candidate):
        """Helper method to check if candidate is an anagram"""
        candidate_lower = candidate.lower()
        return (candidate_lower != self.word and 
                sorted(candidate_lower) == self.sorted_word)


# Example usage that exactly matches your requirement:
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))  # => ['inlets']