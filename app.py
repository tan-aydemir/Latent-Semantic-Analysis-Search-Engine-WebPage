from flask import Flask, render_template, request, jsonify
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

app = Flask(__name__)


# TODO: Fetch dataset, initialize vectorizer and LSA here
newsgroup = fetch_20newsgroups(subset='all')
documents = newsgroup.data

vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'), max_features=10000)
tfidf_matrix = vectorizer.fit_transform(documents)

svd = TruncatedSVD(n_components=100)
lsa_matrix = svd.fit_transform(tfidf_matrix)


def search_engine(query):
    """
    Function to search for top 5 similar documents given a query
    Input: query (str)
    Output: documents (list), similarities (list), indices (list)
    """
    # TODO: Implement search engine here
    # return documents, similarities, indices 
    query_vec = vectorizer.transform([query])
    query_lsa = svd.transform(query_vec)

    # Compute cosine similarities
    similarity = cosine_similarity(query_lsa, lsa_matrix)[0]

    # Get top 5 indices based on the similarity scores
    top_indices = np.argsort(similarity)[-5:][::-1]

    # Get associated docs and their similarity score
    top_documents = [documents[i] for i in top_indices]
    top_similarities = [similarity[i] for i in top_indices]

    return top_documents, top_similarities, top_indices

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    documents, similarities, indices = search_engine(query)

    # Numpy arrays --> lists
    similarities = similarities.tolist() if isinstance(similarities, np.ndarray) else similarities
    indices = indices.tolist() if isinstance(indices, np.ndarray) else indices

    # print("Printing jsonify")
    # print("Documents =", documents)
    # print("Similarities =", similarities)
    # print("Indices = ", indices)

    return jsonify({'documents': documents, 'similarities': similarities, 'indices': indices})


if __name__ == '__main__':
    app.run(debug=True, port=3000)
