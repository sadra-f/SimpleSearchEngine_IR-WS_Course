from IO.Read import Reader
from vectorize.TFIDF import TFIDF
from helpers import find_n_of_largest
rds = Reader()

inp = rds.read_dataset()
test = rds.read_queries()

model = TFIDF([inp[i].text for i in range(len(inp))], [test[i].text for i in range(len(test))])

similarity = model.calc_cosine_similarity()
tmp = find_n_of_largest(similarity, 10)
print("Test")

