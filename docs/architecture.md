# System Architecture
## Drug Interaction Knowledge Graph with RAG

---

# 1. Architecture Overview

The system consists of four major components:

1. Data ingestion
2. Knowledge graph construction
3. Retrieval-Augmented Generation pipeline
4. Interactive visualization

---

# 2. High-Level Architecture Diagram

```mermaid
flowchart TD

A[Biomedical Literature
Research Papers] --> C[Data Processing Layer]
B[Drug Interaction Datasets
DrugBank / SIDER] --> C

C --> D[Entity Extraction
NER and Normalization]

D --> E[Relationship Extraction
LLM or NLP]

E --> F[Knowledge Graph Builder]

F --> G[Graph Database
Neo4j]

G --> H[Graph Query Engine]

C --> I[Text Chunking]

I --> J[Embedding Model]

J --> K[Vector Database]

K --> L[RAG Retrieval System]

G --> M[API Layer]

L --> M

M --> N[Interactive Graph Visualization]

N --> O[User Interface]
