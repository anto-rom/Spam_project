def calculate_spam_score(email):
    score = 0

    # Subject pattern
    if match_pattern(email["subject"], "marketing_spam"):
        score += 30

    # Phishing
    if match_pattern(email["subject"], "phishing_keywords"):
        score += 40

    # Domain
    if match_pattern(email["email"], "suspicious_domains"):
        score += 20

    # Low quality
    if len(email["subject"]) < 5:
        score += 10

    return score


def classify(score):
    if score >= 70:
        return "AUTO_CLOSE"
    elif score >= 40:
        return "REVIEW"
    else:
        return "ALLOW"
