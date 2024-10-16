document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.querySelector('#chat-messages');
    const userInput = document.getElementById('user-input');
    const submitButton = document.getElementById('submit-button');
    const loadingIndicator = document.getElementById('loading');
    const clearChatButton = document.getElementById('clear-chat');

    submitButton.addEventListener('click', submitQuery);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            submitQuery();
        }
    });
    clearChatButton.addEventListener('click', clearChat);

    function submitQuery() {
        const query = userInput.value.trim();
        if (!query) return;

        addMessage('user', query);
        userInput.value = '';
        loadingIndicator.style.display = 'flex';

        // Fetching the response from the server
        fetch('http://localhost:5000/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({query: query}),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            addMessage('bot', data.answer, true);
            if (data.sources && data.sources.length > 0) {
                addMessage('bot', 'Sources: ' + data.sources.join(', '));
            }
            loadingIndicator.style.display = 'none';
        })
        .catch(error => {
            console.error('Error:', error);
            addMessage('bot', 'Sorry, an error occurred. Please try again later.', true);
            loadingIndicator.style.display = 'none';
        });
    }

    function addMessage(sender, text, animate = false) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', `${sender}-message`);
        
        if (animate && sender === 'bot') {
            messageElement.classList.add('typing');
            let i = 0;
            const typingEffect = setInterval(() => {
                if (i < text.length) {
                    messageElement.innerHTML += text.charAt(i);
                    i++;
                } else {
                    clearInterval(typingEffect);
                    messageElement.classList.remove('typing');
                    messageElement.innerHTML = marked(text);
                }
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }, 30);
        } else {
            messageElement.innerHTML = marked(text);
        }
        
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function clearChat() {
        chatMessages.innerHTML = '';
    }
});
