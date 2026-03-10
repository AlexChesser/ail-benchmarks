from datasets import load_dataset
import csv, json
from pathlib import Path

ds = load_dataset('ScaleAI/SWE-bench_Pro', split='test')
row = next(r for r in ds if r['instance_id'] == 'instance_NodeBB__NodeBB-04998908ba6721d64eba79ae3b65a351dcfbc5b5-vnan')

Path('/workspace/results').mkdir(parents=True, exist_ok=True)

with open('/workspace/results/smoke_sample.csv', 'w') as f:
    w = csv.DictWriter(f, fieldnames=row.keys())
    w.writeheader()
    w.writerow(row)
print('CSV written')