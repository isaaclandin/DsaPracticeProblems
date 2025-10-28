class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # take a word and put chars in compare set
            # compare rest of words in set to (compare set)
            # if they are equal we put them in dict with key[set(), val = [word1, word2]]
                # remove word from list to improve time complexity
            # return [] for key, val in output: append val
            # O(n^2)
        
        output = defaultdict(list)
        
        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord("a")] += 1
            output[tuple(count)].append(s)
        
        return list(output.values())
