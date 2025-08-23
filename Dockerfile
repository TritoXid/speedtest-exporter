# Debian bookworm
FROM debian:12.11-slim

# Install curl to download the Speedtest CLI
RUN apt-get update && apt-get install -y curl gnupg ca-certificates && \
    curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | bash && \
    apt-get install -y python3-venv speedtest && \
    rm -rf /var/lib/apt/lists/*

# Install prometheus-client
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir prometheus-client

# Copy the python script
COPY run_speedtest.py /usr/local/bin/run_speedtest.py

# Set the entrypoint to the python script
ENTRYPOINT ["/usr/local/bin/run_speedtest.py"]
