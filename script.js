// ==================================================
// SPLASH SCREEN
// ==================================================

window.addEventListener("load", () => {

    setTimeout(() => {

        const splash =
            document.getElementById("splash");

        const login =
            document.getElementById("login");

        if (splash) {

            splash.style.opacity = "0";

            setTimeout(() => {

                splash.style.display = "none";

                if (login) {

                    login.style.display = "flex";
                }

            }, 500);
        }

    }, 2500);

});


// ==================================================
// LOGIN FUNCTION
// ==================================================

async function checkLogin() {

    let username =
        document.getElementById("username")
        .value.trim();

    let password =
        document.getElementById("password")
        .value.trim();

    let status =
        document.getElementById("status");

    // EMPTY CHECK

    if (!username || !password) {

        status.innerHTML =
            "⚠ Please enter username and password";

        status.style.color =
            "#facc15";

        return;
    }

    try {

        let response = await fetch("/login", {

            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({

                username: username,
                password: password

            })
        });

        let data =
            await response.json();

        // SUCCESS LOGIN

        if (data.success) {

            // HIDE LOGIN

            document.getElementById(
                "login"
            ).style.display = "none";

            // SHOW DASHBOARD

            document.getElementById(
                "dashboard"
            ).style.display = "flex";

            // SHOW CHAT SECTION

            showSection("chat");

            // HEADER UPDATE

            const header =
                document.querySelector(
                    ".header"
                );

            if (header) {

                header.innerHTML =
                    `🤖 Welcome ${username} 👋`;
            }

            // ADMIN BUTTON

            const adminBtn =
                document.getElementById(
                    "admin-btn"
                );

            if (data.role === "admin") {

                if (adminBtn) {

                    adminBtn.style.display =
                        "block";
                }

            } else {

                if (adminBtn) {

                    adminBtn.style.display =
                        "none";
                }
            }

            // SUCCESS STATUS

            status.innerHTML =
                "✅ Login Successful";

            status.style.color =
                "#22c55e";
        }

        // INVALID LOGIN

        else {

            status.innerHTML =
                "❌ Invalid Username or Password";

            status.style.color =
                "#ef4444";
        }

    }

    catch (error) {

        console.log(error);

        status.innerHTML =
            "❌ Server Error";

        status.style.color =
            "#ef4444";
    }
}


// ==================================================
// LOGIN ENTER KEY
// ==================================================

document.addEventListener(
    "DOMContentLoaded",
    () => {

        let passwordInput =
            document.getElementById(
                "password"
            );

        if (passwordInput) {

            passwordInput.addEventListener(
                "keypress",
                function (e) {

                    if (e.key === "Enter") {

                        checkLogin();
                    }
                }
            );
        }
    }
);


// ==================================================
// SIDEBAR TOGGLE
// ==================================================

let menuOpen = true;

function toggleMenu() {

    const sidebar =
        document.getElementById(
            "sidebar"
        );

    const buttons =
        sidebar.querySelectorAll(
            "button:not(:first-child)"
        );

    if (menuOpen) {

        sidebar.style.width =
            "80px";

        buttons.forEach(button => {

            button.style.display =
                "none";
        });

        menuOpen = false;
    }

    else {

        sidebar.style.width =
            "240px";

        buttons.forEach(button => {

            button.style.display =
                "block";
        });

        menuOpen = true;
    }
}


// ==================================================
// SHOW SECTIONS
// ==================================================

function showSection(section) {

    const sections = [

        "chat",
        "notification",
        "about"
    ];

    sections.forEach(sec => {

        const element =
            document.getElementById(
                sec + "-section"
            );

        if (element) {

            element.style.display =
                "none";
        }
    });

    const activeSection =
        document.getElementById(
            section + "-section"
        );

    if (activeSection) {

        activeSection.style.display =
            "block";
    }

    // LOAD NOTIFICATIONS

    if (section === "notification") {

        loadNotifications();
    }
}


// ==================================================
// SEND MESSAGE
// ==================================================

