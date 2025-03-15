# AI Test Case Generator

An AI-powered system that generates unit test cases for Python, Java, and C++ code from a given GitHub repository. It uses a pre-trained CodeT5 model to analyze the source code and generate test cases.

## Usage

### Installation  
1. Clone this repository:
   
```sh
git clone https://github.com/pibuilt/TestCrafter.git
cd TestCrafter/
```
2. Install dependencies:

```sh
pip install -r Requirements.txt
```

### Running Locally
1. Start Flask Server:

```sh
python App/App.py
```

2. Send a request to generate test cases:
   
```sh
curl -X POST http://127.0.0.1:5000/generateTests \
     -H "Content-Type: application/json" \
     -d '{"repoUrl": "https://github.com/example-user/sample-repo"}'
```

### Running with Docker
1. Build the Docker Image:

```sh
docker build -t TestCrafter .
```

2. Run the Docker Container:

```sh
docker run -p 5000:5000 TestCrafter
```

3. Sending API Request:

```sh
curl -X POST http://127.0.0.1:5000/generateTests \
     -H "Content-Type: application/json" \
     -d '{"repoUrl": "https://github.com/example-user/sample-repo"}'
```

