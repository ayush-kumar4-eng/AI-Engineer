const API_URL = "https://ayushai-atvj.onrender.com/chat";

const chatArea = document.querySelector(".chat-area");
const composer = document.querySelector(".composer");
const input = document.querySelector(".composer input");
const sendButton = document.querySelector(".composer button");

// ==========================================
// 2. Submit Question
// ==========================================

composer.addEventListener("submit", async (event) => {

    event.preventDefault();

    const question = input.value.trim();

    if (!question) {
        return;
    }

    await askQuestion(question);

});


// ==========================================
// 3. Main Chat Function
// ==========================================

async function askQuestion(question) {

    // Add user message
    addUserMessage(question);

    // Clear input
    input.value = "";

    // Disable input while AI is answering
    setLoading(true);

    // Add temporary thinking message
    const thinkingMessage = addThinkingMessage();

    try {

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });


        // Check HTTP response
        if (!response.ok) {

            throw new Error(
                `Server returned ${response.status}`
            );

        }


        const data = await response.json();


        // Remove "Thinking..."
        thinkingMessage.remove();


        // Get AI answer
        const answer = data.answer;


        if (!answer) {

            addAIMessage(
                "I couldn't find an answer in Ayush's profile."
            );

            return;
        }


        // Show AI response with typing effect
        await typeAIMessage(answer);


    } catch (error) {

        console.error("Chat error:", error);

        thinkingMessage.remove();

        addAIMessage(
            `AyushAI connection error: ${error.message}`
        );

    } finally {

        setLoading(false);

    }

}


// ==========================================
// 4. Add User Message
// ==========================================

function addUserMessage(text) {

    const message = document.createElement("div");

    message.className = "message user-message";


    const bubble = document.createElement("div");

    bubble.className = "user-bubble";

    bubble.textContent = text;


    message.appendChild(bubble);

    chatArea.appendChild(message);


    scrollToBottom();

}


// ==========================================
// 5. Thinking Message
// ==========================================

function addThinkingMessage() {

    const message = document.createElement("div");

    message.className = "message ai-message";


    const avatar = document.createElement("div");

    avatar.className = "message-avatar";

    avatar.textContent = "A";


    const body = document.createElement("div");

    body.className = "message-body";


    const name = document.createElement("div");

    name.className = "message-name";

    name.textContent = "AYUSHAI";


    const text = document.createElement("p");

    text.textContent = "Thinking...";

    text.classList.add("thinking");


    body.appendChild(name);

    body.appendChild(text);


    message.appendChild(avatar);

    message.appendChild(body);


    chatArea.appendChild(message);


    scrollToBottom();


    return message;

}


// ==========================================
// 6. Add AI Message
// ==========================================

function addAIMessage(text) {

    const message = document.createElement("div");

    message.className = "message ai-message";

    const avatar = document.createElement("div");

    avatar.className = "message-avatar";

    avatar.textContent = "A";

    const body = document.createElement("div");

    body.className = "message-body";

    const name = document.createElement("div");

    name.className = "message-name";

    name.textContent = "AYUSHAI";

    const paragraph = document.createElement("div");

    paragraph.className = "ai-content";

    paragraph.innerHTML = marked.parse(text);

    body.appendChild(name);
    body.appendChild(paragraph);

    message.appendChild(avatar);
    message.appendChild(body);

    chatArea.appendChild(message);

    scrollToBottom();

    return message;
}


// ==========================================
// 7. AI Typing Effect
// ==========================================

async function typeAIMessage(text) {

    const message = document.createElement("div");

    message.className = "message ai-message";

    const avatar = document.createElement("div");

    avatar.className = "message-avatar";

    avatar.textContent = "A";

    const body = document.createElement("div");

    body.className = "message-body";

    const name = document.createElement("div");

    name.className = "message-name";

    name.textContent = "AYUSHAI";

    const content = document.createElement("div");

    content.className = "ai-content";

    content.innerHTML = marked.parse(text);

    body.appendChild(name);
    body.appendChild(content);

    message.appendChild(avatar);
    message.appendChild(body);

    chatArea.appendChild(message);

    scrollToBottom();
}


// ==========================================
// 8. Loading State
// ==========================================

function setLoading(isLoading) {

    input.disabled = isLoading;

    sendButton.disabled = isLoading;


    if (isLoading) {

        sendButton.innerHTML = `
            <span>Thinking</span>
            <b>...</b>
        `;

    } else {

        sendButton.innerHTML = `
            <span>Ask</span>
            <b>↗</b>
        `;

    }

}


// ==========================================
// 9. Scroll Chat
// ==========================================

function scrollToBottom() {

    chatArea.scrollTo({

        top: chatArea.scrollHeight,

        behavior: "smooth"

    });

}


// ==========================================
// 10. Delay Helper
// ==========================================

function sleep(milliseconds) {

    return new Promise(resolve => {

        setTimeout(resolve, milliseconds);

    });

}


// ==========================================
// 11. Enter Key
// ==========================================

input.addEventListener("keydown", event => {

    if (event.key === "Enter") {

        event.preventDefault();

        composer.requestSubmit();

    }

});


// ==========================================
// 12. Focus Input
// ==========================================

window.addEventListener("load", () => {

    input.focus();

});