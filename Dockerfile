# Debian bookworm
FROM debian:12.11-slim

# Install curl to download the Speedtest CLI
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    ca-certificates \
    python3

# Download and extract the Speedtest CLI
RUN curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | bash && \
    apt-get update && \
    apt-get install -y speedtest && \
    rm -rf /var/lib/apt/lists/*

# Copy the python script
COPY run_speedtest.py /usr/local/bin/run_speedtest.py

# Set the entrypoint to the python script
ENTRYPOINT ["/usr/local/bin/run_speedtest.py"]
