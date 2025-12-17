"""
Flask server for Emotion Detection application.

This module provides a web interface to analyze emotions in a given text
using the Watson NLP Emotion Detection service.
"""

import os
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(
        BASE_DIR, "oaqjp-final-project-emb-ai", "templates"
    ),
    static_folder=os.path.join(
        BASE_DIR, "oaqjp-final-project-emb-ai", "static"
    )
)


@app.route("/")
def index():
    """
    Render the home page of the application.

    Returns:
        str: Rendered HTML template.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Handle emotion detection requests.

    Retrieves user input text, invokes the emotion detector,
    and formats the response for display.

    Returns:
        str: Formatted emotion analysis or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
