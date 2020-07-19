from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat, SpeechRecognizer, ResultReason
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from azure.cognitiveservices.speech.languageconfig import SourceLanguageConfig
import azure.cognitiveservices.speech

speech_key, service_region = "9acb5d6239484665b8ee3566bfdf6ee8", "eastus"
speech_config = SpeechConfig(subscription=speech_key, region=service_region)
# audio_config = AudioOutputConfig(filename="test_output.wav")


#input 
# 
speech_recognizer = SpeechRecognizer(speech_config=speech_config)

print("Say something...")

result = speech_recognizer.recognize_once()



# Checks result.
if result.reason == ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == ResultReason.Canceled:
    cancellation_details = cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
        
#output


audio_config = AudioOutputConfig(use_default_speaker=True)
language_config = SourceLanguageConfig("ko-KR")
synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
synthesizer.speak_text_async("result.text")



