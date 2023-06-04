from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
import speech_recognition as sr

def upload_audio(request):
    return render(request, 'transcriber/upload.html')

def stream_audio(request):
    recognizer = sr.Recognizer()
    response = HttpResponse(content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    response['Transfer-Encoding'] = 'chunked'
    response.streaming = True

    def generate_transcription():
        with sr.Microphone() as source:
            while True:
                audio = recognizer.listen(source)
                try:
                    text = recognizer.recognize_google(audio)
                except sr.UnknownValueError:
                    text = ""
                except sr.RequestError:
                    text = "Error al conectarse al servicio de reconocimiento de voz"

                yield f"data: {text}\n\n"

    return StreamingHttpResponse(generate_transcription(), content_type='text/event-stream')
