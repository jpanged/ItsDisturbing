# Import Libraries and APIs
import json
from sys import *
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features
import output
import hashlib

# Defines Main


def main():
    menu()

# Presents user with menu of options


def menu():

    #user_inp = raw_input("\nEnter your .wav file or .txt file: ")
    try:
        user_inp = argv[1]
        # Begins by checking whether input is sound or text

        # If sound, convert to text, then create dictionary
        if user_inp.endswith(".wav"):
            transcript_str = wav_file_to_text(user_inp)
            outFile = get_master_dictionary(transcript_str, "wav")
        elif user_inp.endswith(".txt"):  # If text, just convert to dictionary
            outFile = get_master_dictionary(user_inp, "txt")
        else:
            raise fileExtensionError
        output.outPutFile(outFile)
    except fileExtensionError:
        print("ERROR: Must be a .wav or .txt file in the following format:")
        print("python main_analyzer.py <FILE>")
    except IndexError:
        print("ERROR: Must be a .wav or .txt file in the following format:")
        print("python main_analyzer.py <FILE>")


class fileExtensionError(Exception):
    pass

# wav -> txt
# Process sound input to text output
# A sound_file is a str representing a .wav file


def wav_file_to_text(sound_file):
    transcript = []

    with open(join(dirname(__file__), sound_file), 'rb') as audio_file:
        output = (speech_to_text.recognize(
            audio_file, content_type='audio/wav', timestamps=False,
            word_confidence=False, continuous=True))

        for i in range((len(output['results']))):
            transcript.append(output['results'][i]
                              ['alternatives'][0]['transcript'])

        ret = ""
        for i in range(len(transcript)):
            ret = ret + transcript[i] + "\n"
        if ret.endswith('\n'):
            ret = ret[:-2]
    return ret


# my_text is a str representing the .txt file the user wants to read from
# .txt file -> dict
# Returns a dictionary of each line in the format
#     'line1' : tone
# where tone is the line's emotion, writing, and social tones returned
# from the function below
def get_master_dictionary(my_file, type):
    master_dict = {}
    # Begins by checking whether input is sound or text
    if type == "wav":   # .wav file
        my_text = my_file.split('\n')  # --> ['Line 1', 'Line 2', 'Line 3']
        num_lines = len(my_text)  # Number of lines
    else:   # .txt file
        my_text = open(my_file, "r")
        my_text = my_text.read().replace('\n', '')
        my_text = my_text.split('.')
    # Initializes dictionary
    master_dict = {}
    master_dict['num_lines'] = 0
    master_dict['summary'] = []
    curr_index = 0
    textSummary = ""
    master_dict["lines"] = []
    # Traverses every line of input to create dictionary
    for line in my_text:
        if line != "":
            textSummary += line + "\n "
            print("\n\nline = {}".format(line))
            if line.endswith('\n'):
                line = line[:-2]
            # Calls Natural Language Understanding API
            nlu_dict = get_nlu_dict_per_line(line)
            tone_dict = get_tone_dict_per_line(line)  # Calls Tone Analyzer API
            hash_object = hashlib.md5(bytes(line, "utf-8"))
            hash_object = hash_object.hexdigest()
            # Starts to format output
            line_output = {
                'text': line,
                'hash': hash_object,
                'nlu': nlu_dict,
                'tone': tone_dict
            }
            line_output = {"line": line_output}
            dict_name = "line" + str(curr_index)
            master_dict['summary'] = textSummary
            master_dict['num_lines'] = 1 + master_dict['num_lines']

            master_dict["lines"].append(line_output)
            curr_index += 1

    print(json.dumps(master_dict, indent=2))
    master_dict = json.dumps(master_dict)
    return master_dict  # Spits out JSON output


# Calls the SpeechToTextV1 API
speech_to_text = SpeechToTextV1(
    username="587aae79-5967-434b-93c4-3c4bd3f40621",  # API Key
    password="AnPJuMD0GjYE",  # Replace with personal API
    x_watson_learning_opt_out=False
)

# Calls ToneAnalyzerV3 API
tone_analyzer = ToneAnalyzerV3(
    username='177e2d8a-1048-4fcc-b256-022adbc2fc6b',  # API Key
    password='xMZuRoB52uu7',  # Replace with personal API
    #url = 'https://gateway.watsonplatform.net/tone-analyzer/api'
    version='2016-05-06'
)


