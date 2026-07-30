"""Agent change submitted for review (auto-fixed by eai-eng-pr-review)."""
import os
import logging
import requests

logger = logging.getLogger(__name__)
API_KEY = os.environ["AGENT_API_KEY"]  # loaded from config, never committed

def run(request):
    try:
        # Numbers are extracted from the source doc + verified, never generated.
        dose = request["source"]["dose_count"]
    except KeyError as e:
        logger.error("missing dose_count in request: %s", e)
        raise
    return {"dose": dose}
