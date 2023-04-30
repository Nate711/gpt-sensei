from playsound import playsound
from google.cloud import texttospeech

import os
import pickle
import openai
import yaml

words = []
while True:
    word = input("enter vocab: ")
    if len(word) == 0:
        break
    words.append(word)
words_str = ", ".join(words)
print(f"WORDS: {words_str}")

# openai.api_key = os.getenv("OPENAI_API_KEY")
with open("openai-api-key.txt", "r") as openai_key:
    openai.api_key = openai_key.readline()

result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    # model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "あなたは、ユーザーから提供されたいくつかの単語を使ってストーリーを書く、役に立つアシスタントです。",
        },
        {
            "role": "user",
            "content": f'"{words_str}"を使っている中級者に適切な例文を書いてください。あとで、英語に翻訳してください。',
        },
    ],
)

with open("response.pickle", "wb") as file:
    pickle.dump(result, file)
print(result.choices[0].message.content)
gpt_response_text = result.choices[0].message.content


# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input
text = gpt_response_text

# Set the voice configuration
voice = texttospeech.VoiceSelectionParams(language_code="ja-JP", name="ja-JP-Neural2-C")

# Set the audio file type and audio encoding
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

# Perform the text-to-speech request
synthesis_input = texttospeech.SynthesisInput(text=text)
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# Save the audio output to a file
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')


# specify the path of the mp3 file
mp3_file = "output.mp3"

# play the mp3 file
playsound(mp3_file)
