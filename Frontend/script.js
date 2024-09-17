document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const submitButton = document.getElementById('submit-button');
    const loadingIndicator = document.getElementById('loading');

    submitButton.addEventListener('click', submitQuery);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            submitQuery();
        }
    });

    function submitQuery() {
        const query = userInput.value.trim();
        if (!query) return;

        addMessage('user', query);
        userInput.value = '';
        loadingIndicator.style.display = 'flex';

        fetch('/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({query: query}),
        })
        .then(response => response.text())
        .then(data => {
            addMessage('bot', data);
            loadingIndicator.style.display = 'none';
        })
        .catch(error => {
            console.error('Error:', error);
            addMessage('bot', 'Sorry, an error occurred. Please try again.');
            loadingIndicator.style.display = 'none';
        });
    }

    function addMessage(sender, text) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', `${sender}-message`);
        messageElement.textContent = text;
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
