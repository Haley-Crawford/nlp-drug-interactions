# Knowledge Graph Schema
## Drug Interaction Knowledge Graph

---

# 1. Overview

The knowledge graph represents relationships between drugs, their interactions, side effects, and patient risk factors. The graph structure enables efficient exploration of complex relationships and supports integration with a Retrieval-Augmented Generation (RAG) pipeline.

The graph contains three primary node types and several relationships that describe pharmacological interactions.

---

# 2. Node Types

## Drug

Represents a pharmaceutical compound or medication.

Properties:

- drug_id
- name
- drug_class
- mechanism_of_action
- source

Example:

Drug
name: Warfarin  
class: Anticoagulant  
mechanism_of_action: Vitamin K antagonist

---

## SideEffect

Represents an adverse drug reaction.

Properties:

- effect_id
- name
- severity
- frequency

Example:

SideEffect  
name: Bleeding  
severity: High

---

## PatientFactor

Represents patient characteristics that influence drug interactions.

Examples include:

- Age groups
- Medical conditions
- Pregnancy
- Genetic factors
- Organ impairment

Properties:

- factor_id
- description
- category

Example:

PatientFactor  
description: Age > 65  
category: Age-related risk

---

# 3. Relationship Types

## Drug Interaction

Represents an interaction between two drugs.

Relationship:

Drug → INTERACTS_WITH → Drug

Properties:

- severity
- mechanism
- evidence_source

Example:

Warfarin → INTERACTS_WITH → Ibuprofen  
severity: severe  
mechanism: increased bleeding risk

---

## Drug Causes Side Effect

Represents adverse reactions associated with a drug.

Relationship:

Drug → CAUSES → SideEffect

Properties:

- frequency
- evidence_level

Example:

Warfarin → CAUSES → Bleeding

---

## Drug Risk Factors

Represents patient conditions that increase the likelihood of adverse effects.

Relationship:

Drug → HIGH_RISK_FOR → PatientFactor

Example:

Warfarin → HIGH_RISK_FOR → Age > 65

---

# 4. Graph Representation

Example subgraph:

```mermaid
graph TD

Warfarin[Drug: Warfarin]
Ibuprofen[Drug: Ibuprofen]
Bleeding[SideEffect: Bleeding]
Elderly[PatientFactor: Age > 65]

Warfarin -->|INTERACTS_WITH| Ibuprofen
Warfarin -->|CAUSES| Bleeding
Bleeding -->|HIGH_RISK_FOR| Elderly
