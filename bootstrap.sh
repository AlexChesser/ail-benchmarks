#!/bin/bash
set -euo pipefail

echo "=== Building ail-benchmarks dev environment ==="
docker compose -f docker/docker-compose.yml build \
  --build-arg HF_TOKEN=$(grep HF_TOKEN ./.env | cut -d= -f2)

# Start the container in the background if not already running
docker compose -f docker/docker-compose.yml up -d

# Shell into it
docker compose -f docker/docker-compose.yml exec ail-benchmarks bash
