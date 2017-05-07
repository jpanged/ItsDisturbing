import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features

# 20:5047c647-9695-46a3-85c5-6c3fa0944f1c

def main():
    get_nlu_dict_per_line("Bob is a great guy, and so is Dylan.")

def nlp(input_stuff):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version = '2017-02-27',
        username = "83e901c3-bc9c-43f8-af70-c836d0cd0ea0",
        password = "yDEjfUUEeHBz")

    response = natural_language_understanding.analyze(
        text= input_stuff,
        features=[features.Entities(), features.Keywords()])
    return(response["entities"])

"""
a line is a str representing one line of the .txt file
str -> dict
Returns a dictionary with corresponding type, text, relevance, count values
"""
def get_nlu_dict_per_line(line):

    nlu_dict = {}

    output = nlp(line)
    #print("output = {}".format(output))
    for i in range(len(output)):
        entity_dict = {
            'type': '',
            'text': '',
            'relevance': '',
            'count': ''
        }

        entity = output[i]
        entity_dict['type'] = entity['type']
        entity_dict['text'] = entity['text']
        entity_dict['relevance'] = entity['relevance']
        entity_dict['count'] = entity['count']

        en_dict_name = "entity" + str(i+1)
        nlu_dict[en_dict_name] = entity_dict

    return nlu_dict

if __name__ == "__main__":
    main()
