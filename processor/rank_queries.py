import csv
import json
import os
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

html_dir = "data/crawl_html"
docs = []
doc_ids = []

for f in os.listdir(html_dir):
    if f.endswith(".html"):
        path = os.path.join(html_dir, f)
        text = BeautifulSoup(open(path, encoding="utf-8"), "html.parser").get_text(" ", strip=True)
        docs.append(text)
        doc_ids.append(f)

vectorizer = TfidfVectorizer(stop_words="english")
tfidf = vectorizer.fit_transform(docs)

queries = []
with open("data/queries.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        queries.append((row["query_id"], row["query"] if "query" in row else row["query_text"]))

out = open("data/results.csv", "w")
writer = csv.writer(out)
writer.writerow(["query_id", "rank", "document_id"])

for qid, qtext in queries:
    qvec = vectorizer.transform([qtext])
    sims = cosine_similarity(qvec, tfidf).flatten()
    ranked = sims.argsort()[::-1][:3]
    for rank, idx in enumerate(ranked, start=1):
        writer.writerow([qid, rank, doc_ids[idx]])
