import os
import json
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer

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
vocab = vectorizer.get_feature_names_out()

index = {}
for term_index, term in enumerate(vocab):
    col = tfidf[:, term_index].toarray().ravel()
    postings = {}
    for i, score in enumerate(col):
        if score > 0:
            postings[doc_ids[i]] = float(score)
    index[term] = postings

json.dump(index, open("data/index.json", "w"))
