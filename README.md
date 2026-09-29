# 🚀 RAG Learning Projects

A hands-on **Retrieval-Augmented Generation (RAG)** learning repository created to build a strong practical understanding of RAG systems by implementing different components and gradually developing different types of RAG projects.

Rather than jumping directly into a complex RAG application, this repository focuses on understanding the **fundamentals behind RAG**, including document loading, document chunking, embeddings, vector stores, retrieval, and generation.

The goal is simple:

> **Learn RAG by building RAG.**

---

## 📌 About This Project

Retrieval-Augmented Generation (RAG) is an architecture that allows Large Language Models (LLMs) to retrieve relevant information from external data before generating an answer.

This project is part of a practical learning journey where different RAG concepts are implemented individually and then combined into complete applications.

The repository currently begins with the fundamental stages of a RAG pipeline:

```text
Documents
    ↓
Document Loading
    ↓
Document Chunking
    ↓
Embeddings
    ↓
Vector Store
    ↓
Retrieval
    ↓
Context
    ↓
LLM
    ↓
Generated Answer
```

The project will gradually evolve into multiple RAG implementations using different document types, retrieval strategies, models, and architectures.

---

# 🎯 Main Objective

The primary objective of this repository is to **build confidence and practical experience with RAG systems**.

Instead of learning RAG only through theory, this project focuses on:

* Building each RAG component manually
* Understanding why each component is required
* Experimenting with different document types
* Testing different chunking strategies
* Experimenting with embeddings
* Exploring vector databases
* Building different retrieval pipelines
* Connecting retrievers with LLMs
* Creating different types of RAG applications
* Understanding the limitations of RAG
* Gradually moving from basic RAG to advanced RAG

---

# 🧠 Why I Am Building Different RAG Projects

RAG is not a single technique.

There are many ways to design a RAG system depending on:

* The type of data
* The document format
* The size of the knowledge base
* The embedding model
* The vector database
* The retrieval strategy
* The LLM
* The prompting strategy
* The application's requirements

Therefore, this repository is designed as a **RAG experimentation playground**.

By building different RAG projects, I can understand how the architecture changes from one use case to another.

---

# 📚 Learning Approach

The learning process follows an incremental approach.

```text
Level 1
RAG Fundamentals
      ↓
Level 2
Document Processing
      ↓
Level 3
Embeddings & Vector Stores
      ↓
Level 4
Basic RAG
      ↓
Level 5
Advanced Retrieval
      ↓
Level 6
Different RAG Architectures
      ↓
Level 7
Production-Oriented RAG
```

Each project is intended to introduce a new RAG concept.

---

# 🔥 Current Project

The current implementation focuses on two fundamental RAG components:

1. Document Loading
2. Document Chunking

The current knowledge source is a personal `about_me` text document.

```text
about_me_sri_vardhan.txt
          ↓
      TextLoader
          ↓
       Documents
          ↓
RecursiveCharacterTextSplitter
          ↓
        Chunks
```

This provides a simple environment for understanding how raw documents are transformed before they are passed to embedding and retrieval systems.

---

# 📂 Project Structure

```text
Rag/
│
├── Data/
│   └── about_me_sri_vardhan.txt
│
├── project/
│   ├── data_loading.py
│   └── chunking.py
│
├── src/
│   └── rag/
│       └── __init__.py
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

# 📄 Data

The `Data` directory contains the knowledge source used by the initial RAG experiments.

### `about_me_sri_vardhan.txt`

This file contains information that can later be used as the knowledge base for a question-answering RAG application.

For example:

```text
User Question
      ↓
Retrieve relevant information
      ↓
Provide retrieved context
      ↓
LLM generates answer
```

Using a small personal dataset makes it easier to understand what is actually happening at every stage of the pipeline.

---

# 📥 1. Document Loading

The first step of the project is loading external data into the application.

The project uses LangChain's `TextLoader`.

```python
from langchain_community.document_loaders import TextLoader

document = TextLoader(
    "M:/Rag/Data/about_me_sri_vardhan.txt",
    encoding="utf-8"
)

docs = document.load()
```

The loader converts the text file into LangChain `Document` objects.

Conceptually:

```text
Text File
    ↓
TextLoader
    ↓
