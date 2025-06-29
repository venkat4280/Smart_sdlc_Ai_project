from granite_model import tokenizer, model, device

def summarize_code(code):
    prompt = f"Summarize this code:\n{code}"
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_new_tokens=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)