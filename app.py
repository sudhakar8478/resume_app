from flask import Flask, render_template, request, jsonify
import spacy

app = Flask(__name__, static_url_path='/static')

nlp = spacy.load("en_core_web_sm")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/submit-job-description', methods=['POST'])
def submit_job_description():
    data = request.get_json()
    job_description = data.get('job_description')

    # Process the job description using spaCy
    doc = nlp(job_description)

    # (You can integrate your NLP logic here)

    # Extract relevant information (you can customize this based on your requirements)
    entities = [ent.text for ent in doc.ents]
    nouns = [token.text for token in doc if token.pos_ == 'NOUN']

    # For now, let's just return the received job description
    return jsonify({
        'message': 'Job description received successfully',
        'job_description': job_description,
        'entities': entities,
        'nouns': nouns
    })

@app.route('/api/generate-resume', methods=['POST'])
def generate_resume():
    data = request.get_json()
    job_description = data.get('job_description')

    # Process the job description and generate a personalized resume template
    # (You can integrate your resume generation logic here)

    # For now, let's just return a placeholder response
    return jsonify({'message': 'Resume generated successfully', 'generated_resume': 'Generated Resume Template'})


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
