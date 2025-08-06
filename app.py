import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from career_logic import suggest_careers, suggest_careers_gpt

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.get_json()
    interests = data.get('interests', '')
    skills = data.get('skills', '')
    education = data.get('education', '')
    use_gpt = data.get('use_gpt', False)

    if use_gpt:
        suggestions = suggest_careers_gpt(interests, skills, education)
    else:
        suggestions = suggest_careers(interests, skills, education)
    return jsonify({'careers': suggestions})

if __name__ == '__main__':
    app.run(debug=True)
