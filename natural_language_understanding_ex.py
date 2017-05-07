import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features

# 20:5047c647-9695-46a3-85c5-6c3fa0944f1c

def nlp(input_stuff):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username='93f6afbe-f487-4f2a-847c-5972d0aaff35',
        password='3Bntz00f6MCI')

    response = natural_language_understanding.analyze(
        text= input_stuff,
        features=[features.Entities(), features.Keywords()])
    return(response["entities"])

test = nlp("Bob is a great guy, and so is Dylan.")

print(test[0]['type'])
