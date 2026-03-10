# run.sh
#!/bin/bash
set -euo pipefail

# Start the container in the background if not already running
docker compose -f docker/docker-compose.yml up -d

# Shell into it
docker compose -f docker/docker-compose.yml exec ail-benchmarks bash