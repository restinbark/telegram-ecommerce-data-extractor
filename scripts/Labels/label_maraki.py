import pandas as pd

# Load cleaned data
df = pd.read_csv("data/processed/cleaned_marakibrand_messages.csv")

# Filter messages with at least 5 tokens
df = df[df['tokens'].apply(lambda x: len(eval(x)) >= 5)]

# Take first 50 for labeling
label_df = df.head(50)

# Save to text file
with open("marakibrand_labeling_template.conll", "w", encoding="utf-8") as f:
    for tokens in label_df['tokens']:
        for token in eval(tokens):
            f.write(f"{token} O\n")  # default label 'O', ready to be updated
        f.write("\n")  # separate messages

print("✅ Saved marakibrand_labeling template to labeling_template.conll")
