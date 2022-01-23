from translate import Translator

tradutor = Translator(from_lang = 'english', to_lang='portuguese')

resultado = tradutor.translate('I CAN CODE')

print(resultado)