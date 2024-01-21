function submitJobDescription() {
    // Get job description from the form
    var jobDescription = document.getElementById("jobDescription").value;

    // Send a POST request to your Flask endpoint
    fetch('/api/submit-job-description', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'job_description': jobDescription }),
    })
    .then(response => response.json())
    .then(data => {
        // Display a message or handle the response as needed
        console.log(data);

        // Check if 'data' is defined and has expected properties
        if (data && data.entities && data.nouns) {
            // Display extracted entities and nouns
            document.getElementById("generatedResume").innerText = `
                Entities: ${data.entities.join(', ')}
                Nouns: ${data.nouns.join(', ')}
            `;
        } else {
            console.error('Error: Invalid data format received from the server');
        }

        // Optionally, trigger resume generation after submitting job description
        generateResume();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}


function generateResume() {
    // Get job description from the form
    var jobDescription = document.getElementById("jobDescription").value;

    // Send a POST request to your Flask endpoint for resume generation
    fetch('/api/generate-resume', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'job_description': jobDescription }),
    })
    .then(response => response.json())
    .then(data => {
        // Display the generated resume
        document.getElementById("generatedResume").innerHTML = data.generated_resume;
    })
    .catch((error) => {
        console.error('Error:', error);
    });

}