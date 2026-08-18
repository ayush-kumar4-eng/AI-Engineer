// const API_URL = "https://ayushai-atvj.onrender.com/chat";

// const chatArea = document.querySelector(".chat-area");
// const composer = document.querySelector(".composer");
// const input = document.querySelector(".composer input");
// const sendButton = document.querySelector(".composer button");

// // ==========================================
// // 2. Submit Question
// // ==========================================

// composer.addEventListener("submit", async (event) => {

//     event.preventDefault();

//     const question = input.value.trim();

//     if (!question) {
//         return;
//     }

//     await askQuestion(question);

// });


// // ==========================================
// // 3. Main Chat Function
// // ==========================================

// async function askQuestion(question) {

//     // Add user message
//     addUserMessage(question);

//     // Clear input
//     input.value = "";

//     // Disable input while AI is answering
//     setLoading(true);

//     // Add temporary thinking message
//     const thinkingMessage = addThinkingMessage();

//     try {

//         const response = await fetch(API_URL, {

//             method: "POST",

//             headers: {
//                 "Content-Type": "application/json"
//             },

//             body: JSON.stringify({
//                 question: question
//             })

//         });


//         // Check HTTP response
//         if (!response.ok) {

//             throw new Error(
//                 `Server returned ${response.status}`
//             );

//         }


//         const data = await response.json();


//         // Remove "Thinking..."
//         thinkingMessage.remove();


//         // Get AI answer
//         const answer = data.answer;


//         if (!answer) {

//             addAIMessage(
//                 "I couldn't find an answer in Ayush's profile."
//             );

//             return;
//         }


//         // Show AI response with typing effect
//         await typeAIMessage(answer);


//     } catch (error) {

//         console.error("Chat error:", error);

//         thinkingMessage.remove();

//         addAIMessage(
//             `AyushAI connection error: ${error.message}`
//         );

//     } finally {

//         setLoading(false);

//     }

// }


// // ==========================================
// // 4. Add User Message
// // ==========================================

// function addUserMessage(text) {

//     const message = document.createElement("div");

//     message.className = "message user-message";


//     const bubble = document.createElement("div");

//     bubble.className = "user-bubble";

//     bubble.textContent = text;


//     message.appendChild(bubble);

//     chatArea.appendChild(message);


//     scrollToBottom();

// }


// // ==========================================
// // 5. Thinking Message
// // ==========================================

// function addThinkingMessage() {

//     const message = document.createElement("div");

//     message.className = "message ai-message";


//     const avatar = document.createElement("div");

//     avatar.className = "message-avatar";

//     avatar.textContent = "A";


//     const body = document.createElement("div");

//     body.className = "message-body";


//     const name = document.createElement("div");

//     name.className = "message-name";

//     name.textContent = "AYUSHAI";


//     const text = document.createElement("p");

//     text.textContent = "Thinking...";

//     text.classList.add("thinking");


//     body.appendChild(name);

//     body.appendChild(text);


//     message.appendChild(avatar);

//     message.appendChild(body);


//     chatArea.appendChild(message);


//     scrollToBottom();


//     return message;

// }


// // ==========================================
// // 6. Add AI Message
// // ==========================================

// function addAIMessage(text) {

//     const message = document.createElement("div");

//     message.className = "message ai-message";

//     const avatar = document.createElement("div");

//     avatar.className = "message-avatar";

//     avatar.textContent = "A";

//     const body = document.createElement("div");

//     body.className = "message-body";

//     const name = document.createElement("div");

//     name.className = "message-name";

//     name.textContent = "AYUSHAI";

//     const paragraph = document.createElement("div");

//     paragraph.className = "ai-content";

//     paragraph.innerHTML = marked.parse(text);

//     body.appendChild(name);
//     body.appendChild(paragraph);

//     message.appendChild(avatar);
//     message.appendChild(body);

//     chatArea.appendChild(message);

//     scrollToBottom();

//     return message;
// }


// // ==========================================
// // 7. AI Typing Effect
// // ==========================================

// async function typeAIMessage(text) {

//     const message = document.createElement("div");

//     message.className = "message ai-message";

//     const avatar = document.createElement("div");

//     avatar.className = "message-avatar";

//     avatar.textContent = "A";

//     const body = document.createElement("div");

//     body.className = "message-body";

//     const name = document.createElement("div");

//     name.className = "message-name";

//     name.textContent = "AYUSHAI";

//     const content = document.createElement("div");

//     content.className = "ai-content";

//     content.innerHTML = marked.parse(text);

