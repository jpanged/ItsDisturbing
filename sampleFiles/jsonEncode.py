import json

NLP_data = {
    'tone': '',
    'text': '',
    'relevance': ''
}

speech_to_text = {
    'text': output,
}

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

tone = {
    'emotion': tone_analysis_emotion,
    'writing': tone_analysis_writing,
    'social': tone_analysis_social
}

data = {
    'NLP': NLP_data,
    'tone': tone

}

json_str = json.dumps(data)

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)
