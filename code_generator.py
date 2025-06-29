from granite_model import tokenizer, model, device

def generate_code(story, language):
    prompt = f"Write {language} code for: {story}"
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_new_tokens=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
