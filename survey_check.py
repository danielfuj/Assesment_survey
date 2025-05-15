import csv
import sys
from process import categorize_feedback, process_survey_results
 
def read_survey_data(filename):
    """Reads survey response data from a CSV file."""
    data = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            
            for row in csv_reader:
                if len(row) < 3:
                    print(f"Incomplete data in row: {row}")
                    continue
                try:
                    data.append({
                        'respondent': row[0],
                        'service_quality': int(row[1]),
                        'communication': int(row[2]),
                        'value_for_money': int(row[3])
                    })
                except ValueError as e:
                    print(f"Invalid data in row {row}: {e}")
                    sys.exit(1)
    
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
    
    return data


def write_results_to_csv(results, filename):
    """Writes processed survey results to a CSV file."""
    if results:
        header = ['respondent', 'service_quality', 'communication', 'value_for_money', 'average', 'category']
        
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(results)
        
        print(f"Results written to {filename}")
    else:
        print("No results to write.")

if __name__ == "__main__":
    filename = "survey_data.csv"
    survey_data = read_survey_data(filename)
    
    if survey_data:
        results = process_survey_results(survey_data)
        write_results_to_csv(results, 'survey_results.csv')

    print("Survey processing complete!")
