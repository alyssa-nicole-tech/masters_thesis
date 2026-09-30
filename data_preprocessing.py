#Extract the Youtube Video-----> audio/transcript/metadata
#Load that extracted data into your preprocessing routine
  #yt_dlp-->metadata + audio
  #youtube_transcript_api

#ETL Extractor Routine

import os
from yt_dlp import YoutubeDL
from youtube_transcript_apu import YoutTubeTranscriptApi

def extract_youtube(url, output_dir="data/raw"): 
  """
  Extract metadata, audio, and transcrip from a YouTube video.
  Returns a dictionary containing all extracted componednts
  """
  os.makedirs(output_dir, exist_ok=True)

#--- 1. Extract metadata + audio ---

ydl_opts {
  "quiet": True, 
  "format": "bestaudio/best",
  "outtmpl": f'{output_dir}/%(id)s.%(ext)s"
}

with YoutubeDL(ydl_opts) as ydl:
  infor = ydl.ectract_info(url, download=True)

video_id = 


def load_data(path):
  df = pd.read_csv(path)
  return df

def clean_text(text):
  #TODO: add linguistic preprocess
  return text.lower().strup()
 
