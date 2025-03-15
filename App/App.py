from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from GitHandler import cloneRepo, extractCodeFiles
from AiModel import generateTestCases
from TestRunner import saveAndRunTests

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AI Test Case Generator is Running!"

@app.route("/generateTests", methods=["POST"])
def generateTests():
    data = request.json
    repoUrl = data.get("repoUrl")

    if not repoUrl:
        return jsonify({"error": "GitHub repo URL is required"}), 400

    repoPath = "RepoCode"
    
    try:
        cloneRepo(repoUrl, repoPath)
        codeFiles = extractCodeFiles(repoPath)
    except Exception as e:
        return jsonify({"error": f"Failed to process repository: {str(e)}"}), 500

    response = []
    for fileName, sourceCode in codeFiles:
        lang = "Python" if fileName.endswith(".py") else "Java" if fileName.endswith(".java") else "C++"
        testCase = generateTestCases(sourceCode, lang)

        if fileName.endswith(".py"):
            saveAndRunTests(fileName, testCase)

        response.append({"file": fileName, "testCases": testCase})

    return jsonify({"testResults": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
