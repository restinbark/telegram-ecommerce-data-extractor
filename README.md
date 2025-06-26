# 📦 Amharic NER System for Telegram-Based E-commerce (EthioMart Project)

A multilingual Named Entity Recognition (NER) system fine-tuned for Amharic Telegram messages — built to extract key e-commerce entities such as **Product**, **Price**, and **Location**. This project supports EthioMart’s goal of centralizing fragmented vendor activity into a unified digital platform.

---

## 🚀 Project Overview

**Challenge**: Telegram is the dominant channel for informal e-commerce in Ethiopia. Vendors operate in scattered channels, and customers struggle to search or compare products.

**Solution**: We built a custom Amharic NER model that extracts structured data from unstructured Telegram messages using open-source LLMs like `xlm-roberta-base` and `bert-base-multilingual-cased`.

---

## ✅ Tasks Completed

### 🔹 Task 1: Data Ingestion & Preprocessing

- Connected to 5+ Telegram vendor channels using Telethon.
- Scraped messages and metadata.
- Cleaned Amharic text and stored in structured format.

**Outputs**:
```bash
data/raw/
data/processed/
scripts/auth/
scripts/prep/
🔹 Task 2: Entity Labeling in CoNLL Format
Manually labeled 50+ messages.

Developed auto_labeling.py to automate BIO tagging using keyword lists.

Saved all labels in data/ethio_ner_labels.conll.

Key Tags:

B-Product, B-PRICE, B-LOC, I-PRICE, I-LOC, O

🔹 Task 3: Model Fine-Tuning (XLM-Roberta)
Used Hugging Face Trainer to fine-tune xlm-roberta-base.

Token-label alignment using word_ids().

Trained on GPU with validation evaluation.

Results:

Metric	Score
F1 Score	0.82
Precision	0.83
Recall	0.81
Accuracy	0.85

✅ Saved and pushed model to Hugging Face Hub.

🔹 Task 4: Model Comparison & Selection
Trained a second model: bert-base-multilingual-cased (mBERT)
Reused dataset and evaluation code for apples-to-apples comparison.

Comparison:

Model	F1 Score	Precision	Recall	Accuracy
xlm-roberta-base	0.82	0.83	0.81	0.85
bert-base-multilingual-cased	0.76	0.78	0.74	0.80

✅ Recommendation: Use XLM-Roberta for deployment — better generalization and accuracy for Amharic entity extraction.

📂 Repository Structure
bash
Copy
Edit
├── data/
│   ├── raw/
│   ├── processed/
│   ├── ethio_ner_labels.conll
│   └── labeling_templates/
│
├── scripts/
│   ├── auth/                # Telegram channel auth
│   ├── prep/                # Text preprocessing
│   ├── auto_labeling.py     # Rule-based entity tagger
│   ├── tokenizer.py         # Token-label alignment
│   ├── train_ner_model.py   # Hugging Face Trainer
│
├── results/                 # Saved models & logs
├── README.md
💬 Business Impact
Enables real-time product tracking from Telegram

Supports filtering by price & location

Foundation for recommendation systems & search

📊 Visualization Suggestion
Bar chart of F1 score comparison

Table of predicted entities (manual test)

Power BI dashboard (optional): Top products, frequent locations

🧠 Challenges Faced
Challenge	Solution
Transformers version mismatch	Reinstalled latest libs, restarted Colab
Overlapping prices vs sizes	Regex refinement and keyword filtering
Git mismanagement	Recreated clean branches: task-1, task-2, task-3
Colab memory resets	Modularized notebook with repeatable blocks

🔗 Links
🤗 Hugging Face Model: restin7bark/xlm-roberta-base-amharic-ner

📓 Training Notebook: https://colab.research.google.com/drive/1gNxFlWDYQuYBsY7DpuPrNZ0fJ3nVHMxv?usp=sharing
