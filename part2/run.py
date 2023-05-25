from IO.Read import Reader
from vectorize.TFIDF import TFIDF

rds = Reader()

dataset = rds.read_dataset()
query = rds.read_queries()

inp_model = TFIDF([dataset[i].text for i in range(len(dataset))])
query_model = TFIDF([query[i].text for i in range(len(query))])

print("Model")

