function submitQuery() {
    var userInput = document.getElementById('user-input').value;
    // Send userInput to the backend and receive the response
    fetch('/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({query: userInput}),
    })
    .then(response => response.text())
    .then(data => {
        // Display the response in the 'response' div
        document.getElementById('response').innerHTML = data;
    });
}
