import os
from datasets import load_dataset

token = os.environ.get('HF_TOKEN')
if not token:
    raise Exception('HF_TOKEN build arg required. Pass with: docker compose build --build-arg HF_TOKEN=hf_...')

print("Downloading SWE-bench Pro dataset...")
ds = load_dataset('ScaleAI/SWE-bench_Pro', split='test')
print(f'✓ Downloaded {len(ds)} instances')