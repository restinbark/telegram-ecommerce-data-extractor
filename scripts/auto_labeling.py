import pandas as pd
import re
import os
from nltk.tokenize import word_tokenize
from pathlib import Path

# --- Keyword Lists ---

products = [
    "Skechers", "Nike", "Adidas", "Colombia", "NB", "Puma", "Reebok", "Under", "Armour", "Converse", "Piclse", "Pristine",
    "LeBron", "Jordan", "Air", "Force", "Terrex", "bad", "bunny", "campus", "Delux", "Walker", "Alta", "buckle", "leather",
    "Ultra", "Lace", "Running", "cloud", "foam", "infinity", "flow", "Quantum", "flex", "Hiking", "Witness", "loafer", "loafers",
    "Chelsea", "boots", "suede", "Stay", "Loyal", "original", "bottle", "shoes", "shirt", "jacket", "Sandals", "Warm", "USB",
    "Heated", "Mug", "Blender", "Lunch", "Box", "Electric", "Saachi", "SONIFER", "Cup", "Pad", "Trey", "Rack", "Mattress",
    "Lids", "storage", "protector", "iron", "coaster"
]

locations = [
    "አድራሻ", "ሜክሲኮ", "ኮሜርስ", "ጀርባ", "መዚድ", "ፕላዛ", "የመጀመሪያ", "ደረጃ", "ባልቻ", "ሆስፒታል", "ቁጥር", "ህንፃ",
    "1ኛፎቅ", "114B", "ልደታ", "ወደ", "ባሉበት", "አህመድ", "አናስከፍልም", "ሲደርስ", "ቤት", "ቦታ", "ፀጋ", "ድሬዳዋ", "ሸዋ"
]

price_keywords = [
    "birr", "ብር", "Price", "ዋጋ", "ዋጋ፦", "price", "የአሽከርከሪ", "የሚሰጥ", "ከ1000ብር", "በ", "በብር", "በላይ"
]

location_prefixes = ["ቁጥር", "ፎቅ", "ህንፃ", "1ኛፎቅ", "2ኛፎቅ","እንደወጡ"]

# --- B/I Entity-Aware Labeling Function ---

def label_token(token, prev_token="", prev_label="O"):
    token = token.strip()

    # Contact number detection
    if re.fullmatch(r"(\+251|251)?9\d{8}", token) or token.startswith("09"):
        return "O"

    # Skip size patterns like 404142
    if re.fullmatch(r"(?:\d{2}){2,}", token):
        return "O"

    # --- Location ---
    if prev_label in {"B-LOC", "I-LOC"}:
        if re.fullmatch(r"\d{2,5}", token) or token in locations:
            return "I-LOC"
    if token in location_prefixes or token in locations:
        return "I-LOC"

    # --- Price ---
    if prev_label in {"B-PRICE", "I-PRICE"}:
        if re.fullmatch(r"\d{2,5}", token) or token in price_keywords:
            return "I-PRICE"
    if any(price_word in token for price_word in price_keywords) or re.fullmatch(r"\d{3,5}", token):
        return "B-PRICE"

    # --- Product ---
    if prev_label in {"B-Product", "I-Product"}:
        if token in products:
            return "I-Product"
    if token in products:
        return "B-Product"

    return "O"

# --- Setup Paths ---

folder_path = "data/processed/"
output_file = "data/ethio_ner_labels.conll"
Path(output_file).parent.mkdir(parents=True, exist_ok=True)

# --- Main Processing Loop ---

with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            filepath = os.path.join(folder_path, filename)
            print(f"📄 Processing: {filename}")
            df = pd.read_csv(filepath)

            for message in df['clean_text'].dropna().head(50):  # limit to 50 per file
                tokens = word_tokenize(str(message))
                prev_token = ""
                prev_label = "O"
                for token in tokens:
                    label = label_token(token, prev_token=prev_token, prev_label=prev_label)
                    outfile.write(f"{token} {label}\n")
                    prev_token = token
                    prev_label = label
                outfile.write("\n")  # message separator

print(f"\n✅ Done! Labeled data saved to: {output_file}")