async function sendMessage() {

    const input =
        document.getElementById(
            "input"
        );

    const message =
        input.value.trim();

    if (!message) return;

    const chatArea =
        document.getElementById(
            "chatArea"
        );

    // USER MESSAGE

    chatArea.innerHTML += `

        <div class="user-msg">
            <b>You:</b><br>
            ${message}
        </div>
    `;

    // CLEAR INPUT

    input.value = "";

    // AUTO SCROLL

    chatArea.scrollTop =
        chatArea.scrollHeight;

    try {

        const response =
            await fetch("/chat", {

                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            });

        const data =
            await response.json();

        // BOT MESSAGE

        chatArea.innerHTML += `

            <div class="bot-msg">
                <b>AI Bot:</b><br><br>
                ${data.response.replace(/\n/g, "<br>")}
            </div>
        `;

        // TEXT TO SPEECH

        speakText(data.response);

        // AUTO SCROLL

        chatArea.scrollTop =
            chatArea.scrollHeight;

    }

    catch (error) {

        console.log(error);

        chatArea.innerHTML += `

            <div class="bot-msg">
                ❌ Server Error
            </div>
        `;
    }
}


// ==================================================
// ENTER KEY FOR CHAT
// ==================================================

document.addEventListener(
    "DOMContentLoaded",
    () => {

        const input =
            document.getElementById(
                "input"
            );

        if (input) {

            input.addEventListener(
                "keypress",
                function (e) {

                    if (e.key === "Enter") {

                        sendMessage();
                    }
                }
            );
        }
    }
);


// ==================================================
// CLEAR CHAT
// ==================================================

function clearChat() {

    const chatArea =
        document.getElementById(
            "chatArea"
        );

    if (chatArea) {

        chatArea.innerHTML = `
        
            <div class="bot-msg">
                👋 Chat Cleared Successfully
            </div>
        `;
    }

    window.speechSynthesis.cancel();
}


// ==================================================
// LOAD NOTIFICATIONS
// ==================================================

async function loadNotifications() {

    try {

        const response =
            await fetch(
                "/notifications"
            );

        const data =
            await response.json();

        let output = "";

        // EMPTY

        if (data.length === 0) {

            output = `

                <div class="notification-card">

                    🚫 No Notifications Available

                </div>
            `;
        }

        else {

            data.reverse().forEach(n => {

                output += `

                    <div class="notification-card">

                        <h3>
                            🔔 ${n.type}
                        </h3>

                        <br>

                        <p>
                            ${n.message}
                        </p>

                    </div>
                `;
            });
        }

        document.getElementById(
            "notification-data"
        ).innerHTML = output;

    }

    catch (error) {

        console.log(error);

        document.getElementById(
            "notification-data"
        ).innerHTML = `

            <div class="notification-card">

                ❌ Failed To Load Notifications

            </div>
        `;
    }
}


// ==================================================
// VOICE INPUT
// ==================================================

function startVoiceInput() {

    window.speechSynthesis.cancel();

    const SpeechRecognition =

        window.SpeechRecognition ||

        window.webkitSpeechRecognition;

    // NOT SUPPORTED

    if (!SpeechRecognition) {

        alert(
            "Voice Recognition Not Supported"
        );

        return;
    }

    const micButton =
        document.getElementById(
            "micButton"
        );

    const recognition =
        new SpeechRecognition();

    recognition.lang = "en-US";

    recognition.continuous = false;

    recognition.interimResults = false;

    // BUTTON UPDATE

    micButton.innerHTML =
        "🎙 Listening...";

    micButton.style.opacity =
        "0.8";

    // START

    recognition.start();

    // RESULT

    recognition.onresult =
        function (event) {

            const text =
                event.results[0][0]
                .transcript;

            document.getElementById(
                "input"
            ).value = text;
        };

    // END

    recognition.onend =
        function () {

            micButton.innerHTML =
                "🎤 Mic";

            micButton.style.opacity =
                "1";
        };

    // ERROR

    recognition.onerror =
        function (event) {

            console.log(event.error);

            micButton.innerHTML =
                "🎤 Mic";

            micButton.style.opacity =
                "1";

            alert(
                "Mic Error : " +
                event.error
            );
        };
}


// ==================================================
// TEXT TO SPEECH
// ==================================================

function speakText(text) {

    window.speechSynthesis.cancel();

    const speech =
        new SpeechSynthesisUtterance(
            text
        );

    speech.lang = "en-US";

    speech.rate = 1;

    speech.pitch = 1;

    speech.volume = 1;

    window.speechSynthesis
        .speak(speech);
}