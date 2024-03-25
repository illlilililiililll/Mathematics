import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import wavio
import time

CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
OUTPUT_FILENAME = "Fourier.wav"

audio = pyaudio.PyAudio()

stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK_SIZE
)

print("Recording...")

frames = []

try:
    while True:
        data = stream.read(CHUNK_SIZE)
        frames.append(np.frombuffer(data, dtype=np.int16))

except KeyboardInterrupt:
    print("Recording stopped.")

stream.stop_stream()
stream.close()
audio.terminate()


audio_data = np.concatenate(frames, axis=0)

start_time_sec = 0.3 

# start ~ end
start_sample = int(start_time_sec * RATE)

cropped_audio_data = audio_data[start_sample:]

# .wav export
wavio.write(OUTPUT_FILENAME, audio_data, RATE, sampwidth=2)

print(f"Audio saved as '{OUTPUT_FILENAME}'.")

n = len(cropped_audio_data)
k = np.arange(n)
Fs = 1 / 0.001
T = n / Fs
freq = k / T
freq = freq[range(int(n / 2))]

Y = np.fft.fft(cropped_audio_data) / n
Y = Y[range(int(n / 2))]

fig, ax = plt.subplots(2, 1, figsize=(12, 8))
time = np.arange(0, len(cropped_audio_data)) * (1.0 / RATE)
ax[0].plot(time, cropped_audio_data)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[0].grid(True)
ax[1].plot(freq, abs(Y), 'r', linestyle=' ', marker='^')
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
ax[1].vlines(freq, [0], abs(Y))
ax[1].set_xlim([0, 20])
ax[1].grid(True)

plt.show()