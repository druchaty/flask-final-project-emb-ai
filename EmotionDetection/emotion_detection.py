''' Emotion detection module
'''
import json
import requests

def emotion_detector(text_to_analyse):
    ''' Emotion detector function returns emotion prediction
    '''
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    response = requests.post(url, json = myobj, headers = header, timeout=2)
    formatted_response = json.loads(response.text)

    anger = None
    disgust = None
    fear = None
    joy = None
    sadness = None
    dominant_emotion = None

    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']

        dominant_emotion = max(emotions, key=emotions.get)

    # For the rest status_code's including 400 the values will be 'None'
    return { 
        "anger": anger, 
        "disgust": disgust, 
        "fear": fear, 
        "joy": joy, 
        "sadness": sadness, 
        "dominant_emotion": dominant_emotion 
        }
