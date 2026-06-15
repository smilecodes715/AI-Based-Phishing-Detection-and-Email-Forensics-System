def detect_phishing(email):

    suspicious_words = [
        "urgent",
        "verify",
        "password",
        "bank",
        "click"
    ]

    score = 0

    for word in suspicious_words:
        if word.lower() in email.lower():
            score += 1

    if score >= 2:
        return "Potential Phishing Email"

    return "Safe Email"

sample = "Verify your bank account urgently"

print(detect_phishing(sample))
