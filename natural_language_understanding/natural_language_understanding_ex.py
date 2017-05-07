import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features


natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='93f6afbe-f487-4f2a-847c-5972d0aaff35',
    password='3Bntz00f6MCI')

'''response = natural_language_understanding.analyze(
    text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
         'Superman fears not Banner, but Wayne.',
    features=[features.Entities(), features.Keywords()])'''

response = natural_language_understanding.analyze(
    text='According to all known laws of aviation, there is no way that a bee should be able to fly.',
         #'Superman fears not Banner, but Wayne.',
    features=[features.Entities(),
                features.Keywords(),
                features.Concepts(),
                features.Categories(),
                features.Emotion(),
                features.SemanticRoles(),
                features.Relations(),
                features.Sentiment()])

print(json.dumps(response, indent=2))
