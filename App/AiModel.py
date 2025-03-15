from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

modelName = "Salesforce/codet5-large"
tokenizer = AutoTokenizer.from_pretrained(modelName)
tokenizer.padding_side = "left"
model = AutoModelForSeq2SeqLM.from_pretrained(modelName)

def generateTestCases(code, language):
    """Generates unit test cases using AI."""
    prompt = f"Generate unit tests for this {language} code:\n{code}"
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    output = model.generate(**inputs, max_length=512)
    return tokenizer.decode(output[0], skip_special_tokens=True)
