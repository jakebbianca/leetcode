

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        """
        More verbose version of the counter solution
        """
        
        # build a dict with letters in the mag as keys and counts of each letter as values
        # if any letter for the note does not appear in the mag, return False
        # if any letter in the note appears fewer times in the mag, return False
        # otherwise, return True
        abcdict = {}
        
        for i in magazine:
            if i not in abcdict:
                abcdict[i] = 1
            else:
                abcdict[i] += 1
            
        for j in ransomNote:
            if j not in abcdict:
                return False
            else:
                abcdict[j] -= 1
        
        for val in abcdict.values():            
            if val < 0:
                return False
            
        return True

        """
        Simple solution using counters
        abcnote = Counter(ransomNote)
        abcmag = Counter(magazine)
        
        for key in abcnote:
            if abcnote[key] > abcmag[key]: return False
            
        return True
        """