const chatBox = document.getElementById("chat-box");

function addMessage(sender, message) {
    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${sender}-message`;
    messageDiv.textContent = message;

    // 添加到聊天窗口
    chatBox.appendChild(messageDiv);

    // 自动滚动到底部
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const userInput = document.getElementById("user-input");
    const message = userInput.value.trim();
    if (!message) return;

    // 显示用户消息
    addMessage("user", message);
    userInput.value = "";

    // 调用后端 API 获取机器人回复
    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message }),
        });
        const data = await response.json();
        const botResponse = data.response || "Sorry, I couldn't understand that.";
        addMessage("bot", botResponse);
    } catch (error) {
        addMessage("bot", "An error occurred while processing your request.");
    }
}

// 按下回车键发送消息
document.getElementById("user-input").addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        sendMessage();
    }
});
