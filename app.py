# 4. Verification and Configuration
# Ensure the conversion was successful by checking the file sizes of the original and quantized models:

import os
# Quantized model file size
file_path_quantized = './quantized_model/bge-large-en-1.5.gguf'
if os.path.exists(file_path_quantized):
    file_size_quantized = os.stat(file_path_quantized).st_size
    file_size_gb_quantized = file_size_quantized / (1024 * 1024 * 1024)
    print(f"Size of '{file_path_quantized}': {file_size_quantized} bytes ({file_size_gb_quantized:.2f} GB)")
else:
    print(f"File '{file_path_quantized}' not found.")
# Original model file size
file_path_original = './original_model/onnx/model.onnx'
if os.path.exists(file_path_original):
    file_size_original = os.stat(file_path_original).st_size
    file_size_gb_original = file_size_original / (1024 * 1024 * 1024)
    print(f"Size of '{file_path_original}': {file_size_original} bytes ({file_size_gb_original:.2f} GB)")
else:
    print(f"File '{file_path_original}' not found.")
