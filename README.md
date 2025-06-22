# Telegram E-commerce Extractor (EthioMart NER Project)

This project is part of Tenx Week 4 challenge and aims to develop an Amharic Named Entity Recognition (NER) system to support EthioMart's goal of building a centralized e-commerce platform based on Telegram data.

## 🔍 Project Objective

To fine-tune large language models (LLMs) for extracting key business entities from Amharic-language messages posted in Telegram e-commerce channels. The project consists of 6 tasks, from data ingestion to model interpretability and vendor analytics.

## ✅ Completed Tasks

### Task 1: Data Ingestion and Preprocessing
- Developed Python scripts using **Telethon** to scrape messages from 5+ active Amharic Telegram e-commerce channels.
- Collected over 500 messages including:
  - Text content
  - Views
  - Sender IDs
  - Timestamps
- Cleaned and tokenized Amharic text using `nltk`, `emoji`, and `re` libraries.
- Organized data into raw and processed formats for further use.

### Task 2: CoNLL Labeling for NER
- Selected 50 representative Telegram messages with clearly defined product, price, and location mentions.
- Manually labeled these messages in **CoNLL format** using entity tags:
  - `B-Product`, `I-Product`
  - `B-PRICE`, `I-PRICE`
  - `B-LOC`, `I-LOC`
- Saved the labeled dataset as `ethio_ner_labels.conll`.

## 📁 Project Structure

telegram-ecommerce-extractor/
├── data/
│ ├── raw/
│ ├── processed/
│ │ └── ethio_ner_labels.conll/
├── scripts/
│ ├── auth/
│ ├── prep/
│ └── preprocess_amharic.py
├── README.md


## 🔜 Upcoming Tasks

- **Task 3**: Fine-tune multilingual models (XLM-Roberta, mBERT, BERT-Tiny-Amharic) using Hugging Face Transformers.
- **Task 4**: Compare model performance (F1, Precision, Recall).
- **Task 5**: Apply SHAP and LIME for interpretability.
- **Task 6**: Build Vendor Scorecard using NER + metadata.

## 🚀 Tools Used
- Python, Pandas, NLTK
- Telethon
- Hugging Face Transformers
- Google Colab (for GPU support)

---

## 👥 Maintainer
This project is developed by a solo contributor for Tenx Platform’s EthioMart NER challenge.
