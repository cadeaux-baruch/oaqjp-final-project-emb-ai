'''
This is the emotion detection final project for Course 5. Execution of this code
with text_to_analyze will provide one of 5 emotions in a dictionary extracted from json
'''

#Imports flask and related packages
from flask import Flask, render_template, request
#Imports emotion detection
from EmotionDetection.emotion_detection import emotion_detector

#instantiates the flask app
app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def emo_detect():

    text_to_analyze = request.args.get('textToAnalyze')

    #collect response
    resp = emotion_detector(text_to_analyze)

    #extract response
    return ("For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.").format(resp['anger'], resp['disgust'], resp['fear'], resp['joy'], resp{'sadness'}, resp['dominant_emotion'])


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)