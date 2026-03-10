# 1. Install mini-swe-agent
pip install -e submodules/swe-bench-pro/mini-swe-agent

# 2. Generate a CSV for one instance
python3 make_dataset.py
"

# 3. Run mini-swe-agent on that instance
mini swebench \
  --model claude-sonnet-4-6 \
  --instances /workspace/results/smoke_sample.csv \
  --output_dir /workspace/results/smoke_trajs

# 4. Gather the .pred file into patches.json
python3 submodules/swe-bench-pro/helper_code/gather_patches.py \
  --directory /workspace/results/smoke_trajs \
  --prefix smoke_001 \
  --output /workspace/results/smoke_patches.json

# 5. Score it
python3 submodules/swe-bench-pro/swe_bench_pro_eval.py \
  --raw_sample_path /workspace/results/smoke_sample.csv \
  --patch_path /workspace/results/smoke_patches.json \
  --output_dir /workspace/results/smoke_eval \
  --dockerhub_username jefzda \
  --scripts_dir submodules/swe-bench-pro/run_scripts \
  --use_local_docker

---

row['problem_statement']   # the issue text
row['instance_id']         # the identifier
row['dockerhub_tag']       # the Docker image with the repo pre-loaded
```

## What `ail`'s integration point looks like
```
for each instance:
  1. pull jefzda/sweap-images:<dockerhub_tag>
  2. start container
  3. feed problem_statement to ail
  4. ail runs its pipeline inside the container (bash, edit files, run tests)
  5. ail outputs a git diff
  6. write diff to results/<instance_id>/<instance_id>.pred
gather_patches.py → patches.json → swe_bench_pro_eval.py