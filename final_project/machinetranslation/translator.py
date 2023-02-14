"""
Translator module. IBM Course
Date: 12/02/2023
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

class Translator:
    """
    Translator English-French using IBM Watson API
    """
    def __init__(self):
        """
        Translator class constructor
        """
        load_dotenv()
        self.__apikey = os.environ['apiKey']
        self.__url = os.environ['URL']
        self.__authenticator = IAMAuthenticator(self.__apikey)
        self.language_translator = LanguageTranslatorV3(
            version='2018-05-01',
            authenticator=self.__authenticator
        )
        self.language_translator.set_service_url(self.__url)

    def english_to_french(self, english_text):
        """
        This methods translates english input text to french
        ---
        Parameters:
        english_text: string
        ---
        """
        translated = None
        if english_text is not None and isinstance(english_text, str):
            translation=self.language_translator.translate(
                text=english_text,
                model_id='en-fr').get_result()
            translated = translation["translations"][0]["translation"]
        return translated

    def french_to_english(self, french_text):
        """
        This methods translates french input text to english
        ---
        Parameters:
        french_text: string
        ---
        """
        translated = None
        if french_text is not None and isinstance(french_text, str):
            translation=self.language_translator.translate(
                text=french_text,
                model_id='fr-en').get_result()
            translated = translation["translations"][0]["translation"]
        return translated