Document Object
```

A LangChain document generally contains:

```text
Document
├── page_content
└── metadata
```

---

# ✂️ 2. Document Chunking

Large documents should generally not be passed directly into an LLM.

Instead, the document is divided into smaller pieces called **chunks**.

The project uses:

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
```

The current configuration is:

```python
RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
```

The pipeline becomes:

```text
Large Document
      ↓
Text Splitter
      ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
...
```

---

# 🔄 Chunk Overlap

The project uses a chunk overlap of:

```text
200 characters
```

This means neighboring chunks share part of their content.

For example:

```text
Chunk 1
[--------------------]
              [--------]

                    Chunk 2
                    [--------------------]
```

Overlap can help preserve context when an important piece of information occurs near a chunk boundary.

---

# ⚙️ Current Chunking Configuration

| Parameter     |                  Current Value |
| ------------- | -----------------------------: |
| Chunk Size    |                           1000 |
| Chunk Overlap |                            200 |
| Splitter      | RecursiveCharacterTextSplitter |
| Input         |                  Text document |
| Output        |      LangChain Document chunks |

These values are intentionally simple so that the behavior of chunking can be studied before experimenting with more advanced strategies.

---

# 🧩 Why Chunking Matters

Chunking is one of the most important parts of a RAG pipeline.

Poor chunking can result in:

* Missing context
* Irrelevant retrieval
* Incomplete answers
* Poor semantic matching
* Increased token usage
* Lower retrieval quality

Good chunking can help:

* Preserve meaningful context
* Improve retrieval relevance
* Reduce unnecessary information
* Provide better context to the LLM

Therefore, this repository will experiment with different chunking approaches rather than treating chunking as a one-time configuration.

---

# 🏗️ Planned RAG Pipeline

The current project is only the beginning.

The planned architecture is:

```text
                ┌─────────────────┐
                │     Documents   │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ Document Loader │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │  Text Splitter  │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │    Embeddings   │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │  Vector Store   │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │    Retriever    │
                └────────┬────────┘
                         ↓
                  Relevant Context
                         ↓
                ┌─────────────────┐
                │       LLM       │
                └────────┬────────┘
                         ↓
                      Answer
```

---

# 🧪 RAG Experiments Planned

This repository is intended to contain multiple RAG experiments.

## Beginner RAG Projects

### 1. Personal Knowledge RAG

Create a RAG system that answers questions about personal information stored in text files.

Possible questions:

```text
What technologies does the person know?

What projects has the person built?

What is the person's education?

What are the person's career interests?
```

---

### 2. College Information RAG

Create a RAG system using college-related information.

Possible knowledge sources:

* College rules
* Courses
* Departments
* Examination information
* Library rules
* Admission information
* Campus facilities

---

### 3. FAQ RAG

Build a question-answering system using an FAQ dataset.

```text
Question
   ↓
Retriever
   ↓
Relevant FAQ
   ↓
LLM
   ↓
Answer
```

---

# 📚 Document-Based RAG Projects

The repository can later experiment with different document formats.

### Text RAG

```text
.txt
 ↓
TextLoader
 ↓
Chunks
 ↓
Embeddings
 ↓
Vector Store
```

### PDF RAG

```text
.pdf
 ↓
PDF Loader
 ↓
Chunks
 ↓
Embeddings
 ↓
Vector Store
```

### Multiple Document RAG

```text
PDF
TXT
DOCX
CSV
   ↓
Document Loaders
   ↓
Common Document Format
   ↓
Chunking
   ↓
Embeddings
```

---

# 🔬 Advanced RAG Experiments

As confidence improves, the repository will explore more advanced RAG techniques.

Potential experiments include:

* Different chunk sizes
* Different chunk overlaps
* Recursive chunking
* Semantic chunking
* Different embedding models
* Different vector databases
* Similarity search
* Maximum Marginal Relevance
* Metadata filtering
* Hybrid search
* Query transformation
* Query expansion
* Multi-query retrieval
* Reranking
* Context compression
* Parent-document retrieval
* Self-query retrieval
* Conversational RAG
* Multi-document RAG
* Agentic RAG

---

# 🤖 Local LLM Experiments

The project is also intended to explore local LLMs.

Ollama can be used to run compatible models locally.

The general architecture can become:

```text
User
 ↓
Question
 ↓
Retriever
 ↓
Relevant Documents
 ↓
Context
 ↓
Ollama
 ↓
Local LLM
 ↓
Answer
```

