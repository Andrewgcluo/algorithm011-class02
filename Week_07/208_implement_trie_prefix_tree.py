class Trie:
    def __init__(self):
        self.d = {}
        
    def insert(self, word: str) -> None:
        t = self.d
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['end'] = True

    def search(self, word: str) -> bool:
        t = self.d
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return 'end' in t

    def startsWith(self, prefix: str) -> bool:
        t = self.d
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)