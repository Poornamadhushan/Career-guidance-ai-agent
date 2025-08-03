# Career Guidance Agent

A Flask web application that provides personalized career suggestions based on user interests, skills, and education background.

## Features

- **Interactive Web Interface**: Clean, responsive design using Tailwind CSS
- **Rule-based Career Matching**: Built-in logic to suggest careers based on user input
- **AI-Enhanced Suggestions**: Optional integration with OpenAI GPT for intelligent career recommendations
- **Real-time Results**: Dynamic display of career suggestions without page reload

## Project Structure

```
career-guidance-agent/
├── app.py                 # Flask application entry point
├── career_logic.py        # Career matching logic (rule-based and GPT)
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (API keys)
├── templates/
│   └── index.html        # Frontend HTML template
└── static/               # Static files (CSS, JS, images)
```

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**:
   - Edit the `.env` file
   - Add your OpenAI API key (optional, for AI-enhanced suggestions):
     ```
     OPENAI_API_KEY=your_actual_api_key_here
     ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the App**:
   - Open your browser and go to `http://localhost:5000`

## Usage

1. Fill out the form with your:
   - Interests and passions
   - Skills (current or desired)
   - Educational background

2. Choose whether to use AI-enhanced suggestions (requires OpenAI API key)

3. Click "Get Career Suggestions" to receive personalized recommendations

4. View detailed career information including:
   - Job description
   - Required skills
   - Recommended education path

## API Endpoints

- `GET /` - Renders the main application page
- `POST /suggest` - Accepts JSON data and returns career suggestions

### Request Format for `/suggest`:
```json
{
  "interests": "technology, problem solving",
  "skills": "programming, python, data analysis",
  "education": "Computer Science degree",
  "use_gpt": false
}
```

### Response Format:
```json
{
  "careers": [
    {
      "title": "Software Developer",
      "description": "Design and develop software applications and systems",
      "skills_needed": "Programming languages, problem-solving, logical thinking",
      "education_path": "Computer Science degree or coding bootcamp"
    }
  ]
}
```

## Customization

### Adding New Career Rules
Edit `career_logic.py` and modify the `suggest_careers()` function to add new career matching rules.

### Styling Changes
The frontend uses Tailwind CSS classes. Modify `templates/index.html` to change the appearance.

### GPT Prompt Customization
Modify the prompt in the `suggest_careers_gpt()` function to change how the AI generates suggestions.

## Dependencies

- **Flask**: Web framework
- **OpenAI**: API client for GPT integration
- **python-dotenv**: Environment variable management
- **Tailwind CSS**: Frontend styling (loaded via CDN)

## License

This project is open source and available under the MIT License.