This allows experimentation with RAG without depending entirely on paid hosted LLM APIs.

---

# 🧠 RAG Concepts I Want to Understand

This repository is designed to help develop a deeper understanding of:

```text
Documents
   ↓
Loading
   ↓
Parsing
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Representation
   ↓
Vector Database
   ↓
Similarity Search
   ↓
Retrieval
   ↓
Context Construction
   ↓
Prompt
   ↓
LLM
   ↓
Answer
```

The goal is not simply to make the pipeline work.

The goal is to understand **why each stage exists and how changing one stage affects the final result**.

---

# 📊 RAG Experimentation Mindset

For each experiment, the following questions can be considered:

### Data

* What type of data am I using?
* How large is the dataset?
* Is the data clean?

### Chunking

* What chunk size should I use?
* Should chunks overlap?
* Should I use semantic chunking?

### Embeddings

* Which embedding model should I use?
* Does the embedding model understand my domain?

### Retrieval

* How many documents should be retrieved?
* Is similarity search enough?
* Should I use MMR?
* Should I use reranking?

### Generation

* Which LLM should generate the answer?
* How should the context be included in the prompt?
* How can hallucination be reduced?

### Evaluation

* Did the system retrieve the correct information?
* Is the answer grounded in the retrieved context?
* Are irrelevant documents being retrieved?

---

# 🛠️ Technologies

The project currently uses or is designed around the following technologies:

| Technology               | Purpose                           |
| ------------------------ | --------------------------------- |
| Python                   | Main programming language         |
| LangChain                | RAG application framework         |
| LangChain Community      | Document loading integrations     |
| LangChain Text Splitters | Document chunking                 |
| LangChain Core           | Core LangChain functionality      |
| Ollama                   | Local LLM experimentation         |
| PyPDF                    | PDF processing experiments        |
| python-dotenv            | Environment configuration         |
| uv                       | Python project/package management |

---

# 📦 Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project:

```bash
cd Rag
```

Create a virtual environment.

Using Python:

```bash
python -m venv rag
```

Activate it on Windows:

```bash
rag\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Current Project

## Document Loading

Run:

```bash
python project/data_loading.py
```

This loads:

```text
Data/about_me_sri_vardhan.txt
```

and prints the loaded document content.

---

## Document Chunking

Run:

```bash
python project/chunking.py
```

The script imports the loaded documents:

```python
from data_loading import docs
```

and splits them using:

```python
RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
```

The resulting chunks are printed individually.

---

# ⚠️ Windows File Path Note

When using Windows paths in Python, raw strings are recommended.

Use:

```python
r"M:\Rag\Data\about_me_sri_vardhan.txt"
```

instead of:

```python
"M:\Rag\Data\about_me_sri_vardhan.txt"
```

This prevents Python from interpreting sequences such as:

```text
\a
\t
\n
```

as escape characters.

---

# 🗂️ Suggested Future Project Structure

As more RAG projects are added, the repository can evolve into:

```text
Rag/
│
├── beginner/
│   ├── personal-rag/
│   ├── faq-rag/
│   └── college-rag/
│
├── intermediate/
│   ├── pdf-rag/
│   ├── multi-document-rag/
│   ├── conversational-rag/
│   └── metadata-rag/
│
├── advanced/
│   ├── hybrid-rag/
│   ├── reranking-rag/
│   ├── agentic-rag/
│   ├── multimodal-rag/
│   └── graph-rag/
│
├── Data/
│
├── requirements.txt
│
└── README.md
```

This structure can make the repository function as a personal RAG learning portfolio.

---

# 🎯 Learning Roadmap

```text
                    RAG JOURNEY
                         │
                         ↓
              ┌────────────────────┐
              │ RAG Fundamentals   │
              └─────────┬──────────┘
                        ↓
              ┌────────────────────┐
              │ Document Loading   │
              └─────────┬──────────┘
                        ↓
              ┌────────────────────┐
              │ Document Chunking  │
              └─────────┬──────────┘
                        ↓
              ┌────────────────────┐
              │     Embeddings     │
              └─────────┬──────────┘
                        ↓
              ┌────────────────────┐
              │   Vector Stores    │
              └─────────┬──────────┘
                        ↓
              ┌────────────────────┐
              │     Retrieval      │
              └─────────┬──────────┘
                        ↓
              ┌────────────────────┐
              │      Basic RAG     │
              └─────────┬──────────┘
                        ↓
              ┌────────────────────┐
              │ Advanced Retrieval │
              └─────────┬──────────┘
                        ↓
              ┌────────────────────┐
              │   Advanced RAG     │
              └─────────┬──────────┘
                        ↓
              ┌────────────────────┐
              │   Agentic RAG      │
              └─────────┬──────────┘
                        ↓
              ┌────────────────────┐
              │ Production RAG     │
              └────────────────────┘
