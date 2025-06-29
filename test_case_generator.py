from granite_model import tokenizer, model, device

def generate_tests(code):
    prompt = f"Write test cases for this code:\n{code}"
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_new_tokens=150)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)