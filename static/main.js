document.getElementById('search-form').addEventListener('submit', function (event) {
    event.preventDefault();
    
    let query = document.getElementById('query').value;
    let resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';


    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'query': query
        })
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data);
        displayChart(data);
    });
});

function displayResults(data) {
    let resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '<h2>Results</h2>';
    for (let i = 0; i < data.documents.length; i++) {
        let docDiv = document.createElement('div');
        docDiv.innerHTML = `<strong>Document ${data.indices[i]}</strong><p>${data.documents[i]}</p><br><strong>Similarity: ${data.similarities[i]}</strong>`;
        resultsDiv.appendChild(docDiv);
    }
}
    function displayChart(data) {
        // Input: data (object) - contains the following keys:
        //        - documents (list) - list of documents
        //        - indices (list) - list of indices   
        //        - similarities (list) - list of similarities
        // TODO: Implement function to display chart here
        //       There is a canvas element in the HTML file with the id 'similarity-chart'
        let ctx = document.getElementById('similarity-chart').getContext('2d');

        if (window.similarityChart) {
            window.similarityChart.destroy();
        }
        console.log("Does it ever come here");
        window.similarityChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.indices.map(i => `Doc ${i + 1}`), // Adjust for 1-based index
                datasets: [{
                    label: 'Cosine Similarity',
                    data: data.similarities,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 1 // Adjust scale to fit similarity scores
                    }
                }
            }
        });

        console.log("Chart displayed successfully!");  // Print confirmation
    }