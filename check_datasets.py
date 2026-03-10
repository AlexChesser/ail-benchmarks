from datasets import load_dataset
ds = load_dataset('ScaleAI/SWE-bench_Pro', split='test')
print(f'✓ {len(ds)} instances ready')
print(ds[0]['instance_id'])