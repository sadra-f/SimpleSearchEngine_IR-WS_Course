from nltk import SpaceTokenizer
from IO import read_dir
from Document import Document
from Term import Term

class InvertedIndex:

    def __init__(self, path):
        self.path = path
        self.docs = list[Document]
        self.dictionary = set[Term]
        self.posting_lists = list[int]
        self.len = 0
    

    def load_dictionary(self, path):
        self.docs = read_dir(path)
        for doc in self.docs:
            for trm in SpaceTokenizer.tokenize(doc):
                if Term(trm) in self.dictionary:
                    temp = self.dictionary.pop(Term(trm))
                    self.dictionary.add(Term(trm, temp.frq + 1))
                else:
                    self.dictionary.add(Term(trm))
        self.dictionary.remove(' ')
        self.len = len(self.dictionary)


    def fill_posting_lists(self):
        for i in range(0, self.len):
            
            for doc in self.docs:
                pass #TODO
                
