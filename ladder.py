#!/usr/bin/env python
"""
    ladder.py - find shortest path between two words in a word ladder
"""
import sys
import heapq

DICTIONARY = "dict.txt"


class WordGraph(object):
    def __init__(self, words, size):
        self.word_patterns = {}
        self.size = size

        for word in words:
            if len(word) != size:
                continue
            for p in self.patterns(word):
                if p not in self.word_patterns:
                    self.word_patterns[p] = []
                self.word_patterns[p].append(word)

    def patterns(self, word):
        p = []
        for i in range(len(word)):
            letters = list(word)
            letters[i] = '?'
            p.append(''.join(letters))
        return p

    def unvisited(self, word, visited):
        words = []
        for p in self.patterns(word):
            candidates = self.word_patterns.get(p)
            if candidates is None:
                continue
            for cand in candidates:
                if cand not in visited:
                    words.append(cand)
        return words

    @classmethod
    def hamming(cls, word1, word2):
        c = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                c += 1
        return c

    def min_path(self, word1, word2):
        visited = {}
        frontier = []
        heapq.heappush(frontier, (0, word1, [word1]))
        while len(frontier) > 0:
            distance, word, path = heapq.heappop(frontier)
            if word == word2:
                return path
            for adjacent in self.unvisited(word, visited):
                cost = distance + self.hamming(adjacent, word2)
                visited[adjacent] = cost
                heapq.heappush(frontier, (cost, adjacent, path + [adjacent]))
        return None


def min_ladder(words, word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    if word2 not in words:
        print "Warning: %s is not in dictionary." % word2
        words.append(word2)

    graph = WordGraph(words, len(word1))
    return graph.min_path(word1, word2)


def main():
    if len(sys.argv) != 3:
        print "Usage: %s word1 word2" % sys.argv[0]
        exit(1)
    if len(sys.argv[1]) != len(sys.argv[2]):
        print "Words must be the same length."
        exit(1)
    words = [word.strip() for word in open(DICTIONARY).readlines()]
    ladder = min_ladder(words, sys.argv[1], sys.argv[2])
    if ladder is None:
        print "No known ladder."
        exit(1)
    for word in ladder:
        print word.upper()


if __name__ == '__main__':
    main()
