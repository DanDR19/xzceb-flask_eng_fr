"""
Translator unit testing module
Date: 12/02/2023
"""
import unittest
import translator

class TestTranslator(unittest.TestCase):
    """
    Testing class
    """
    def test_english_to_french(self):
        """
        Test english to french method
        """
        translator_object = translator.Translator()
        self.assertEqual(translator_object.english_to_french(None), None)
        self.assertEqual(translator_object.english_to_french("Hello"), "Bonjour")
        self.assertEqual(translator_object.english_to_french("Bonjour"), "Bonjour")

    def test_french_to_english(self):
        """
        Test french to english method
        """
        translator_object = translator.Translator()
        self.assertEqual(translator_object.french_to_english(None), None)
        self.assertEqual(translator_object.french_to_english("Bonjour"), "Hello")
        self.assertEqual(translator_object.french_to_english("Hello"), "Hello")

if __name__=="__main__":
    unittest.main()
