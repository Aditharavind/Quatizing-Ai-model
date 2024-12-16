# 2. Download and Prepare the Model
# Begin by fetching a pre-trained model from the Hugging Face Hub. For demonstration, let’s use a model named bge-large-en-v1.5:

import os
from huggingface_hub import snapshot_download

model_name = "BAAI/bge-large-en-v1.5"
base_model_dir = "./original_model/"
# Download the model
snapshot_download(repo_id=model_name, local_dir=base_model_dir, local_dir_use_symlinks=False)
