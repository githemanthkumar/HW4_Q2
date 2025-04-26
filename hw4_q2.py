import spacy

# Load the small English model
nlp = spacy.load("en_core_web_sm")

# Input sentence
sentence = "Barack Obama served as the 44th President of the United States and won the Nobel Peace Prize in 2009."

# Process the sentence
doc = nlp(sentence)

# Extract and print named entities
for ent in doc.ents:
    print(f"Entity Text: {ent.text}")
    print(f"Entity Label: {ent.label_}")
    print(f"Start Char: {ent.start_char}, End Char: {ent.end_char}")
    print("-")
