import pandas as pd
import re
import emoji
import string
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Optional: for Amharic-specific cleanup, you could later use `camel_tools` or similar libs.

# Load raw Telegram data
df = pd.read_csv("ethio_brand_collection_telegram_messages.csv")

# Function to remove emojis
def remove_emojis(text):
    return emoji.replace_emoji(text, replace='')

# Function to remove punctuation and normalize spacing
def clean_text(text):
    text = str(text)
    text = remove_emojis(text)
    text = re.sub(r"[{}]".format(string.punctuation), "", text)  # remove punctuation
    text = re.sub(r"\s+", " ", text)  # normalize spaces
    text = text.strip()
    return text

# Function to tokenize Amharic (basic using NLTK)
def tokenize_amharic(text):
    return word_tokenize(text)

# Apply preprocessing
df['clean_text'] = df['text'].apply(clean_text)
df['tokens'] = df['clean_text'].apply(tokenize_amharic)

# Save cleaned version
df.to_csv("cleaned_ethio_brand_collection_messages.csv", index=False)

print("✅ Preprocessing complete! Saved to cleaned_ethio_brand_collection_messages.csv")
