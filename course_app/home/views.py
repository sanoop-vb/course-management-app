from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render


def course_list(request):
    with open('home/data/get_all_courses_API_response.json') as f:
        courses = json.load(f)
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, course_id):
    # Load the course detail JSON file
    with open('home/data/get_course_detail_API_response.json') as f:
        course_details = json.load(f)

    # Assuming course_details contains the correct course details
    # Find the course by ID

    if str(course_id) == str(course_details["course_id"]):

        videos = course_details["videos"]

        # Add embed URL to each video
        for video in videos:
            video_id = video['youtube_url'].split('=')[1]  # Extract video ID and any other params
            video['embed_url'] = video_id.split('&')[0]  # Remove any query parameters after the video ID


        return render(request, 'courses/course_detail.html', {
            'course_id': course_id,
            'videos': videos,

        })
    else:
        return render(request, 'courses/404.html')  # Or handle as needed


