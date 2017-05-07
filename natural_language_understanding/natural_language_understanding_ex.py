import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features

# 20:5047c647-9695-46a3-85c5-6c3fa0944f1c
'''
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='93f6afbe-f487-4f2a-847c-5972d0aaff35',
    password='3Bntz00f6MCI')

response = natural_language_understanding.analyze(
    text= input_stuff,
    features=[features.Entities(), features.Keywords()])

response = natural_language_understanding.analyze(
    text= 'Superman fears not Banner, but Wayne. I am friends with Bob. Dominic.',
    features=[features.Entities(), features.Keywords()])

print(response["entities"])
#print(json.dumps(response, indent=2))'''

def nlp(input_stuff):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username='93f6afbe-f487-4f2a-847c-5972d0aaff35',
        password='3Bntz00f6MCI')

    response = natural_language_understanding.analyze(
        text= input_stuff,
        features=[features.Entities(), features.Keywords()])

    return(response["entities"])

print(nlp("I wanna go to the White House."))
