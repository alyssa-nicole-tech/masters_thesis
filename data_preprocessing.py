#Extract the Youtube Video-----> audio/transcript/metadata
#Load that extracted data into your preprocessing routine
  #yt_dlp-->metadata + audio
  #youtube_transcript_api

#ETL Extractor Routine
import os
from yt_dlp import YoutubeDL
from youtube_transcript_api import YouTubeTranscriptApi

def extract_youtube(url, output_dir="data/raw"):
    """
    Extract metadata, audio, and transcript from a YouTube video.
    Returns a dictionary containing all extracted components.
    """
    os.makedirs(output_dir, exist_ok=True)

    # --- 1. Extract metadata + audio ---
    ydl_opts = {
        "quiet": True,
        "format": "bestaudio/best",
        "outtmpl": f"{output_dir}/%(id)s.%(ext)s"
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    video_id = info["https://youtu.be/QeJAdlV4fXM?si=cmAfZBnOtW0da_Y3"]
    audio_path = f"{output_dir}/{video_id}.webm"

    # --- 2. Extract transcript ---
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception:
        transcript = None

    return {
        "video_id": video_id,
        "title": info.get("title"),
        "description": info.get("description"),
        "audio_path": audio_path,
        "transcript": transcript,
        "metadata": info
    }

def load_extracted(etl_output):
    """
    Load ETL output into a usable form for preprocessing.
    """
    print(f"Loaded YouTube extraction for video: {etl_output['title']}")
    print(f"Transcript segments: {len(etl_output['transcript']) if etl_output['transcript'] else 0}")
    print(f"Audio file: {etl_output['audio_path']}")

    return etl_output

from etl_youtube import extract_youtube
from data_preprocessing import load_extracted

etl_output = extract_youtube("https://youtu.be/QeJAdlV4fXM?si=SIMpO4nAhUGetyRf")
data = load_extracted(etl_output)

def load_extracted(etl_output):
    """
    Load ETL output into a usable form for preprocessing.
    """
    print(f"Loaded YouTube extraction for video: {etl_output['title']}")
    print(f"Transcript segments: {len(etl_output['transcript']) if etl_output['transcript'] else 0}")
    print(f"Audio file: {etl_output['audio_path']}")

    return etl_output



