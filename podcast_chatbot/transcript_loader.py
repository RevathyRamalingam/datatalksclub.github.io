"""
transcript_loader.py
--------------------
Fetches transcripts from YouTube videos and saves them locally.
Each transcript is broken into "chunks" (groups of lines) so the chatbot
can return answers with accurate timestamps.

HOW TO USE:
    from transcript_loader import load_episodes
    episodes = load_episodes(EPISODE_LIST)
"""

import json
import os
from youtube_transcript_api import YouTubeTranscriptApi
# ─────────────────────────────────────────────
# 1.  Define your podcast episodes here
# ─────────────────────────────────────────────
# Add as many episodes as you like.
# "video_id" is the part after "?v=" in a YouTube URL.
# Example: https://www.youtube.com/watch?v=abc123  →  video_id = "abc123"

EPISODE_LIST = [
    {
        "video_id": "sample",               # ← replace with real YouTube video IDs
        "title":    "Episode 1: Getting Started with AI",
        "url":      "https://www.youtube.com/watch?v=29eo5XnuMOs",
    },
    # Add more episodes here …
]
TRANSCRIPTS_FILE = "transcripts.json"   # where transcripts are cached locally
CHUNK_SECONDS    = 60                    # group transcript lines into 60-second chunks
def fetch_transcript(video_id:str)-> list(Dict):

"""
    Downloads the auto-generated transcript for a YouTube video.

    Returns a list of dicts like:
        [{"text": "Hello world", "start": 12.4, "duration": 2.1}, ...]

    'start' is the timestamp in SECONDS from the beginning.
"""
try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    print(f"Transcript fetched for the video {video_id} is {transcript}")
except Exception as e:
    print(f"could not fetch transcription for video {video_id}: {e}")

def load_episodes(episode_list: list[dict])-> list(dict):
    
if __name__ == "main":
    load_episodes(EPISODE_LIST)
