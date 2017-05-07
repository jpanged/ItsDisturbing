import json
from sys import *
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features


def main():
    get_master_dictionary(argv[1])

"""
my_text is a str representing the .txt file the user wants to read from
.txt file -> dict
Returns a dictionary of each line in the format
    'line1' : tone
where tone is the line's emotion, writing, and social tones returned from the
function below
"""
def get_master_dictionary(my_text):
    master_dict = {}
    my_file = open(my_text, "r")
    curr_index = 0

    for line in my_file:
        print("\n\nline = {}".format(line))
        if line.endswith('\n'):
            line = line[:-2]
        nlu_dict = get_nlu_dict_per_line(line)
        tone_dict = get_tone_dict_per_line(line)
        line_output = {
            'text': line,
            'nlu': nlu_dict,
            'tone': tone_dict
        }
        dict_name = "line" + str(curr_index)
        master_dict[dict_name] = line_output
        curr_index += 1

    print master_dict



tone_analyzer = ToneAnalyzerV3(
    username = '177e2d8a-1048-4fcc-b256-022adbc2fc6b',
    password = 'xMZuRoB52uu7',
    #url = 'https://gateway.watsonplatform.net/tone-analyzer/api'
    version = '2016-05-06'
)


"""
a line is a str representing one line of the .txt file
str -> dict
Returns a dictionary with corresponding emotion, writing, and social tone scores
"""
def get_tone_dict_per_line(line):

    tone_analysis_emotion = {
        'anger': '',
        'disgust': '',
        'fear': '',
        'joy': '',
        'sadness': ''
    }

    tone_analysis_writing = {
        'analytical': '',
        'confident': '',
        'tentative': ''
    }

    tone_analysis_social = {
        'openness_big5': '',
        'conscientiousness_big5': '',
        'extraversion_big5': '',
        'agreeableness_big5': '',
        'neuroticism_big5': ''
    }

    output = tone_analyzer.tone(text = line)
    for i in range(3):
        tone_categories = output['document_tone']['tone_categories'][i]
        category_id = tone_categories['category_id']
        tones = tone_categories['tones']
        #print("\n{}".format(category_id))

        for j in range(len(tones)):
            tone_name =  tones[j]['tone_name']
            score =  tones[j]['score']
            tone_id = tones[j]['tone_id']
            #print("{}: {}".format(tone_name, score))

            if category_id == "emotion_tone":
                tone_dict = tone_analysis_emotion
            elif category_id == "writing_tone":
                tone_dict = tone_analysis_writing
            else:
                tone_dict = tone_analysis_social
            tone_dict[tone_id] = score

    tone = {
        'emotion': tone_analysis_emotion,
        'writing': tone_analysis_writing,
        'social': tone_analysis_social
    }

    return tone


def nlp(input_stuff):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username='93f6afbe-f487-4f2a-847c-5972d0aaff35',
        password='3Bntz00f6MCI')

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
        nlu_dict[en_dict_name, entity_dict]

    #print("nlu_dict = {}".format(nlu_dict))
    return nlu_dict



if __name__ == "__main__":
    main()
