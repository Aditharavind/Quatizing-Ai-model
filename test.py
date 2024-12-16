from llama_cpp import Llama

# Load the quantized model (path to GGUF file)
model_path = "./quantized_model/bge-large-en-1.5.gguf"

# Initialize the Llama model
model = Llama(model_path=model_path)

# Example prompt to test
prompt = "What is the capital of France?"

# Generate a response from the model
response = model.generate(prompt)

print("Response:", response)
