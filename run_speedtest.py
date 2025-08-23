#!/usr/bin/env python3
import subprocess
import sys
import os
import json
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

def run_speedtest():
    """Runs the speedtest command and pushes metrics to Prometheus Pushgateway."""
    try:
        command = ["speedtest", "--accept-license", "--accept-gdpr", "--format=json"]
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )
        
        # Print the JSON output to stdout
        print(result.stdout)

        # Push metrics to Prometheus Pushgateway if PUSHGATEWAY_URL is set
        pushgateway_url = os.environ.get("PUSHGATEWAY_URL")
        if pushgateway_url:
            try:
                data = json.loads(result.stdout)
                registry = CollectorRegistry()
                
                g = Gauge('speedtest_download_bits_per_second', 'Download speed in bits per second', registry=registry)
                g.set(data['download']['bandwidth'] * 8)

                g = Gauge('speedtest_upload_bits_per_second', 'Upload speed in bits per second', registry=registry)
                g.set(data['upload']['bandwidth'] * 8)

                g = Gauge('speedtest_ping_latency_ms', 'Ping latency in milliseconds', registry=registry)
                g.set(data['ping']['latency'])

                g = Gauge('speedtest_jitter_ms', 'Jitter in milliseconds', registry=registry)
                g.set(data['ping']['jitter'])

                push_to_gateway(pushgateway_url, job='speedtest', registry=registry)
                print(f"Successfully pushed metrics to {pushgateway_url}", file=sys.stderr)

            except Exception as e:
                print(f"Error pushing metrics to Prometheus Pushgateway: {e}", file=sys.stderr)


    except FileNotFoundError:
        print("Error: 'speedtest' command not found. Please make sure it's installed and in your PATH.", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error running speedtest: {e}", file=sys.stderr)
        print(f"Stderr: {e.stderr}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_speedtest()
