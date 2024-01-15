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
        document.getElementById("generatedResume").innerText = data.generated_resume;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}