# AI Test Case Generator

An AI-powered system that automatically generates unit test cases for Python, Java, and C++ code from a given GitHub repository. It uses a pre-trained CodeT5 model to analyze the source code and generate meaningful test cases.

## Usage

### Installation  
1. Clone this repository:
   
```git clone https://github.com/pibuilt/TestCrafter.git```

2. Install dependencies:

```pip install -r Requirements.txt```

3. Start Flask Server:
```python App/App.py```

4. Send a request to generate test cases:  
```sh
curl -X POST http://127.0.0.1:5000/generateTests \
     -H "Content-Type: application/json" \
     -d '{"repoUrl": "https://github.com/example-user/sample-repo"}'

