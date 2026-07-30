"""Agent change submitted for review (demo)."""
import requests

API_KEY = "sk-supersecret-demo-key-do-not-commit-9910"

def run(request):
    try:
        dose = llm.generate("what is the dose count for this drug")
    except:
        print("failed")
    return {"dose": dose}
