from flask import Flask, render_template, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__, static_url_path='/static')


# Load pre-trained GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/submit-job-description', methods=['POST'])
def submit_job_description():
    data = request.get_json()
    job_description = data.get('job_description')

    # Process the job description using spaCy
    #doc = nlp(job_description)

    # (You can integrate your NLP logic here)

    # Extract relevant information (you can customize this based on your requirements)
    #entities = [ent.text for ent in doc.ents]
    #nouns = [token.text for token in doc if token.pos_ == 'NOUN']

    # For now, let's just return the received job description
   # return jsonify({
        #'message': 'Job description received successfully',
        #'job_description': job_description,
        #'entities': entities,
       # 'nouns': nouns
  #  })

@app.route('/api/generate-resume', methods=['POST'])
def generate_resume():
    data = request.get_json()
    job_description = data.get('job_description')

    # Generate resume template using GPT-2
    input_text = f"Generate a resume template for a {job_description} position with skills:"
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=500)
    output = model.generate(input_ids, max_length=200, num_return_sequences=1)

    # Decode and return the generated resume template
    generated_resume = tokenizer.decode(output[0], skip_special_tokens=True)
    return jsonify({'message': 'Resume template generated successfully', 'generated_resume': generated_resume})


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