# A line is a str representing one line of the .txt file
# str -> dict
# Returns a dictionary with corresponding emotion, writing, and social
# tone scores
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

    output = tone_analyzer.tone(text=line)
    for i in range(3):
        tone_categories = output['document_tone']['tone_categories'][i]
        category_id = tone_categories['category_id']
        tones = tone_categories['tones']
        # print("\n{}".format(category_id))

        for j in range(len(tones)):
            tone_name = tones[j]['tone_name']
            score = tones[j]['score']
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

# str -> listofdicts
# Gets Natural Language data for the line of text


def nlp(input_stuff):
    # Calls NaturalLanguageUnderstandingV1 API
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username="83e901c3-bc9c-43f8-af70-c836d0cd0ea0",  # API Key
        password="yDEjfUUEeHBz")  # Replace with personal API

    response = natural_language_understanding.analyze(
        text=input_stuff,
        features=[features.Concepts(), features.Entities(), features.Keywords(), features.Categories(), features.Emotion(), features.Sentiment(), features.Relations(), features.SemanticRoles()])
    nlu_data = {
        'sentiment': response["sentiment"],
        'semanticRoles': response["semantic_roles"],
        'concepts': response["concepts"],
        'entities': response["entities"],
        'relations': response["relations"],
        'concepts': response["concepts"],
        'categoreis': response["categories"]
    }
    nlu_data = [nlu_data]
    # print(nlu_data)
    return(nlu_data)


# a line is a str representing one line of the .txt file
# str -> dict
# Returns a dictionary with corresponding type, text, relevance, count values
def get_nlu_dict_per_line(line):
    nlu_dict = {}
    output = nlp(line)
    nlu_dict['nlu_entity_items'] = len(output[0]["entities"])
    for i in range(len(output[0]["entities"])):
        entity_dict = {
            'type': '',
            'text': '',
            'relevance': '',
            'count': ''
        }

        entity = output[0]["entities"][i]
        entity_dict['type'] = entity['type']
        entity_dict['text'] = entity['text']
        entity_dict['relevance'] = entity['relevance']
        entity_dict['count'] = entity['count']

        en_dict_name = "entity" + str(i)
        nlu_dict[en_dict_name] = entity_dict
        # nlu_dict.append(entity_dict)

#####
# TO BE ADDED IS THE FOLLOWING WHICH ADDS IN A LOT MORE NLU DATA
#####

    # sentiment_dict = {
    #     'score': output[0]["sentiment"]["document"]["score"],
    #     'label': output[0]["sentiment"]["document"]["label"]
    # }
    #
    # for i in range(len(output[0]["semanticRoles"])):
    #     semantic_roles = output[0]["semanticRoles"][i]
    #     semantic_roles_action_dict = {
    #         'text': '',
    #         'tense': '',
    #         'text-normalized': ''
    #     }
    #     semantic_roles_dict = {
    #         'subject': '',
    #         'sentence': '',
    #         'object': '',
    #         'action': semantic_roles_action_dict,
    #     }
    #     semantic_roles_dict["subject"] = semantic_roles["subject"]["text"]
    #     semantic_roles_dict["sentance"] = semanti_roles["sentance"]
    #     semantic_roles_dict["object"] = semantic_roles["object"]["text"]
    #     for i in range(len(output[0]["semanticRoles"])):
    #         semantic_roles_action_dict["text"]
    #
    # concepts_dict = {
    #     'text': '',
    #     'relevance': '',
    #     'dbpedia_resource': ''
    # }
    # relations_arguments_entities_dict = {
    #     'type': '',
    #     'text': ''
    # }
    # relations_arguments_dict = {
    #     'text': '',
    #     'entities': relations_arguments_entities_dict
    # }
    # relations_dict = {
    #     'type': '',
    #     'sentence': '',
    #     'score': '',
    #     'arguments': relations_arguments_dict,
    # }
    # categories_category_dict = {
    #     'score': '',
    #     'label': ''
    # }
    # cetegories_dict = {
    #     'category': categories_category_dict
    # }
    return nlu_dict


if __name__ == "__main__":
    main()
