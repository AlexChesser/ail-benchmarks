from datasets import load_dataset
from pathlib import Path

ds = load_dataset('ScaleAI/SWE-bench_Pro', split='test')
subset = ds.filter(lambda r: r['instance_id'] == 'instance_NodeBB__NodeBB-04998908ba6721d64eba79ae3b65a351dcfbc5b5-vnan')

Path('/workspace/results/smoke_subset').mkdir(parents=True, exist_ok=True)
subset.to_parquet('/workspace/results/smoke_subset/data.parquet')