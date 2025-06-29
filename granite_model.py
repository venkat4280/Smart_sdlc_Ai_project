# granite_model.py

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load from Hugging Face directly (Colab will cache it)
model_name = "ibm-granite/granite-3.3-2b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
