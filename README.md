这一切的一切的前提是可以上google，从chrome和控制台，两种方式都必须确保可以上谷歌。
使用蓝灯代理全部流量。
vim ~/.bashrc, 增加
export http_proxy=http://127.0.0.1:***
export https_proxy=http://127.0.0.1:***

## 有关 google cloud 授权 
创建服务账号, 并在本机上 export GOOGLE_APPLICATION_CREDENTIALS=dialo-around-5a18309a3f8e.json

## Installing 
asr:

pip install --upgrade google-cloud-speech

translate:

pip install googletrans

tts:

pip install --upgrade google-cloud-texttospeech


## 相关repo
Python Client for Cloud Speech API[https://github.com/googleapis/python-speech]

## 参考文献
Transcribing phone audio with enhanced models[https://cloud.google.com/speech-to-text/docs/phone-model]

