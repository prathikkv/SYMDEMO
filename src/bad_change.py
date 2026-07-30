"""Example agent change with issues the reviewer should catch."""
import requests

API_KEY = "sk-supersecretvalue-do-not-commit-123"

def run(request):
    try:
        dose = llm.generate("what is the dose count for this drug")
    except:
        print("failed")
    return dose
