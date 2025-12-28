
# 🚀 LeetHelp

**LeetHelp** is an intelligent LeetCode companion tool designed to help users understand problems better by providing **hints, approaches, and solutions** in an interactive way.  
It works as a **browser-based assistant / extension-style app**, enhancing the problem-solving experience without directly spoiling solutions.

---

## ✨ Features

- 🧠 **Problem-aware assistance**  
  Detects the currently opened LeetCode problem and understands its context.

- 💡 **Hints & Step-by-step Approaches**  
  Provides guided hints and explanations instead of direct answers.

- 🤖 **AI-powered Responses**  
  Uses an LLM-backed backend to generate clean, structured solutions and explanations.

- 🔍 **Sample Input/Output Awareness**  
  Leverages problem examples for better reasoning and contextual help.

- 🌐 **Interactive Chat-style UI**  
  Ask follow-up questions just like a chatbot.

---

## 🛠️ Tech Stack

### Frontend
- JavaScript
- HTML, CSS
- Chrome Extension APIs / Browser DOM APIs

### Backend
- Python
- FastAPI / Flask
- LLM APIs
- REST APIs

### Others
- Git & GitHub
- Prompt Engineering
- (Optional) RAG / Vector Search for future improvements

---

## 📂 Project Structure

```

LeetHelp/
├── backend/
│   ├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── ...
├── frontend/
│   ├── content.js
│   ├── popup.html
│   ├── popup.js
│   └── ...
├── README.md
└── .gitignore

````

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/manya014/LeetHelp.git
cd LeetHelp
````

### 2️⃣ Backend setup

```bash
cd backend
python -m venv venv
venv/Scripts/activate   # Windows
pip install -r requirements.txt
```

Run the backend:

```bash
uvicorn main:app --reload
```

---

### 3️⃣ Frontend / Extension setup

1. Open **Chrome**
2. Go to `chrome://extensions`
3. Enable **Developer mode**
4. Click **Load unpacked**
5. Select the `frontend` folder

---

## 🧪 Usage

1. Open a problem on **LeetCode**
2. Activate LeetHelp
3. Ask for:

   * Hints
   * Approach
   * Edge cases
   * Optimizations
4. Solve smarter, not harder 🚀

---

## Screenshots
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/f8a0fa76-7975-41da-a7a5-c533358a4089" />


## 🧩 Future Enhancements

* ⭐ Bookmark & history tracking
* ⏱️ Contest mode support
* 🔐 User authentication
* 📊 Personalized difficulty analytics

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👩‍💻 Author

**Manya Rawat**

* GitHub: [@manya014](https://github.com/manya014)
* LeetCode | Codeforces | CodeChef

---

⭐ If you find LeetHelp useful, consider giving it a star!


```
