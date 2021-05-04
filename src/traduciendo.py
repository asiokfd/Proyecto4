import TextBlob
#@fer ;)


def intoEnglish(string):
    """
    Esta función toma como elemento un string y, en caso de que esté en español, nos lo devuelve en inglés. En otro caso nos devuelve 
    el mismo string.
    """
    spanish_string = TextBlob(string)
    try:
        english_blob=spanish_string.translate(from_lang='es',to='en')
        return "".join(list(english_blob))
    except:
        return string