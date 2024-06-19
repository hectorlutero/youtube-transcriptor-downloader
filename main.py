from youtube_transcript_api import YouTubeTranscriptApi

def download_transcript(video_url):
    try:
        video_id = video_url.split("v=")[-1].split("&")[0]
        
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        transcript_text = "\n".join([entry['text'] for entry in transcript])

        with open(f'{video_id}_transcript.txt', 'w', encoding='utf-8') as file:
            file.write(transcript_text)
        
        print(f"Transcript successfully downloaded for video ID: {video_id}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Please enter the YouTube video URL: ")
    download_transcript(video_url)
