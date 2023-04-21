from  InvertedIndex import InvertedIndex as IX
from SimpleSearch import SimpleSearch as Searcher
import os

def main():
    indexer = IX(os.getcwd())
    print(indexer.inverted_index)
    srch = Searcher(indexer.inverted_index, set([i for i in range(0,len(indexer.docs))]))
    print(srch.query("sadra&!helps"))




if __name__ == '__main__':
    main()


