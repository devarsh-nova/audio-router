import sounddevice as sd
import soundfile as sf
import threading

input_device = None  # Use default
output_devices = []  # Add device indexes here (you can use sd.query_devices())

def list_devices():
    print("Available audio devices:")
    print(sd.query_devices())

def callback(indata, frames, time, status):
    if status:
        print(status)
    for stream in output_streams:
        stream.write(indata)

if __name__ == "__main__":
    list_devices()
    # Example: add output devices manually here
    output_devices.extend([3, 5])  # <- Replace with your output device indices

    samplerate = 44100
    channels = 2

    output_streams = []
    for dev in output_devices:
        stream = sd.OutputStream(device=dev, samplerate=samplerate, channels=channels)
        stream.start()
        output_streams.append(stream)

    with sd.InputStream(callback=callback, channels=channels, samplerate=samplerate, device=input_device):
        print("Routing audio... press Ctrl+C to stop.")
        threading.Event().wait()
