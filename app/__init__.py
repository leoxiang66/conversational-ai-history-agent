from flask import Flask, render_template
from flask_dialogflow.agent import DialogflowAgent
from app import webhooks

app = Flask(__name__)
agent = DialogflowAgent(app=app, route="/", templates_file="templates/templates.yaml")


@app.route("/")
def agent_template():
    return render_template('frontend.html')
