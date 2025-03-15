import os

def saveAndRunTests(fileName, testCode):
    """Saves the generated test case and runs it for Python files."""
    if fileName.endswith(".py"):
        testFile = f"test_{fileName}"
        with open(testFile, "w", encoding="utf-8") as f:
            f.write(testCode)

        print(f"Running tests for {fileName}...")
        os.system(f"pytest {testFile} --maxfail=1 --disable-warnings")
    else:
        print(f"Skipping execution for {fileName} (Java/C++ not supported).")
