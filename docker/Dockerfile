FROM python:3.11-slim

ENV TERM=xterm-256color
ENV FORCE_COLOR=1
ARG HF_TOKEN
ENV HF_TOKEN=${HF_TOKEN}

RUN echo 'export PS1="\[\033[01;32m\]ail-benchmarks\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]# "' >> /root/.bashrc

# Install system deps
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    pkg-config \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js (for claude CLI)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Install Claude CLI globally
RUN npm install -g @anthropic-ai/claude-code

# Install Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Install Docker CLI only (not daemon)
RUN curl -fsSL https://download.docker.com/linux/static/stable/x86_64/docker-27.5.1.tgz \
    | tar -xz --strip=1 -C /usr/local/bin docker/docker

WORKDIR /workspace

# Install Python deps
COPY submodules/swe-bench-pro/requirements.txt /tmp/swe-bench-requirements.txt
RUN pip install -r /tmp/swe-bench-requirements.txt

COPY ./download_dataset.py .
RUN python3 download_dataset.py

CMD ["bash"]