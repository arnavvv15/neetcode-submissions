class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.end = True

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.end

            if word[i] == ".":
                for c in node.children:
                    if dfs(node.children[c], i + 1):
                        return True
                return False

            if word[i] not in node.children:
                return False

            return dfs(node.children[word[i]], i + 1)

        return dfs(self.root, 0)
        
