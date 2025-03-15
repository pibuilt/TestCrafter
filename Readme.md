# AI Test Case Generator

An AI-powered system that automatically generates unit test cases for Python, Java, and C++ code from a given GitHub repository. It uses a pre-trained CodeT5 model to analyze the source code and generate meaningful test cases.

## Usage

### Installation  

Clone this repository:  
```sh
git clone https://github.com/your-username/ai-test-generator.git
cd ai-test-generator
Install dependencies:

sh
Copy
Edit
pip install -r requirements.txt
Start the Flask server:

sh
Copy
Edit
python app/App.py
Open another terminal and send a request to generate test cases:

sh
Copy
Edit
curl -X POST http://127.0.0.1:5000/generateTests \
     -H "Content-Type: application/json" \
     -d '{"repoUrl": "https://github.com/example-user/sample-repo"}'
Running with Docker
Build the Docker image:

sh
Copy
Edit
docker build -t ai-test-generator .
Run the Docker container:

sh
Copy
Edit
docker run -p 5000:5000 ai-test-generator
