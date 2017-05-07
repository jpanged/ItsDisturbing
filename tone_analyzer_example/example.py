import json
from watson_developer_cloud import ToneAnalyzerV3


tone_analyzer = ToneAnalyzerV3(
    username='2e243f72-72b3-40cf-a697-928fe5cc074c',
    password='L1TKnYKLhTKN',
    version='2016-02-11')

#print(json.dumps(tone_analyzer.tone(text='I am very happy'), indent=2))

utterances = [{'text': 'I am very happy', 'user': 'glenn'}]
#print(json.dumps(tone_analyzer.tone_chat(utterances), indent=2))

test = "I am very tired right now, I wish I could sleep."
test2 = "Wow! What a nice day today, I can't wait to go outside."
print(json.dumps(tone_analyzer.tone(text=test2), indent=2))
