from googletrans import Translator
translator = Translator()

trans_en = translator.translate('トレント・アレクサンダー・アーノルド')
print(trans_en.text)
