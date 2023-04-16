from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def question_page():
    "Show prompt for madlibs"
    prompts = story.prompts
    
    return render_template("questions.html", prompts = prompts)

@app.route('/story')
def show_story():
    "Display your generated story"
    text = story.generate(request.args)

    return render_template("story.html", text = text)