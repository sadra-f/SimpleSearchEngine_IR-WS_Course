from IO.Read import Reader
from vectorize.TFIDF import TFIDF
from helpers import find_n_of_largest
rds = Reader()

inp = rds.read_dataset()
test = rds.read_queries()

model = TFIDF([inp[i].text for i in range(len(inp))], [test[i].text for i in range(len(test))])

similarity = model.calc_cosine_similarity()
top_ten =[]
for i in range(len(similarity)):
    top_ten.append(find_n_of_largest(similarity.take(i,0), 10))
print("Test")

