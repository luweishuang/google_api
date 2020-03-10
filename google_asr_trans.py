#! -*- coding: utf-8 -*-
import os
from googletrans import Translator
import time
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io



client = speech_v1.SpeechClient()
language_code = "ja-JP"
sample_rate_hertz = 16000
encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
config = {
    "language_code": language_code,
    "sample_rate_hertz": sample_rate_hertz,
    "encoding": encoding,
}

def sample_recognize(local_file_path):
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}
    response = client.recognize(config, audio)
    asr_result = ""
    for result in response.results:
        alternative = result.alternatives[0]
        # print(u"Transcript: {}".format(alternative.transcript))
        asr_result += alternative.transcript
    return asr_result


translator = Translator()
# 可以指定服务的地址
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])


local_dir = "resources/japan/wav"

# asr_time = 0
# trans_time = 0
# begin_time = time.time()
# for cur_file in os.listdir(local_dir):
#     cur_wav_path = os.path.join(local_dir, cur_file)
#     if cur_wav_path.lower().endswith("wav"):
#         starttime = time.time()
#         asr_result = sample_recognize(cur_wav_path)
#         asr_endtime = time.time()
#         asr_time += float(asr_endtime - starttime)
#         trans_result = translator.translate(asr_result, src='ja', dest='en')
#         trans_time += float(time.time() - asr_endtime)
#         print("cur_wav_file : %s " % cur_file)
#         print("asr_result = %s " % asr_result)
#         print("trans_result = %s " % trans_result.text)
#         print("---------------------------------------")
# print("asr 总耗时： %f " % asr_time)
# print("trans 总耗时： %f " % trans_time)
# endtime = time.time()
# print("总耗时： %f " % (endtime - begin_time))


import timeit

asr_time = 0
trans_time = 0
begin_time = timeit.default_timer()
for cur_file in os.listdir(local_dir):
    cur_wav_path = os.path.join(local_dir, cur_file)
    if cur_wav_path.lower().endswith("wav"):
        starttime = timeit.default_timer()
        asr_result = sample_recognize(cur_wav_path)
        asr_endtime = timeit.default_timer()
        asr_time += float(asr_endtime - starttime)
        trans_result = translator.translate(asr_result, src='ja', dest='en')
        trans_time += float(timeit.default_timer() - asr_endtime)
        print("cur_wav_file : %s " % cur_file)
        print("asr_result = %s " % asr_result)
        print("trans_result = %s " % trans_result.text)
        print("---------------------------------------")
print("asr 总耗时： %f " % asr_time)
print("trans 总耗时： %f " % trans_time)
endtime = timeit.default_timer()
print("总耗时： %f " % (endtime - begin_time))