import json
import os
from datetime import datetime

def save_results(results, niche):
    """Save results to a JSON file with timestamp"""
    # Create results directory if it doesn't exist
    if not os.path.exists('results'):
        os.makedirs('results')
    
    # Format the data
    data = {
        'timestamp': datetime.now().isoformat(),
        'niche': niche,
        'results': str(results).strip()  # Ensure the results are properly stringified
    }
    
    # Save to file with proper formatting
    with open('results/latest_results.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write('\n')  # Add newline at end of file

def load_latest_results():
    """Load the most recent results"""
    try:
        if os.path.exists('results/latest_results.json'):
            with open('results/latest_results.json', 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading results: {e}")
        return None
    return None 