
class SimpleSearch:
    def __init__(self,invertedIndex:dict, doc_list:set):
        self.invertedIndex = invertedIndex
        self.doc_list = doc_list
    
    class Query:
        def __init__(self, type=None, value=None):
            self.type = type
            self.value = value

    def query(self, query:str):
        start_with = SimpleSearch.Query()
        other_queries = []
        last_end = 0


        def find_next_stop(start, str):
            for i in range(start, len(str)):
                if query[i] == '|' or query[i] == '&':
                    return i
                if i > 0 and str[i] == '!':
                    return i
                
                if i == len(query) - 1:
                    return i + 1
                
            return -1
                

        i = find_next_stop(0, query)
        if query[0] == '!':
            start_with.value = query[1:i]
            start_with.type = 'not'
        else:
            start_with.value = query[0:i]
            start_with.type = 'none'


        while i < len(query) - 1:
            if query[i] == '|':
                if query[i+1] == '!':
                    other_queries.append(SimpleSearch.Query('ornot',query[i + 2 :  find_next_stop(i + 2, query)]))
                else:
                    other_queries.append(SimpleSearch.Query('or',query[i + 1 : find_next_stop(i + 1, query)]))
            if query[i] == '&':
                if query[i+1] == '!':
                    other_queries.append(SimpleSearch.Query('andnot',query[i + 2 : find_next_stop(i + 2, query)]))
                else:
                    other_queries.append(SimpleSearch.Query('and',query[i + 1 : find_next_stop(i + 1, query)]))
            # if query[i] == '!':
            #     other_queries.append(SimpleSearch.Query('not', query[i+1: find_next_stop(i, query)]))# sorry, i dono regex :((
            
            i = find_next_stop(i + 1, query)            

        if start_with.type == 'none':
            res = set(self.invertedIndex[start_with.value])
        else:
            res = self.doc_list.difference(set(self.invertedIndex[start_with.value]))

        if len(other_queries) > 0:
            for i in range(0, len(other_queries)):
                if other_queries[i].type == 'or':
                    res = self.or_opr(res, other_queries[i].value)
                if other_queries[i].type == 'and':
                    res = self.and_opr(res, other_queries[i].value)
                if other_queries[i].type == 'not':
                    res = self.not_opr(res, other_queries[i].value)
                if other_queries[i].type == 'ornot':
                    res = res.union(self.doc_list.difference(set(self.invertedIndex[other_queries[i].value])))
                if other_queries[i].type == 'andnot':
                    res = res.intersection(self.doc_list.difference(set(self.invertedIndex[other_queries[i].value])))
        return res


    def and_opr(self, set:set, query):
        return set.intersection(self.invertedIndex[query])

    def or_opr(self, set:set, query):
        return set.union(self.invertedIndex[query])

    def not_opr(self, set:set, query):
        return set.difference(self.invertedIndex[query])
