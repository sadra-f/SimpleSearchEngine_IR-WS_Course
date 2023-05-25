from IO.Read import Reader
from vectorize.TFIDF import TFIDF

rds = Reader()

inp = rds.read_dataset()
test = rds.read_queries()

model = TFIDF([inp[i].text for i in range(len(inp))], [test[i].text for i in range(len(test))])


print("Test")

