import io
import time
from flask import Flask, Response
from pydub import AudioSegment

app = Flask(__name__)

# Audio-Einstellungen
SAMPLE_RATE = 44100  # 44,1 kHz
CHANNELS = 2  # Stereo
DURATION_MS = 200  # Dauer pro Block in Millisekunden

def generate_audio():
    """Erzeugt einen MP3-Stream aus stiller Audiodatei."""
    while True:
        # Erzeuge Stille (mit 0 Amplitude)
        silence = AudioSegment.silent(duration=DURATION_MS, frame_rate=SAMPLE_RATE)

        # Exportiere als MP3
        byte_io = io.BytesIO()
        silence.export(byte_io, format="mp3", bitrate="128k")
        byte_io.seek(0)
        chunk = byte_io.read()

        yield chunk
        time.sleep(DURATION_MS / 1000.0)  # Wartezeit in Sekunden für kontinuierliches Streaming

@app.route('/stream')
def stream_audio():
    """Streamt den Audio-Stream als MP3."""
    return Response(generate_audio(), mimetype="audio/mpeg")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True)