//     body.appendChild(name);
//     body.appendChild(content);

//     message.appendChild(avatar);
//     message.appendChild(body);

//     chatArea.appendChild(message);

//     scrollToBottom();
// }


// // ==========================================
// // 8. Loading State
// // ==========================================

// function setLoading(isLoading) {

//     input.disabled = isLoading;

//     sendButton.disabled = isLoading;


//     if (isLoading) {

//         sendButton.innerHTML = `
//             <span>Thinking</span>
//             <b>...</b>
//         `;

//     } else {

//         sendButton.innerHTML = `
//             <span>Ask</span>
//             <b>↗</b>
//         `;

//     }

// }


// // ==========================================
// // 9. Scroll Chat
// // ==========================================

// function scrollToBottom() {

//     chatArea.scrollTo({

//         top: chatArea.scrollHeight,

//         behavior: "smooth"

//     });

// }


// // ==========================================
// // 10. Delay Helper
// // ==========================================

// function sleep(milliseconds) {

//     return new Promise(resolve => {

//         setTimeout(resolve, milliseconds);

//     });

// }


// // ==========================================
// // 11. Enter Key
// // ==========================================

// input.addEventListener("keydown", event => {

//     if (event.key === "Enter") {

//         event.preventDefault();

//         composer.requestSubmit();

//     }

// });


// // ==========================================
// // 12. Focus Input
// // ==========================================

// window.addEventListener("load", () => {

//     input.focus();

// });

// // ==========================================
// // LOCAL STORAGE - CHAT HISTORY
// // ==========================================

// const CHAT_STORAGE_KEY = "ayushAI_chat_history";


// // Save chat history
// function saveChatHistory() {

//     const messages = [];

//     const chatMessages = chatArea.querySelectorAll(".message");

//     chatMessages.forEach(message => {

//         const isUser = message.classList.contains("user-message");

//         const isAI = message.classList.contains("ai-message");

//         if (isUser) {

//             const bubble = message.querySelector(".user-bubble");

//             if (bubble) {

//                 messages.push({
//                     role: "user",
//                     content: bubble.textContent
//                 });

//             }

//         }

//         else if (isAI) {

//             const content = message.querySelector(".ai-content");

//             if (content) {

//                 messages.push({
//                     role: "assistant",
//                     content: content.innerText
//                 });

//             }

//         }

//     });


//     localStorage.setItem(
//         CHAT_STORAGE_KEY,
//         JSON.stringify(messages)
//     );
// }

// ==========================================
// 1. API CONFIGURATION
// ==========================================

const API_URL = "https://ayushai-atvj.onrender.com/chat";

const CHAT_STORAGE_KEY = "ayushAI_chat_history";


// ==========================================
// 2. DOM ELEMENTS
// ==========================================

const chatArea = document.querySelector(".chat-area");

const composer = document.querySelector(".composer");

const input = document.querySelector(".composer input");

const sendButton = document.querySelector(".composer button");

const clearButton = document.querySelector("#clear-chat");


// ==========================================
// 3. SUBMIT QUESTION
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
// 4. MAIN CHAT FUNCTION
// ==========================================

async function askQuestion(question) {

    // Add user message
    addUserMessage(question);

    // Clear input
    input.value = "";

    // Disable input
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

        console.log("Backend response:", data);


        // Remove thinking message
        thinkingMessage.remove();


        // Get AI answer
        const answer = data.answer;


        if (!answer) {

            addAIMessage(
                "I couldn't find an answer in Ayush's profile."
            );

            return;

        }


        // Show AI response
        await typeAIMessage(answer);


    } catch (error) {

        console.error("Chat error:", error);


        // Remove thinking message
        if (thinkingMessage) {
            thinkingMessage.remove();
        }


        addAIMessage(
            `I couldn't connect to AyushAI. Error: ${error.message}`
        );


    } finally {

        setLoading(false);

    }

}


// ==========================================
// 5. ADD USER MESSAGE
// ==========================================

function addUserMessage(text, save = true) {

    const message = document.createElement("div");

    message.className = "message user-message";


    const bubble = document.createElement("div");

    bubble.className = "user-bubble";

    bubble.textContent = text;


    message.appendChild(bubble);

    chatArea.appendChild(message);


    scrollToBottom();


    // Save to LocalStorage
    if (save) {

        saveChatHistory();

    }

}


// ==========================================
// 6. THINKING MESSAGE
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
// 7. ADD AI MESSAGE
// ==========================================

