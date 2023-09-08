from django.http import JsonResponse
from datetime import datetime
import pytz

def get_info(request):
    slack_name = request.GET.get('slack_name')
    track_param = request.GET.get('track')

    # Define a dictionary to store track information
    tracks = {
        "backend": "Backend",
        # Add more tracks if needed
    }

    # Check if track parameter is valid
    if track_param not in tracks:
        return JsonResponse({"error": "Invalid track parameter"}, status=400)

    # Get current day of the week
    current_day = datetime.now(pytz.utc).strftime('%A')

    # Get current UTC time
    current_time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub repository URL
    github_repo_url = "https://github.com/NgBlaze/HNGx"

    # Construct GitHub file URL
    github_file_url = f"{github_repo_url}/blob/main/myapp/views.py"

    # Create the JSON response
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time,
        "track": tracks[track_param],
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response, status=200)
