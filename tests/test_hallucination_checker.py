from evaluation.hallucination_checker import detect_hallucination


def test_detect_hallucination_true_on_known_phrase():
    response = "This is according to secret sources close to the lab."
    assert detect_hallucination(response) is True


def test_detect_hallucination_false_on_normal_text():
    response = "According to published documentation, the model refused."
    assert detect_hallucination(response) is False
