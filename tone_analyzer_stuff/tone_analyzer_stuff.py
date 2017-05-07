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
    my_file = open(argv[1], "r")
    for line in my_file:
        print("\n\nline = {}".format(line))
        output = tone_analyzer.tone(text = line)
        #print output["document_tone"][0]["tones"][0]["score"]
        for i in range(3):
            tone_categories = output['document_tone']['tone_categories'][i]
            category_id = tone_categories['category_id']
            tones = tone_categories['tones']
            print("\n{}".format(category_id))

            for j in range(len(tones)):
                tone_name =  tones[j]['tone_name']
                score =  tones[j]['score']
                tone_id = tones[j]['tone_id']
                print("{}: {}".format(tone_name, score))


def analyze(text):
    out = tone_analyzer.tone(text)
    return out

if __name__ == "__main__":
    main()
