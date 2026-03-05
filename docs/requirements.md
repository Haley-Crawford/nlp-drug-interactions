# System Requirements
## Drug Interaction Knowledge Graph with RAG

## 1. Project Overview

This project will develop a system that integrates biomedical datasets and scientific literature to construct a **knowledge graph of drug interactions, side effects, and patient risk factors**.  

The system will use **Retrieval-Augmented Generation (RAG)** to extract knowledge from biomedical literature and combine it with structured datasets. The resulting knowledge graph will allow users to explore drug interactions and visualize relationships through an interactive interface.

---

# 2. Functional Requirements

## 2.1 Data Ingestion

The system must:

- Import drug interaction datasets
- Import drug side-effect datasets
- Retrieve biomedical literature
- Process structured and unstructured biomedical data

Supported sources include:

- Drug interaction databases
- Side-effect datasets
- Biomedical research papers
- Clinical literature repositories

---

## 2.2 Document Processing

The system must:

- Convert biomedical documents into machine-readable text
- Split documents into smaller semantic chunks
- Store chunks for retrieval
- Extract entities including:

  - Drug names
  - Side effects
  - Patient risk factors
  - Interaction descriptions

---

## 2.3 Knowledge Graph Construction

The system must construct a knowledge graph containing:

### Node Types

- Drug
- SideEffect
- PatientFactor

### Relationships

- Drug → interacts_with → Drug
- Drug → causes → SideEffect
- Drug → high_risk_for → PatientFactor

The system must also:

- Remove duplicate nodes
- Normalize entity names
- Associate evidence sources with relationships

---

## 2.4 RAG Retrieval System

The system must support:

- Embedding biomedical document chunks
- Storing embeddings in a vector database
- Retrieving relevant literature passages for queries
- Providing context to a language model

---

## 2.5 Graph Query System

Users must be able to:

- Search for a drug
- View interacting drugs
- View possible side effects
- Identify patient risk factors
- Trace interaction pathways

---

## 2.6 Visualization

The system must provide an **interactive visualization of the knowledge graph**.

Features include:

- Node-based graph exploration
- Clickable nodes
- Expandable relationships
- Visual differentiation between entity types

Example color scheme:

- Drug → Blue
- SideEffect → Red
- PatientFactor → Green

---

# 3. Non-Functional Requirements

## Performance

The system should:

- Support efficient graph queries
- Retrieve relevant documents quickly
- Render graph visualizations interactively

---

## Scalability

The system should allow:

- Integration of new datasets
- Expansion of the knowledge graph
- Addition of new biomedical literature sources

---

## Usability

The visualization should:

- Allow intuitive navigation
- Clearly display relationships
- Support interactive exploration

---

# 4. Deliverables

The final project will include:

- Knowledge graph database
- RAG retrieval pipeline
- Graph visualization system
- Documentation of architecture and methodology
