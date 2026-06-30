import unittest
from EmotionDetection.emotion_detection import emotion_detector

class Test_Emotion_Detection(unittest.TestCase):

    def test_emotion_detection(self):
        response00 = emotion_detector("I am glad this happened")
        response01 = emotion_detector("I am really mad about this")
        response02 = emotion_detector("I feel disgusted just hearing about this")
        response03 = emotion_detector("I am so sad about this")
        response04 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(response00['dominant emotion'], 'joy')
        self.assertEqual(response01['dominant emotion'], 'anger')
        self.assertEqual(response02['dominant emotion'], 'disgust')
        self.assertEqual(response03['dominant emotion'], 'sadness')
        self.assertEqual(response04['dominant emotion'], 'fear')

unittest.main()