def calculate_average_rating(response):
    """Calculates the average survey rating for a respondent."""
    try:
        total = sum([response['service_quality'], response['communication'], response['value_for_money']])
        average = total / 3
        return average
    except KeyError as e:
        print(f"Missing data for {e}")
        return None



def process_survey_results(survey_data):
    """Processes survey data and categorizes responses."""
    results = []
    
    for response in survey_data:
        ratings = [response['service_quality'], response['communication'], response['value_for_money']]
        average = calculate_average_rating(response)
        
        if average is not None:
            category = categorize_feedback(round(average))  # Rounding to fit discrete categories
            response_results = {
                'respondent': response['respondent'],
                'service_quality': response['service_quality'],
                'communication': response['communication'],
                'value_for_money': response['value_for_money'],
                'average': average,
                'category': category
            }
            results.append(response_results)
    
    return results

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