import xml.etree.ElementTree as ET
from django.utils.translation import get_language

def load_translations():
    """Load translations from an XML file."""
    translations = {}

    try:
        tree = ET.parse("translations.xml")  # Ensure the correct path
        root = tree.getroot()

        for text in root.findall("text"):
            key = text.get("key")
            translations[key] = {}

            for lang_element in text:
                translations[key][lang_element.tag] = lang_element.text  # Store translations by language code

    except Exception as e:
        print(f"Error loading translations: {e}")

    return translations


def translate_text(text):
    """Return the translation for the given text based on the user's language."""
    translations = load_translations()
    lang = get_language()[:2]  # Get 'hr', 'en', or 'de'

    if text in translations and lang in translations[text]:
        return translations[text][lang]
    
    return text  # Return original text if no translation found
