import json
from sys import *
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features


def main():
    menu()

"""
Presents user with menu of options
"""
def menu():
    user_inp = raw_input("\nEnter your .wav file or .txt file: ")
    if user_inp.endswith(".wav"):
        transcript_str = wav_file_to_text(user_inp)
        get_master_dictionary(transcript_str, "wav")
    elif user_inp.endswith(".txt"):
        get_master_dictionary(user_inp, "txt")
    else:
        print("Invalid option")
        menu()

"""
a sound_file is a str representing a .wav file
"""
def wav_file_to_text(sound_file):
   transcript = []

   with open(join(dirname(__file__), sound_file), 'rb') as audio_file:
      output = (speech_to_text.recognize(
         audio_file, content_type='audio/wav', timestamps=False,
         word_confidence=False, continuous=True))

      for i in range((len(output['results']))):
         transcript.append(output['results'][i]['alternatives'][0]['transcript'])

      ret = ""
      for i in range(len(transcript)):
         ret = ret + transcript[i] + "\n"
      if ret.endswith('\n'):
          ret = ret[:-2]
   return ret

"""
my_text is a str representing the .txt file the user wants to read from
.txt file -> dict
Returns a dictionary of each line in the format
    'line1' : tone
where tone is the line's emotion, writing, and social tones returned from the
function below
"""
def get_master_dictionary(my_file, type):
    master_dict = {}

    if type == "wav":   # .wav file
        my_text = my_file.split('\n')  # --> ['Line 1', 'Line 2', 'Line 3']
        num_lines = len(my_text)
    else:   # .txt file
        my_text = open(my_file, "r")
        my_text = my_text.read().replace('\n', '')
        my_text = my_text.split('.')

    master_dict['num_lines'] = 0
    curr_index = 0

    for line in my_text:
        if line != "":
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
            master_dict['num_lines'] = 1 + master_dict['num_lines']
            master_dict[dict_name] = line_output
            curr_index += 1

    print(json.dumps(master_dict, indent=2))
    master_dict = json.dumps(master_dict)
    return master_dict


speech_to_text = SpeechToTextV1(
   username = "587aae79-5967-434b-93c4-3c4bd3f40621",
   password = "AnPJuMD0GjYE",
   x_watson_learning_opt_out = False
)


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
        version = '2017-02-27',
        username = "83e901c3-bc9c-43f8-af70-c836d0cd0ea0",
        password = "yDEjfUUEeHBz")

    response = natural_language_understanding.analyze(
        text = input_stuff,
        features = [features.Entities(), features.Keywords()])
    return(response["entities"])

"""
a line is a str representing one line of the .txt file
str -> dict
Returns a dictionary with corresponding type, text, relevance, count values
"""
def get_nlu_dict_per_line(line):
    nlu_dict = {}
    output = nlp(line)
    nlu_dict['nlu_entity_items'] = len(output)
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

        en_dict_name = "entity" + str(i)
        nlu_dict[en_dict_name] = entity_dict

    return nlu_dict



if __name__ == "__main__":
    main()