```

---

# 🧪 Experiment Log

Each future RAG project can document:

```text
Project Name:
Problem:
Dataset:
Document Type:
Loader:
Chunking Strategy:
Chunk Size:
Chunk Overlap:
Embedding Model:
Vector Store:
Retriever:
LLM:
Prompt Strategy:
Evaluation Method:
Problems Encountered:
What I Learned:
Future Improvements:
```

This makes the repository useful not only as a coding project but also as a record of the RAG concepts learned through experimentation.

---

# 💡 What I Want to Learn From This Repository

By completing different projects, I want to understand:

* How RAG works internally
* How documents become retrievable knowledge
* How chunking affects retrieval
* How embeddings represent text
* How vector databases work
* How similarity search works
* How retrievers select context
* How LLMs use retrieved context
* How RAG differs from traditional LLM applications
* Why RAG systems sometimes produce incorrect answers
* How retrieval quality can be improved
* How RAG systems can be evaluated
* How different RAG architectures solve different problems

---

# 🚧 Current Status

### Completed

* [x] Project setup
* [x] RAG learning repository created
* [x] Text document added
* [x] Document loading implemented
* [x] Document chunking implemented
* [x] RecursiveCharacterTextSplitter configured
* [x] Chunk overlap experiment started

### In Progress

* [ ] Embeddings
* [ ] Vector store
* [ ] Similarity search
* [ ] Retriever
* [ ] LLM integration
* [ ] Basic question-answering RAG

### Planned

* [ ] PDF RAG
* [ ] Multi-document RAG
* [ ] Conversational RAG
* [ ] Metadata-based RAG
* [ ] Hybrid RAG
* [ ] Reranking
* [ ] Advanced retrieval
* [ ] Agentic RAG
* [ ] RAG evaluation
* [ ] Production-oriented RAG

---

# 📈 Project Philosophy

This repository is not intended to be a single finished RAG application.

It is a **learning laboratory for RAG**.

Every new project is an opportunity to answer questions such as:

> What happens if I change the chunk size?

> What happens if I change the embedding model?

> What happens if I use a different vector store?

> What happens if I retrieve more documents?

> What happens if I add reranking?

> What happens if the question requires information from multiple documents?

> What happens if the retrieved context is incorrect?

> What happens if the LLM does not have enough context?

These experiments will help develop practical intuition instead of relying only on theoretical knowledge.

---

# 🌱 Long-Term Goal

The long-term goal of this repository is to progress from:

```text
"I know what RAG is."
```

to:

```text
"I can build a RAG system."
```

and eventually:

```text
"I understand how to design, debug,
evaluate, and improve different RAG systems."
```

---

# 🏆 Expected Outcome

After completing multiple RAG projects, the intended outcome is a stronger understanding of:

```text
RAG Fundamentals
        +
Document Processing
        +
Chunking
        +
Embeddings
        +
Vector Databases
        +
Retrieval
        +
LLMs
        +
Prompt Engineering
        +
Evaluation
        +
Advanced Retrieval
        +
Agentic Workflows
```

This repository will serve as both a **learning environment and a portfolio of RAG experiments**.

---

# 👨‍💻 Author

**Sri Vardhan Jilla**

Computer Science and Engineering Student
AI / Machine Learning / Generative AI Enthusiast

### Profiles

GitHub:
https://github.com/jillasrivardhan

LinkedIn:
https://www.linkedin.com/in/jilla-srivardhan/

---

# ⭐ Final Note

This project is being developed with one main principle:

> **Don't just learn RAG. Build different RAG systems until you understand RAG.**

Every experiment in this repository represents another step toward becoming confident in designing and developing real-world Retrieval-Augmented Generation applications.

⭐ If this learning journey is useful to you, feel free to explore the projects, experiment with the code, and build your own RAG systems.
