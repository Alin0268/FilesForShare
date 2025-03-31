import os
from pydub import AudioSegment
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
import wave
import contextlib

def analyze_mp3(file_path):
    audio = AudioSegment.from_mp3(file_path)
    info = MP3(file_path)

    print("===== The MP3 File INFO =====")
    print(f"Duration: {info.info.length:.2f} sec")
    print(f"Bitrate: {info.info.bitrate / 1000} kbps")
    print(f"Sampling rate: {info.info.sample_rate} Hz")
    print(f"Channels: {info.info.channels}")
    num_frames = int(info.info.length * info.info.sample_rate / 1152)
    print(f"Estimated number of frames: {num_frames}")

    print("\n===== ID3 Metadata =====")
    try:
        tags = ID3(file_path)
        for tag in tags.values():
            print(f"{tag.FrameID}: {tag.text}")
    except Exception as e:
        print("No ID3 tags or failed to read.")

    print("\n===== Physical Parameters =====")
    print(f"File size: {round(os.path.getsize(file_path) / 1024, 2)} KB")
    print(f"Duration (via Pydub): {audio.duration_seconds} sec")
    print(f"Sampling rate: {audio.frame_rate} Hz")
    print(f"Channels: {audio.channels}")
    print(f"Bit depth: {audio.sample_width * 8} bit")
    print(f"Format: {audio.sample_width}-byte PCM")

    
analyze_mp3("audio_66s_128kbps.mp3")



