import os
import zipfile
import pandas as pd
from nltk.tokenize import sent_tokenize
import nltk

# Download NLTK punkt tokenizer data
nltk.download('punkt')

# Extract the zipped folder
zip_folder_path ='/Users/aayush/Downloads/untitled folder.zip'
extract_folder_path = '/Users/aayush/Downloads/extracted_folder'
with zipfile.ZipFile(zip_folder_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder_path)

#list of CSV files 
csv_files = [file for file in os.listdir(extract_folder_path) if file.endswith('.csv')]

# Create a list 
all_text = []

for csv_file in csv_files:
    file_path = os.path.join(extract_folder_path, csv_file)

    df = pd.read_csv(file_path)

    # yesma chai jun column ko data tanni ho tae column ko name lekh.
    large_text_column = 'large_text_column'
    # Concatenate the texts 
    all_text.extend(df[large_text_column].dropna().tolist())

# Join the texts into a single string
merged_text = ' '.join(all_text)

# Tokenize the text into sentences using NLTK
sentences = sent_tokenize(merged_text)

# Save the sentences to a text file
output_txt_file = 'output_text.txt'
with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
    for sentence in sentences:
        txt_file.write(sentence + '\n')

print(f'Text extracted and saved to {output_txt_file}')
