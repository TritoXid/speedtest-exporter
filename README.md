<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="images/speedtest-exporter-logo.png">
    <img src="images/speedtest-exporter-logo.png" width="65%">
  </picture>
</p>

<p align="center">
  <a href="https://github.com/tritoxid/speedtest-exporter/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/tritoxid/speedtest-exporter/ci.yml?branch=main&logo=github" alt="Build Status" height="20"></a>
  <a href="https://github.com/tritoxid/speedtest-exporter/pkgs/container/speedtest-exporter"><img src="https://img.shields.io/github/v/tag/tritoxid/speedtest-exporter?logo=docker" alt="Docker Tag" height="20"></a>
</p>

A simple Prometheus exporter for [Speedtest CLI](https://www.speedtest.net/apps/cli) results.

This application runs the Speedtest CLI, collects the results, and pushes them to a Prometheus Pushgateway. This is useful for monitoring your internet connection speed over time.

## Usage

The easiest way to run the Speedtest Exporter is with Docker. The container is available on GHCR.

```bash
docker run -e PUSHGATEWAY_URL=<your-pushgateway-url> ghcr.io/tritoxid/speedtest-exporter
```

Replace `<your-pushgateway-url>` with the URL of your Prometheus Pushgateway. For example: `http://localhost:9091`.

The container will run the speedtest every time it is started. You can use a scheduler like `cron` or a systemd timer to run the container periodically.

### Environment Variables

* `PUSHGATEWAY_URL`: The URL of the Prometheus Pushgateway to push metrics to.

## Metrics

The following metrics are exported:

* `speedtest_download_bits_per_second`: Download speed in bits per second.
* `speedtest_upload_bits_per_second`: Upload speed in bits per second.
* `speedtest_ping_latency_ms`: Ping latency in milliseconds.
* `speedtest_jitter_ms`: Jitter in milliseconds.

## Development

To run the script locally, you need to have Python 3 and the Speedtest CLI installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/tritoxid/speedtest-exporter.git
   cd speedtest-exporter
   ```

2. Install the Python dependencies:
   ```bash
   pip install prometheus-client
   ```

3. Run the script:
   ```bash
   ./run_speedtest.py
   ```

   You can also set the `PUSHGATEWAY_URL` environment variable to push the metrics to your Pushgateway.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.
