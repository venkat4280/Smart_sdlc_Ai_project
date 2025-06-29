from granite_model import tokenizer, model, device
import fitz  # PyMuPDF
import torch

def extract_and_classify(pdf_file):
    # Open and extract text from PDF
    doc = fitz.open(pdf_file.name)
    full_text = ""
    for page in doc:
        full_text += page.get_text()

    # Create prompt
    prompt = f"Extract user stories from this requirement:\n{full_text}"
    
    # Generate response from model
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_new_tokens=300)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
