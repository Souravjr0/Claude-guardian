from evaluation.safety_score import calculate_score


def test_calculate_score_all_safe():
    results = [{"safe": True}, {"safe": True}, {"safe": True}]
    assert calculate_score(results) == 10.0


def test_calculate_score_partial_safe():
    results = [{"safe": True}, {"safe": False}, {"safe": True}]
    assert calculate_score(results) == 6.67
