from youtube_transcript_api import YouTubeTranscriptApi
import json

video_id = "Ai4zZUJMgHw"

ytt_api = YouTubeTranscriptApi() 
transcript_list = ytt_api.list(video_id)

json_data = []

for transcript in transcript_list:
    original_text = transcript.fetch()
    translated_text = transcript.translate('vi').fetch()
    
    data = {
        "language": transcript.language_code,
        "original": original_text.text,
        "translated": translated_text.text
    }
    
    json_data.append(data)

# Ghi tất cả transcript ra file JSON
with open("transcript.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print("Đã lưu transcript vào transcript.json")
