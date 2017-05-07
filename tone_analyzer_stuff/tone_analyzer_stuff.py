import json
from watson_developer_cloud import ToneAnalyzerV3
from sys import *

tone_analyzer = ToneAnalyzerV3(
    username = '177e2d8a-1048-4fcc-b256-022adbc2fc6b',
    password = 'xMZuRoB52uu7',
    #url = 'https://gateway.watsonplatform.net/tone-analyzer/api'
    version = '2016-05-06'
)

def main():
    get_tone_dictionaries(argv[1])

"""
my_text is a str representing the .txt file the user wants to read from
.txt file -> dict
Returns a dictionary of each line in the format
    'line1' : tone
where tone is the line's emotion, writing, and social tones returned from the
function below
"""
def get_tone_dictionaries(my_text):
    supreme_dict = {}
    my_file = open(my_text, "r")
    curr_index = 0

    for line in my_file:
        print("\n\nline = {}".format(line))
        if line.endswith('\n'):
            line = line[:-2]
        tone_dict = get_tone_dict_per_line(line)
        line_output = {
            'tone': tone_dict,
            'text': line
        }
        dict_name = "line" + str(curr_index)
        supreme_dict[dict_name] = line_output
        curr_index += 1

    #print supreme_dict

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

if __name__ == "__main__":
    main()
