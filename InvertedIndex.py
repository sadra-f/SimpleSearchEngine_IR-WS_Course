from nltk import SpaceTokenizer
from IO import read_dir
from Document import Document
from Term import Term

class InvertedIndex:

    def __init__(self, path, do_build:bool=True):
        self.path = path
        self.docs = []
        self.dictionary = []
        self.posting_lists = []
        self.len = 0
        if do_build:
            self.build_inverted_index()
        
    

    def _load_dictionary(self, path):
        self.docs = read_dir(path)
        for doc in self.docs:
            tokenizer = SpaceTokenizer()
            for trm in tokenizer.tokenize(doc.text):
                if Term(trm) in self.dictionary:
                    self.dictionary[self.dictionary.index(Term(trm))].frq += 1
                else:
                    self.dictionary.append(Term(trm))
        if ' ' in self.dictionary:
            self.dictionary.remove(' ')
        self.dictionary = sorted(self.dictionary)
        self.len = len(self.dictionary)


    def _fill_posting_lists(self):
        for i in range(0, self.len): # loop over terms in dictionary
            self.posting_lists.append([])
            for j in range(0, len(self.docs)):# loop over docs
                tokenizer = SpaceTokenizer()
                if tokenizer.tokenize(self.docs[j].text).count(self.dictionary[i].text) > 0 :
                    self.posting_lists[i].append(j)
        return
                
    def build_inverted_index(self):
        self._load_dictionary(self.path)
        self._fill_posting_lists()

    def rebuild_inverted_index(self):
        del self.dictionary
        del self.posting_lists
        self.build_inverted_index()

    @property
    def inverted_index(self) -> dict:
        return dict(zip([trm.text for trm in self.dictionary], self.posting_lists))
