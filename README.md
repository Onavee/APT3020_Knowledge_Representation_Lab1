#  Medical Expert System
### Knowledge Representation Lab — Rule-Based Inference Engine


## Overview

A simple **rule-based expert system** that infers possible illnesses from a set of patient-reported symptoms. The system demonstrates core AI concepts in Knowledge Representation:

- **Facts** — symptoms and diseases stored in a structured knowledge base
- **Rules** — IF–THEN production rules encoding medical heuristics
- **Inference** — forward-chaining to match symptoms against rules
- **Semantic Network** — a graphical representation of relationships between patients, symptoms, and diseases


###  Knowledge Base Design

The knowledge base is stored in [`knowledge_base.json`](knowledge_base.json) and contains:

| Component | Contents |
|-----------|----------|
| **Symptoms** | Fever, Headache, Cough, Chest Pain, Sneezing, Runny Nose, Fatigue, Sore Throat, Vomiting, Diarrhea |
| **Diseases** | Malaria, Pneumonia, Flu, Food Poisoning |
| **Rules** | 4 IF–THEN production rules (R1–R4) |
| **Facts** | Domain metadata, version, disclaimer |

###  Rule-Based Inference System

The CLI engine is implemented in [`KR.py`](KR.py).

**Inference Rules:**

| Rule | Conditions (IF) | Diagnosis (THEN) |
|------|-----------------|------------------|
| R1   | Fever ∧ Headache ∧ Fatigue | Malaria |
| R2   | Cough ∧ Chest Pain ∧ Fatigue | Pneumonia |
| R3   | Sneezing ∧ Runny Nose ∧ Sore Throat | Flu |
| R4   | Vomiting ∧ Diarrhea ∧ Fatigue | Food Poisoning |


###  Semantic Network Diagram

The semantic network is saved as an SVG at [`semantic_network.png`](semantic_network.png).

It models three entity types and their relationships:

```
[Patient] ──has_symptom──▶ [Symptom] ──indicates──▶ [Disease]
```

- 
- **Symptom nodes** (rounded rectangles, amber) — the 10 possible symptoms
- **Disease nodes** (Rectangles, ) — the 4 diagnosable conditions


## How the Inference Engine Works

The system uses **forward chaining**:

1. The patient's reported symptoms form the **working memory** (fact base).
2. Each rule's `IF` conditions are checked against working memory.
3. If **all conditions** of a rule are satisfied, the rule **fires** and the disease is added to the conclusions.
4. All fired rules are reported — multiple diagnoses are possible if symptoms overlap.

```
Working Memory: {Fever, Headache, Fatigue}

R1: Fever ∧ Headache ∧ Fatigue → ✔ FIRES → Malaria
R2: Cough ∧ Chest Pain ∧ Fatigue → ✘ (Cough, Chest Pain absent)
R3: Sneezing ∧ Runny Nose ∧ Sore Throat → ✘
R4: Vomiting ∧ Diarrhea ∧ Fatigue → ✘ (Vomiting, Diarrhea absent)

Conclusion: Malaria
```

---

