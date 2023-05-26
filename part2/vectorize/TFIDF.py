from numpy import ndarray
import numpy as np
from numpy import dot
import re
from statics.stopwords import STOPWORDS
from math import log10

class TFIDF:
     
    def __init__(self, inp_strings, query_strings):
        self.inp_strings = TFIDF.preprocess(inp_strings)
        self.query_strings = TFIDF.preprocess(query_strings)
        self.all_strings = [itm for itm in inp_strings]
        for i in range(len(self.query_strings)):
            self.all_strings.append(self.query_strings[i])

        self.inp_terms = TFIDF.extract_terms(self.inp_strings)
        self.query_terms = TFIDF.extract_terms(self.query_strings)
        self.all_terms = TFIDF.extract_terms(self.all_strings)

        self.tf = TFIDF.TF(self.all_strings, self.all_terms).tf
        self.idf = TFIDF.IDF(self.all_strings, self.all_terms).idf
        self.tfidf = ndarray((len(self.all_terms),len(self.all_strings)))

        self.calc_tfidf()
        return
        
    def preprocess(inp_list):
        for i in range(len(inp_list)):
            inp_list[i] = re.subn("([.]$)|( [.] )", " ", inp_list[i])[0]
            inp_list[i] = re.subn("[(]|[)]|[/]|[']|[*]|[+]|[],]|[-]|[--]|[?]", "", inp_list[i])[0]
        return inp_list
               
    def extract_terms(string_list:list[str], remove_stopwords=True):
        tmp = []
        result = []
        for string in string_list:
            for word in string.split(" "):
                if word.strip() not in tmp:
                    tmp.append(word.strip())
        if remove_stopwords:
            for sw in STOPWORDS:
                try:
                    tmp.remove(sw)
                except ValueError:
                    continue
            for i in range(len(tmp)):
                if re.search("\d", tmp[i]) is None:
                    result.append(tmp[i])

        result = sorted(result)
        return result

    def calc_tfidf(self):
        for i in range(len(self.tf)):
            for j in range(len(self.tf[i])):
                self.tfidf[i][j] = self.tf[i][j] * self.idf[i]

    def vector_length(vector:ndarray):
        return np.sqrt(vector.dot(vector))

    def cosine_similarity(vector1:ndarray, vector2:ndarray):
        return dot(vector1, vector2) / ( TFIDF.vector_length(vector1) * TFIDF.vector_length(vector2) )

    def calc_cosine_similarity(self):
        result = []
        for i in range(len(self.query_strings)):
            result.append([])
            for j in range(len(self.inp_strings)):
                result[i].append(TFIDF.cosine_similarity(self.tfidf.take(i+len(self.inp_strings),1), self.tfidf.take(j,1)))
        return np.asarray(result)
                

    class TF:
        def __init__(self, strings:list[str], terms:list[str]=None):
            if strings is None:
                raise TypeError('strings must NOT be None')
            self.strings = strings
            self.terms = terms
            self.tf = ndarray((len(self.terms), len(self.strings)))
            self.process_tf()
        
        def process_tf(self):
            if self.terms is None:
                self.terms = TFIDF.extract_terms(self.strings)
            for i in range(len(self.terms)):
                # self.tf.append([])
                for j in range(len(self.strings)):
                    count = self.strings[j].count(self.terms[i])
                    self.tf[i][j] = 0 if count == 0 else (1 + log10(count))
            return self.tf

    class IDF:
        def __init__(self, strings:list[str], terms:list[str]=None):
            if strings is None:
                raise TypeError('strings must NOT be None')
            self.strings = strings
            self.terms = terms
            self.idf = []
            self.process_idf()
        
        def process_idf(self):
            if self.terms is None:
                self.terms = TFIDF.extract_terms(self.strings)
            for i in range(len(self.terms)):
                self.idf.append(0)
                for string in self.strings:
                    self.idf[i] += 1 if self.terms[i] in string else 0
                self.idf[i] = log10(len(self.strings) / self.idf[i])
            return self.idf
