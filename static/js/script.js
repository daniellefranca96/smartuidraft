    const userInputEl = document.getElementById('userInput');
    const sendButtonEl = document.getElementById('sendButton');
    const messagesEl = document.getElementById('messages');
    const displayEl = document.getElementById('display');
	const downloadButtonEl = document.getElementById('downloadButton');
	const loadingEl = document.getElementById('loading');
	downloadButtonEl.disabled = true;

    function sendMessage() {
    if (userInputEl.value.trim() !== '') {
        const userMessage = document.createElement('div');
        userMessage.textContent = 'User: ' + userInputEl.value;
        userMessage.classList.add('message');
        messagesEl.appendChild(userMessage);
		sendButtonEl.disabled = true;
		downloadButtonEl.disabled = true;
		loadingEl.hidden = false;
		
        fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ request: userInputEl.value })
        })
        .then(response => response.json())
        .then(json => {
            const iframe = document.getElementById('display');
			const doc = iframe.contentDocument || iframe.contentWindow.document;
			doc.open();
			doc.write(json.data);
			doc.close();
			setTimeout(() => {
				adjustIframeHeight(iframe);
				sendButtonEl.disabled = false;
			}, 100);
			
			sendButtonEl.disabled = false;
			downloadButtonEl.disabled = false;
			loadingEl.hidden = true;
        })
        .catch(error => {
            console.error('Error:', error);
        });

        userInputEl.value = '';
        messagesEl.scrollTop = messagesEl.scrollHeight;
		
		while (messagesEl.children.length > 2) {
            messagesEl.removeChild(messagesEl.firstChild);
        }
    }
}


    userInputEl.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });
	

	downloadButtonEl.addEventListener('click', function() {
		window.open('/download', '_blank');
	});
	
	function adjustIframeHeight(iframe) {
		try {
			// Set the iframe height to its content height
			iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px';
		} catch (e) {
			console.error('Could not adjust iframe height:', e);
    }
}

    sendButtonEl.addEventListener('click', sendMessage);