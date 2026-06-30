import requests
import json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    my_obj = {'raw_document': {"text": text_to_analyze}}

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json= my_obj, headers=header)
    
    #extract text from json string
    extract = json.loads(response.text)
    
    #dictionary slicing
    need_dict = extract['emotionPredictions'][0]['emotion']
    
    #extracts of all scores
    anger_score = need_dict['anger']
    disgust_score =need_dict['disgust']
    fear_score = need_dict['fear']
    joy_score = need_dict['joy']
    sadness_score = need_dict['sadness']
    key_max_emo = max(need_dict,key=need_dict.get)
    
    
    #final output
    emo_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': key_max_emo
    }
    return emo_dict