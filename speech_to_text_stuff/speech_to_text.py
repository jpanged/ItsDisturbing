import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1


speech_to_text = SpeechToTextV1(
   username= "587aae79-5967-434b-93c4-3c4bd3f40621",
   password= "AnPJuMD0GjYE",
   x_watson_learning_opt_out=False
)

with open(join(dirname(__file__), 'beemovie.wav'), 'rb') as audio_file:
   output = json.dumps((speech_to_text.recognize(
      audio_file, content_type='audio/wav', timestamps=False,
      word_confidence=True)), indent=2)

'''
   transcript = output['results'][0]['alternatives'][0]['transcript']
'''

print(output)

