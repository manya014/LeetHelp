/***********************
 * SAFETY + DEBUG
 ***********************/
console.log("LeetHelp content script loaded");

window.onerror = function (msg, url, line, col) {
  alert("LeetHelp JS Error:\n" + msg);
};

/***********************
 * PREVENT DUPLICATES
 ***********************/
if (document.getElementById("leethelp-root")) {
  console.log("LeetHelp already injected");
} else {
  initLeetHelp();
}

/***********************
 * MAIN INIT
 ***********************/
function initLeetHelp() {
  /***********************
   * CREATE ROOT
   ***********************/
  const root = document.createElement("div");
  root.id = "leethelp-root";

  Object.assign(root.style, {
    position: "fixed",
    bottom: "20px",
    right: "20px",
    width: "360px",
    height: "480px",
    background: "#0f172a",
    color: "white",
    zIndex: "999999",
    borderRadius: "12px",
    display: "flex",
    flexDirection: "column",
    fontFamily: "system-ui",
    boxShadow: "0 20px 40px rgba(0,0,0,0.5)",
  });

  root.innerHTML = `
    <div style="padding:10px;font-weight:bold;background:#020617">
      LeetHelp AI
    </div>

    <div id="leethelp-messages"
         style="flex:1;padding:10px;overflow-y:auto;font-size:14px">
      <div style="opacity:0.7">
        Ask for hint, approach, or code…
      </div>
    </div>

    <div style="display:flex;padding:8px;border-top:1px solid #334155">
      <input id="leethelp-input"
             placeholder="Type here…"
             style="flex:1;padding:6px;border-radius:6px;border:none"/>

      <button id="leethelp-send"
              style="margin-left:6px;padding:6px 10px;
                     background:#22c55e;border:none;border-radius:6px">
        Send
      </button>
    </div>
  `;

  document.body.appendChild(root);

  /***********************
   * ELEMENTS
   ***********************/
  const messages = root.querySelector("#leethelp-messages");
  const input = root.querySelector("#leethelp-input");
  const sendBtn = root.querySelector("#leethelp-send");

  /***********************
   * HELPERS
   ***********************/
  function addMessage(text, who) {
    const div = document.createElement("div");
    div.textContent = text;

    Object.assign(div.style, {
      margin: "6px 0",
      padding: "6px 8px",
      borderRadius: "6px",
      background: who === "user" ? "#1e40af" : "#064e3b",
      whiteSpace: "pre-wrap",
    });

    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  /***********************
   * PROBLEM CONTEXT
   ***********************/
  function getProblemContext() {
    const title =
      document.querySelector("div[data-cy='question-title']")?.innerText ||
      document.querySelector("h1")?.innerText ||
      "";

    const description =
      document.querySelector('[data-track-load="description_content"]')
        ?.innerText || "";

    return { title, description };
  }

  /***********************
   * SEND HANDLER
   ***********************/
  sendBtn.onclick = async () => {
    const userText = input.value.trim();
    if (!userText) return;

    addMessage(userText, "user");
    input.value = "";

    const ctx = getProblemContext();

    addMessage("Thinking...", "ai");

    try {
      const res = await fetch("http://127.0.0.1:8000/solve", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: ctx.title,
          description: ctx.description,
          user_query: userText,
        }),
      });

      const data = await res.json();
      messages.lastChild.remove();

      addMessage(data.answer || "No response", "ai");
    } catch (err) {
      messages.lastChild.remove();
      addMessage("Backend error. Is server running?", "ai");
      console.error(err);
    }
  };
}
