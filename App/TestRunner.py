import os

def saveAndRunTests(fileName, testCode):
    testFile = f"test_{fileName}"
    
    with open(testFile, "w", encoding="utf-8") as f:
        f.write(testCode)

    if fileName.endswith(".py"):
        print(f"Running tests for {fileName}...")
        os.system(f"python -m pytest {testFile} --maxfail=1 --disable-warnings")
    else:
        print(f"Skipping execution for {fileName} (Java/C++ execution not implemented).")
