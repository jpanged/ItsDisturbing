import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1


speech_to_text = SpeechToTextV1(
   username= "587aae79-5967-434b-93c4-3c4bd3f40621",
   password= "AnPJuMD0GjYE",
   x_watson_learning_opt_out=False
)

transcript = []

with open(join(dirname(__file__), 'beemovie.wav'), 'rb') as audio_file:
   output = (speech_to_text.recognize(
      audio_file, content_type='audio/wav', timestamps=False,
      word_confidence=False, continuous=True))

   for i in range((len(output['results']))):
      transcript.append(output['results'][i]['alternatives'][0]['transcript'])

   index = []

   for i in range(1, len(transcript) + 1):
      index.append(("line" + str(i)))

   list1 = []

   for i in range(len(transcript)):
      t = index[i], transcript[i]
      list1.append(t)

   d = dict(list1)

print(d)

