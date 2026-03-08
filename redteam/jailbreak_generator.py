import json
import random


def generate_prompt():
    with open("prompts/jailbreak_prompts.json") as f:
        prompts = json.load(f)

    return random.choice(prompts)
