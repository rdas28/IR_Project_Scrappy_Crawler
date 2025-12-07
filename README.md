Information Retrieval Mini Search Engine
Developed by Riddhi Das (Student ID: 20582829)
Course: CS-429 Information Retrieval — Fall 2025
📌 Project Overview

This project implements a miniature search engine pipeline consisting of:

A Scrapy-based Web Crawler

Crawls Wikipedia pages starting from a seed URL.

HTML pages are saved locally for indexing.

A Scikit-Learn TF-IDF Indexer

Reads all crawled HTML files.

Extracts text, computes TF-IDF weights, and produces an inverted index (JSON).

A Query Processor & Ranker

Loads the index.

Applies cosine similarity to return Top-K ranked documents.

Outputs results as a CSV.

A Jupyter Notebook Report

Demonstrates code execution, outputs, analysis, and system explanation.

Includes test cases and commentary for each module.

📂 Repository Structure
IR_Project/
│
├── crawler/
│   ├── ircrawler/
│   │   └── spiders/wiki_spider.py     ← Scrapy crawler
│   └── scrapy.cfg
│
├── data/
│   ├── crawl_html/                    ← Crawled Wikipedia HTML files
│   ├── queries.csv
│   ├── results.csv
│   └── index.json                     ← Generated inverted index
│
├── indexer/
│   └── build_index.py                 ← TF-IDF index builder
│
├── processor/
│   └── rank_queries.py                ← Query ranking script
│
├── notebook/
│   └── project.ipynb                  ← End-to-end analysis + outputs
│
├── crawler_samples/                   ← 2–3 sample HTML files for report
│
└── README.md

🚀 How to Run the Project
1. Run the Scrapy Crawler

From the project root:

cd crawler
scrapy crawl wiki_spider


The HTML files will be saved to:

data/crawl_html/

2. Build the TF-IDF Index

From project root:

python indexer/build_index.py


Creates:

data/index.json

3. Run the Query Ranker
python processor/rank_queries.py


Produces:

data/results.csv

🧪 Test Cases

The system was tested using:

Valid queries

Highly specific queries

Out-of-vocabulary (garbage) queries

Short single-word queries

All tests ran successfully with correct TF-IDF cosine ranking behavior.

📘 Jupyter Notebook

The notebook includes:

System explanation

Code for crawling, indexing, and ranking

Outputs from each module

Test case results

Final CSV preview

Commentary before every step

This satisfies the course requirement of having write-up + code + outputs in one place.

🛠️ Dependencies

Python 3.12+

Scrapy 2.13+

scikit-learn 1.6+

BeautifulSoup4

Flask (optional, not used in minimal config)

Install via:

pip install -r requirements.txt


(If you want, I can create the requirements.txt file too.)

🔗 Source Code Access

All source code for the crawler, indexer, and ranking system is contained in this repository.
This repository link is included in the project report for verification.

✍️ Authorship Statement

This project was developed by Riddhi Das, with logical guidance from ChatGPT.
No external repositories or pre-built IR systems were used.
All code in this repository was written specifically for this assignment.

📄 License

This project is for academic use in CS-429 Information Retrieval and is not licensed for redistribution.
