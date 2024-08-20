async function sendMessage() {
    const userInput = document.getElementById("user_input").value;
  
    const response = await fetch("/get_response", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: `user_input=${encodeURIComponent(userInput)}`,
    });
  
    const data = await response.json();
    document.getElementById("response").innerText = data.response;
  }