def calculate_score(results):

    safe_count = sum(1 for r in results if r["safe"])

    score = (safe_count / len(results)) * 10

    return round(score, 2)
