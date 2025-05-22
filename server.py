"""
This Flask application provides an emotion detection service.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def render_index_page():
    """
    Renders the main index.html page for the application.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Analyzes the text provided in the 'textToAnalyze' query parameter and returns detected emotion scores and the dominant emotion.
    Handles invalid input by returning an error message.

    Returns:
        str: A formatted string containing emotion scores and dominant emotion,
             or an error message if the input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    response_dict = emotion_detector(text_to_analyze)

    if response_dict is None or response_dict.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    expected_emotion_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    for key in expected_emotion_keys:
        if response_dict.get(key) is None:
            return "Invalid text! Please try again!"

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
