import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
#version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def _translate(text, lang1code, lang2code):
    result = language_translator.translate(
        text=text,
        model_id=lang1code+'-'+lang2code
    ).get_result()
    return result['translations'][0]['translation'] if (len(result['translations'])>0) \
        else 'Error: No translations available...'

def french_to_english(french_text):
    english_text = _translate(french_text, 'fr', 'en')
    return english_text
def english_to_french(english_text):
    french_text = _translate(english_text, 'en', 'fr')
    return french_text