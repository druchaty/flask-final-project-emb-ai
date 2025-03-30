''' Emotion detection module
'''
import requests

def emotion_detector(text_to_analyse):
    ''' Emotion detector function returns emotion prediction
    '''
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    response = requests.post(url, json = myobj, headers = header, timeout=2)

    return response.text