function addAIMessage(text, save = true) {

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


    // Render Markdown
    if (typeof marked !== "undefined") {

        content.innerHTML = marked.parse(text);

    } else {

        content.textContent = text;

    }


    body.appendChild(name);

    body.appendChild(content);


    message.appendChild(avatar);

    message.appendChild(body);


    chatArea.appendChild(message);


    scrollToBottom();


    // Save to LocalStorage
    if (save) {

        saveChatHistory();

    }


    return message;

}


// ==========================================
// 8. AI TYPING EFFECT
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


    body.appendChild(name);

    body.appendChild(content);


    message.appendChild(avatar);

    message.appendChild(body);


    chatArea.appendChild(message);


    // ======================================
    // Typing effect
    // ======================================

    for (let i = 0; i < text.length; i++) {

        const currentText = text.substring(
            0,
            i + 1
        );


        // Render Markdown while typing
        if (typeof marked !== "undefined") {

            content.innerHTML = marked.parse(
                currentText
            );

        } else {

            content.textContent = currentText;

        }


        scrollToBottom();


        await sleep(8);

    }


    // Save final AI response
    saveChatHistory();

}


// ==========================================
// 9. LOADING STATE
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
// 10. SCROLL CHAT
// ==========================================

function scrollToBottom() {

    chatArea.scrollTo({

        top: chatArea.scrollHeight,

        behavior: "smooth"

    });

}


// ==========================================
// 11. DELAY HELPER
// ==========================================

function sleep(milliseconds) {

    return new Promise(resolve => {

        setTimeout(resolve, milliseconds);

    });

}


// ==========================================
// 12. LOCAL STORAGE
// ==========================================

function saveChatHistory() {

    const messages = [];


    const chatMessages = chatArea.querySelectorAll(
        ".message"
    );


    chatMessages.forEach(message => {

        // -------------------------------
        // User message
        // -------------------------------

        if (
            message.classList.contains(
                "user-message"
            )
        ) {

            const bubble = message.querySelector(
                ".user-bubble"
            );


            if (bubble) {

                messages.push({

                    role: "user",

                    content: bubble.textContent

                });

            }

        }


        // -------------------------------
        // AI message
        // -------------------------------

        else if (
            message.classList.contains(
                "ai-message"
            )
        ) {

            const content = message.querySelector(
                ".ai-content"
            );


            if (content) {

                messages.push({

                    role: "assistant",

                    // innerText gives readable text
                    // instead of HTML

                    content: content.innerText

                });

            }

        }

    });


    localStorage.setItem(

        CHAT_STORAGE_KEY,

        JSON.stringify(messages)

    );

}


// ==========================================
// 13. LOAD CHAT HISTORY
// ==========================================

function loadChatHistory() {

    const savedHistory = localStorage.getItem(
        CHAT_STORAGE_KEY
    );


    // No previous conversation
    if (!savedHistory) {

        return;

    }


    try {

        const messages = JSON.parse(
            savedHistory
        );


        messages.forEach(message => {

            if (message.role === "user") {

                addUserMessage(
                    message.content,
                    false
                );

            }


            else if (
                message.role === "assistant"
            ) {

                addAIMessage(
                    message.content,
                    false
                );

            }

        });


        scrollToBottom();


    } catch (error) {

        console.error(
            "Could not load chat history:",
            error
        );


        // Remove corrupted history
        localStorage.removeItem(
            CHAT_STORAGE_KEY
        );

    }

}


// ==========================================
// 14. CLEAR CHAT HISTORY
// ==========================================

function clearChatHistory() {

    // Remove saved history
    localStorage.removeItem(
        CHAT_STORAGE_KEY
    );


    // Remove messages from UI
    chatArea.innerHTML = "";


    // Optional welcome message
    addAIMessage(
        "Hi! I'm **AyushAI**. Ask me anything about Ayush's education, skills, projects, certifications, experience, or achievements.",
        false
    );

}


// ==========================================
// 15. CLEAR CHAT BUTTON
// ==========================================

if (clearButton) {

    clearButton.addEventListener(
        "click",
        () => {

            clearChatHistory();

        }
    );

}


// ==========================================
// 16. ENTER KEY
// ==========================================

input.addEventListener(
    "keydown",
    event => {

        if (event.key === "Enter") {

            event.preventDefault();

            composer.requestSubmit();

        }

    }
);


// ==========================================
// 17. PAGE LOAD
// ==========================================

window.addEventListener(
    "load",
    () => {

        // Load previous conversation
        loadChatHistory();

        // Focus input
        input.focus();

    }
);