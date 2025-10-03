Company Search Chatbot (Demo)

This project demonstrates how to build a company search chatbot that can:

Search over documents (using OpenAI File Search / vector stores).

Query structured analytics data (via the Vanna API).

The chatbot can answer questions either from your uploaded company files or by querying Vanna for metrics like usage, counts, and analytics.

🚀 Features

Upload your own PDFs, DOCX, or TXT files into a vector store.

Search documents with natural language questions.

Route structured queries (e.g. “hosted app usage in last 24 hours”) to the Vanna API.

Combine both sources for a unified company search assistant.

⚙️ Setup
1. Clone this repo
git clone https://github.com/your-username/company-search-chatbot.git
cd company-search-chatbot

2. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows PowerShell

3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

4. Configure environment variables

Copy .env.example to .env and fill in your own keys:

cp .env.example .env


Inside .env:

OPENAI_API_KEY=your-openai-api-key-here
VANNA_API_KEY=your-vanna-api-key-here
VANNA_USER_EMAIL=your-email@domain.com
VECTOR_STORE_ID=your-vector-store-id


⚠️ Never commit your real .env to GitHub. Only push .env.example.

📂 Project Structure
company-search-chatbot/
│
├── chatbot.py           # main chatbot combining file search + Vanna
├── upload_files.py      # helper to upload files to OpenAI
├── vectorstore.py       # create a new vector store
├── files_to_vector.py   # attach files to vector store
├── vector_status.py     # check file processing status
├── requirements.txt     # dependencies
├── .env.example         # sample env file
├── .gitignore           # ignore venv, .env, etc.
└── README.md            # this file

🧑‍💻 Usage

Upload files:

python upload_files.py
python vectorstore.py
python files_to_vector.py
python vector_status.py


Run the chatbot:

python chatbot.py


Example queries:

“What is the GCP VM architecture?” → answers from your docs

“How many hosted app questions were asked in the last 36 hours?” → routed to Vanna

🔒 Security

API keys and private company files are not included in this repo.

Always store secrets in .env and add .env to .gitignore.

You can safely demo this chatbot using public files (e.g. sample PDFs) without exposing private data.