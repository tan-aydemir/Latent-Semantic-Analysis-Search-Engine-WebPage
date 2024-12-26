# LSA Search Engine Webpage

This project implements a basic search engine using **Latent Semantic Analysis (LSA)**. It allows users to query a predefined dataset and retrieve the most relevant documents based on **cosine similarity**. The web application includes a responsive user interface and visualization for query results.

---

## Features

1. **Interactive Document Retrieval**:
   - Users can enter a query to retrieve the top 5 relevant documents from the dataset.
   - Results are ranked based on cosine similarity.

2. **Visualization**:
   - A bar chart displays the similarity scores of the top documents.

3. **Responsive User Interface**:
   - Input field for queries and a "Search" button.
   - Results section displays document summaries and similarity scores.

4. **Efficiency**:
   - Dimensionality reduction using LSA optimizes performance for large datasets.

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript, Plotly.js
- **Data Processing**: NumPy, Scikit-learn
- **Visualization**: Plotly.js
- **Dataset**: [20 Newsgroups Dataset](https://scikit-learn.org/0.19/datasets/twenty_newsgroups.html)

---

## Dataset

This project uses the `20 Newsgroups` dataset. It is preprocessed into a Term-Document Matrix using **TF-IDF**.

```python
from sklearn.datasets import fetch_20newsgroups
newsgroups = fetch_20newsgroups(subset='all')
