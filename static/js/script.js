    const userInputEl = document.getElementById('userInput');
    const sendButtonEl = document.getElementById('sendButton');
    const messagesEl = document.getElementById('messages');
    const displayEl = document.getElementById('display');
    const downloadButtonEl = document.getElementById('downloadButton');
    const loadingEl = document.getElementById('loading');
    const templateEl = document.getElementById('template');
    const undoButtonEl = document.getElementById('undoButton');

    downloadButtonEl.disabled = true;
    undoButtonEl.disabled = true;

    let previousCode = '';

    function sendMessage(event) {
		event.preventDefault();
		sendButtonEl.disabled = true;
        if (userInputEl.value.trim() !== '') {
            const userMessage = document.createElement('div');
            userMessage.textContent = 'User: ' + userInputEl.value;
            userMessage.classList.add('message');
			messagesEl.appendChild(userMessage);
            downloadButtonEl.disabled = true;
            undoButtonEl.disabled = true;
            loadingEl.hidden = false;

            const formData = new FormData();
            if (templateEl.files.length > 0) {
                formData.append('file', templateEl.files[0]);
            }
            formData.append('request', userInputEl.value);

            fetch('/generate', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(json => {
                const iframe = document.getElementById('display');
                const doc = iframe.contentDocument || iframe.contentWindow.document;
				previousCode = doc.documentElement.innerHTML;
                doc.open();
                doc.write(json.data);
                doc.close();
                setTimeout(() => {
                    adjustIframeHeight(iframe);
                    sendButtonEl.disabled = false;
                    undoButtonEl.disabled = false;
                }, 100);

                sendButtonEl.disabled = false;
                downloadButtonEl.disabled = false;
                undoButtonEl.disabled = false;
                loadingEl.hidden = true;

            })
            .catch(error => {
				sendButtonEl.disabled = false;
				undoButtonEl.disabled = false;
				loadingEl.hidden = true;
				alert("An error occur while processing your request please try again.")
                console.error('Error:', error);
            });
			
			userInputEl.value = '';
            messagesEl.scrollTop = messagesEl.scrollHeight;

            while (messagesEl.children.length > 2) {
                messagesEl.removeChild(messagesEl.firstChild);
            }
        }
    }

    downloadButtonEl.addEventListener('click', function() {
        window.open('/download?filename=' + encodeURIComponent(templateEl.value), '_blank');
    });

    sendButtonEl.addEventListener('click', function(event) {
        sendMessage(event);
    });

    undoButtonEl.addEventListener('click', function() {
        if (previousCode !== '') {
            const iframe = document.getElementById('display');
			const doc = iframe.contentDocument || iframe.contentWindow.document;
			doc.open();
			doc.write(previousCode);
			doc.close();
			setTimeout(() => {
				adjustIframeHeight(iframe);
			}, 100);
            sendButtonEl.disabled = false;
            downloadButtonEl.disabled = false;
            undoButtonEl.disabled = true;
            loadingEl.hidden = true;
            messagesEl.removeChild(messagesEl.firstChild);
            userInputEl.value = '';
        }
    });

    function adjustIframeHeight(iframe) {
        try {
            // Set the iframe height to its content height
            iframe.style.height = iframe.contentWindow.document.body.scrollHeight+250 + 'px';
        } catch (e) {
            console.error('Could not adjust iframe height:', e);
        }
    }
