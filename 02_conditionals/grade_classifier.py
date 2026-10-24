"""Classify a score (0 to 100) into a letter grade."""


def classify_score(score):
    """Return a letter grade using the Nigerian university scale."""
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    return "F"


if __name__ == "__main__":
    print(classify_score(int(input("Enter score: "))))
