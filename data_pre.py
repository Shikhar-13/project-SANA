from pdfminer.high_level import extract_text
text = extract_text('')
arr = text.split('\n')
def preprocess_text(text):
    # Remove leading and trailing whitespace
    text = text.strip()
    # Remove multiple spaces
    text = ' '.join(text.split())
    return text