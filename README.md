# Agentic_RAG_system

An *Agentic* Retrieval‑Augmented Generation (RAG) system that answers questions about restaurants using customer reviews. It retrieves relevant feedback and generates concise, accurate summaries, helping users discover insights like food quality, service, or atmosphere from real customer experiences.

## 🎯 Features
- Ingests restaurant review data (e.g., from `realistic_restaurant_reviews.csv`)
- Converts reviews into vector embeddings (via `vector.py`)
- Performs semantic search over the embeddings to find relevant feedback
- Uses a language model (e.g., via `main.py`) to generate human‑readable summaries and answer questions
- Designed for restaurant‑specific queries (e.g., “What do customers say about vegan options?”, “How’s the service at XYZ?”, “Which restaurants have the best atmosphere?”)

## 📂 Repository Structure
- `.gitignore` — Files/folders to exclude from version control  
- `main.py` — Entry point / orchestration logic  
- `vector.py` — Embedding creation & vector store logic  
- `requirements.txt` — Python dependencies  
- `realistic_restaurant_reviews.csv` — Sample dataset of customer reviews  

## 🛠️ Getting Started
1. Clone this repository:
   ```bash
   git clone https://github.com/oshobabz/Agentic_RAG_system.git
   cd Agentic_RAG_system

##🧠 How it Works

Embedding & Vector Store: Reviews are converted into vector representations using a text embedding model. These are stored in a vector database/index for fast semantic retrieval.

Retrieval: When a user asks a question, the system retrieves the most relevant review embeddings (and associated text) via the vector store.

Generation: A language model is then prompted with the retrieved review excerpts and the user’s question; it synthesizes a coherent, concise answer grounded in the retrieved feedback.

Agentic Behavior: The system can direct the retrieval + generation flow (the “agent” part) — e.g., identify whether to fetch more reviews, filter by restaurant or category, and tailor the summarization.

##✅ Use Cases

Foodies seeking quick insights about restaurants before visiting

Restaurant owners wanting to monitor review themes (service, ambiance, menu quality)

Review analysis for market research or competitive benchmarking

##🚀 Next Steps & Enhancements

Add support for more review sources (Yelp, Google Reviews, TripAdvisor)

Introduce restaurant metadata filtering (e.g., cuisine type, location, price range)

Build a simple web UI or chatbot interface for interactive querying

Enable fine‑tuning of the language model for better domain alignment

Add caching and incremental indexing for ongoing review ingestion

📄 License & Contribution

Feel free to open issues or create pull requests for improvements. Specify the license here (e.g., MIT) if you want to share this as open source.
