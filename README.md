# Audio Router

A simple Python tool to route audio from an input device to multiple output devices on Windows.

## Requirements
- Python 3.8+
- `sounddevice`
- `soundfile`

## How to Use

1. Install requirements:
    ```
    pip install -r requirements.txt
    ```

2. Edit `main.py` and replace `output_devices` with the correct device indexes from your system.

3. Run:
    ```
    python main.py
    ```

Use `sd.query_devices()` to see available device indices.
