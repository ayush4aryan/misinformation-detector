# 🕵️ Misinformation Detector

![Demo Banner](https://dummyimage.com/800x200/74ebd5/fff&text=Misinformation+Detector+🕵️)  
*A GenAI Hackathon project by Team Script Kiddies 🚀*

---

## 🌍 Overview
The internet is flooded with misleading content. Our **Misinformation Detector** is a simple, web-based tool that helps people quickly analyze news articles, blogs, or social media posts and get a **Misinformation Score** with transparent reasoning.

---

## ⚡ Features
- **Text Input** – paste any article/excerpt for analysis  
- **Keyword Detection** – flags phrases like “secret cure,” “shocking,” “fake news”  
- **Sentiment Analysis** – detects emotional/biased tone  
- **Source Credibility Check** – verifies if a link comes from a trusted domain (.gov, .edu, major news sites)  
- **Visual UI** – risk shown with colored progress bar + highlighted risky terms in the text  

---

## 🛠 Tech Stack
- **Backend:** Python, Flask  
- **NLP:** TextBlob  
- **Frontend:** HTML, Bootstrap, CSS (Glassmorphism UI ✨)  
- **Other:** Regex + Validators  

---

## 🚀 How to Run Locally
```bash
# clone the repo
git clone https://github.com/ayush4aryan/misinformation-detector.git
cd misinformation-detector

# install requirements
pip install -r requirements.txt

# download textblob corpora (only needed the first time)
python -m textblob.download_corpora

# run the app
python app.py
Then open your browser at:
👉 http://127.0.0.1:5000

📸 Screenshots
(add these after you run locally — take screenshots and drag-drop into GitHub Readme)

Upload Box
Results (with progress bar + highlights)
📺 Demo Video
Watch here (insert YouTube or Google Drive link to your 3‑minute demo video)

🔗 Prototype Link
If hosted on Render/Heroku/Streamlit:
https://misinfo-checker.onrender.com

💡 Future Scope
Multilingual misinformation detection
Browser Extension (analyze posts on social media feeds directly)
ML Models for advanced claim verification
👨‍💻 Developed by Team Script Kiddies
(Ayush Aryan + teammates) for GenAI Hackathon 2025 ✨
