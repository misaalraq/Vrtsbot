
import requests

def load_data(token):
    # Simulated function to load the data based on the token
    # You should replace this with your actual data loading logic
    return [
        # Example data loaded
        {"query_id": "AAESnJcbAAAAABKclxuQqiDl", "user": {"id": 462920722, "first_name": "Prometheus"}},
        {"query_id": "AAFTM6hnAAAAAFMzqGd_qRNa", "user": {"id": 1739076435, "first_name": "3"}}
    ]

def get_task(token):
    data = load_data(token)  # Assuming this function loads your data
    recommendations = []  # Initialize an empty list for recommendations
    
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                # Parse relevant fields from the dictionary in the list
                recommendations.append(item.get('query_id', 'Unknown Query ID'))
    elif isinstance(data, dict):
        recommendations = data.get('recommendations', {}).get('missions', [])
    else:
        # Handle unexpected formats
        print(f"Unexpected data format: {type(data)}")
        recommendations = []
    
    return recommendations

def main():
    token = "your_token_here"  # Replace with your actual token
    task_ids, task_titles = get_task(token)
    print(task_ids)

if __name__ == "__main__":
    main()
