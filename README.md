# Company Search Chatbot

A demo project that shows how to build a **company search assistant** using:

- **OpenAI File Search / Vector Stores** → for answering from documents  
- **Vanna API** → for querying structured analytics data  

The chatbot can answer questions from uploaded company files and also handle structured queries such as usage metrics.  

---

## ✨ Features

- Upload and index your own documents (PDF, DOCX, TXT, etc.)  
- Natural language search across documents  
- Route analytics questions to the Vanna API  
- Combine unstructured and structured results in one chatbot  

---

## ⚙️ Setup

Run the following commands:

```bash
# 1. Clone the repo
git clone https://github.com/adityasudhakar/company-search.git
cd company-search

# 2. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows PowerShell

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
```

Edit `.env` with your keys:
```
OPENAI_API_KEY=your-openai-api-key
VANNA_API_KEY=your-vanna-api-key
VANNA_USER_EMAIL=your-email@company.com
VECTOR_STORE_ID=your-vector-store-id
```

⚠️ **Never commit `.env` to GitHub.** Only share `.env.example`.  

---

## 🚀 Usage

```bash
# Upload files & create a vector store
python upload_files.py
python vectorstore.py
python files_to_vector.py
python vector_status.py

# Run the chatbot
python chatbot.py
```

### Example queries
- *“What is the GCP VM architecture?”* → answered from docs  
- *“How many hosted app questions were asked in the last 24 hours?”* → routed to Vanna  

---

## 📂 Project Structure

```
company-search/
├── chatbot.py           # main chatbot (docs + Vanna)
├── upload_files.py      # upload files to OpenAI
├── vectorstore.py       # create a vector store
├── files_to_vector.py   # attach files to store
├── vector_status.py     # check file indexing status
├── requirements.txt     # dependencies
├── .env.example         # sample env file
├── .gitignore           # ignores .env, venv, etc.
└── README.md            # this file
```

---

## 🔒 Security

- API keys and private company files are **not included** in this repo  
- Secrets should go into `.env` (ignored in `.gitignore`)  
- You can safely demo this chatbot using public PDFs or docs  
