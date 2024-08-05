'''Emotion Web Server'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def home():
    '''Render homepage'''
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detect():
    '''Call Emotion API'''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return " Invalid text! Please try again!"

    formatted_output = f"For the given statement, the system response is \
                        'anger': {response['anger']}, \
                        'disgust': {response['disgust']}, \
                        'fear': {response['fear']}, \
                        'joy': {response['joy']} and \
                        'sadness': {response['sadness']}. \
                        The dominant emotion is {response['dominant_emotion']}."

    return formatted_output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    