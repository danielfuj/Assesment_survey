def categorize_feedback(score):
    """Categorizes survey feedback based on the average rating."""
    if score == 5:
        return "Very Good"
    elif score == 4:
        return "Good"
    elif score == 3:
        return "Neutral"
    elif score == 2:
        return "Bad"
    else:
        return "Really Bad"