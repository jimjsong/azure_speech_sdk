from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat, SpeechRecognizer, ResultReason
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from azure.cognitiveservices.speech.languageconfig import SourceLanguageConfig
import azure.cognitiveservices.speech


import azure.cognitiveservices.speech as speechsdk

# Sets source and target languages.
# Replace with the languages of your choice, from list found here: https://aka.ms/speech/sttt-languages
fromLanguage = 'en-US'
toLanguage = 'ko'
speech_key, service_region = "9acb5d6239484665b8ee3566bfdf6ee8", "eastus"

def translate_speech_to_text():

    # Creates an instance of a speech translation config with specified subscription key and service region.
    # Replace with your own subscription key and region identifier from here: https://aka.ms/speech/sdkregion
    translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=speech_key, region=service_region)


    translation_config.speech_recognition_language = fromLanguage
    translation_config.add_target_language(toLanguage)

    # Creates a translation recognizer using and audio file as input.
    recognizer = speechsdk.translation.TranslationRecognizer(translation_config=translation_config)

    # Starts translation, and returns after a single utterance is recognized. The end of a
    # single utterance is determined by listening for silence at the end or until a maximum of 15
    # seconds of audio is processed. It returns the recognized text as well as the translation.
    # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
    # shot recognition like command or query.
    # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
    print("Say something...")
    result = recognizer.recognize_once()

    # Check the result
    if result.reason == speechsdk.ResultReason.TranslatedSpeech:
        print("RECOGNIZED '{}': {}".format(fromLanguage, result.text))
        print("TRANSLATED into {}: {}".format(toLanguage, result.translations[toLanguage]))
        speak_translations(result)
    elif result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("RECOGNIZED: {} (text could not be translated)".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("NOMATCH: Speech could not be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        print("CANCELED: Reason={}".format(result.cancellation_details.reason))
        if result.cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("CANCELED: ErrorDetails={}".format(result.cancellation_details.error_details))

def speak_translations(result):
    audio_config = AudioOutputConfig(use_default_speaker=True)
    language_config = SourceLanguageConfig("ko-KR")
    speech_config = SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_synthesis_language = "ko-KR"
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    # synthesizer.speak_text_async(result.text) #English
    synthesizer.speak_text_async(result.translations[toLanguage])


translate_speech_to_text()