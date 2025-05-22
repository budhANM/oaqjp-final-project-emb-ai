
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask(__name__)

@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():

    text_to_analyze = request.args.get('textToAnalyze')
    
    response_dict = emotion_detector(text_to_analyze)

    if response_dict['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    else:
        formatted_output = (
            f"For the given statement, the system response is "
            f"'anger': {response_dict['anger']:.7f}, "
            f"'disgust': {response_dict['disgust']:.7f}, "
            f"'fear': {response_dict['fear']:.7f}, "
            f"'joy': {response_dict['joy']:.7f}, "
            f"and 'sadness': {response_dict['sadness']:.7f}. "
            f"The dominant emotion is {response_dict['dominant_emotion']}."
        )
        return formatted_output

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)