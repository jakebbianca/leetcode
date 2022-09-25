"""
Implement Trie
Grind 75 #34
LC #208 Medium

This solution works with individual chars
"""


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.word=False
        self.children={}
    
    class Trie:
    
        def __init__(self):
            self.root = TrieNode()
    
        # @param {string} word
        # @return {void}
        # Inserts a word into the trie.
        def insert(self, word):
            node=self.root
            for i in word:
                if i not in node.children:
                    node.children[i]=TrieNode()
                node=node.children[i]
            node.word=True
    
        # @param {string} word
        # @return {boolean}
        # Returns if the word is in the trie.
        def search(self, word):
            node=self.root
            for i in word:
                if i not in node.children:
                    return False
                node=node.children[i]
            return node.word
    
        # @param {string} prefix
        # @return {boolean}
        # Returns if there is any word in the trie
        # that starts with the given prefix.
        def startsWith(self, prefix):
            node=self.root
            for i in prefix:
                if i not in node.children:
                    return False
                node=node.children[i]
            return True
            
    
    # Your Trie object will be instantiated and called as such:
    # trie = Trie()
    # trie.insert("somestring")
    # trie.search("key")

"""
class Trie:

    # object that holds word (value) and pointer to potential next trie
    def __init__(self, string=None, next=None):
        self.string = string
        self.next = next

    # check strings at each trie
    # if already in trie structure, return without further action
    # if word is not found, add new trie and fill string value
    def insert(self, word: str) -> None:
        while True:       
            if not self.string:
                self.string = word
                return
            else:
                if self.next:
                    self = self.next
                else:
                    self.next = Trie(word)
                    return
        
    def search(self, word: str) -> bool:
        while True:
            if not self.string or word != self.string:
                if self.next:
                    self = self.next
                else:
                    return False
            else:
                return True
        
    def startsWith(self, prefix: str) -> bool:
           while True:
                if not self.string or prefix != self.string[0:len(prefix)]:
                    if self.next:
                        self = self.next
                    else:
                        return False
                else:
                    return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
"""