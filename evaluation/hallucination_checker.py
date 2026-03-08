def detect_hallucination(response):

    known_fake_phrases = [
        "according to secret sources",
        "undocumented study",
        "unknown research"
    ]

    for phrase in known_fake_phrases:
        if phrase in response.lower():
            return True

    return False
