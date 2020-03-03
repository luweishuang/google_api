#! -*- coding: utf-8 -*-

from googletrans import Translator

translator = Translator()
# 可以指定服务的地址
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

print(translator.translate('안녕하세요.'))
# <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
print(translator.translate('안녕하세요.', dest='ja'))
# <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
print(translator.translate('veritas lux mea', src='la'))
# <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>