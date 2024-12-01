from django.shortcuts import render, reverse

from rest_framework.views import APIView
from rest_framework.response import  Response
from .models import video_link
from googleapiclient.discovery import build
import re
from .emotin_finder import get_emotion
from collections import Counter
from .Video_classifier import content_classifier


def home(request):
    return render(request, 'home.html')  # Ensure you have the home.html template


API_KEY = 'AIzaSyDDbwRlQb_9ifaoji_f0lfOMge08Sca04Q'  # API key 

# YouTube Data API v3 service
youtube = build('youtube', 'v3', developerKey=API_KEY)

class CommentData(APIView):
    def extract_video_id(self,youtube_link):
        # Improved regular expression pattern to match YouTube video IDs in URLs
        pattern = re.compile(
            r'(?:https?://)?(?:www\.)?(?:youtube\.com/.*?\?.*?v=|youtu\.be/|youtube\.com/embed/|youtube\.com/v/|youtube\.com/watch\?.*?v=|youtube\.com/live/)([a-zA-Z0-9_-]{11})')

        # Search for the pattern in the provided link
        match = pattern.search(youtube_link)

        # If a match is found, return the video ID, else return None
        return match.group(1) if match else None

    def get_video_comments(self,video_id):
        comments = []

        # Request comments for the specified video
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100  # Adjust as needed, maximum is 100 per request
        )

        # Iterate through each page of comments
        while request:
            response = request.execute()

            # Extract comments from the response
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
                comments.append(comment)

            # Check if there are more pages of comments
            request = youtube.commentThreads().list_next(request, response)

        return comments

    video_id = "hQwFeIupNP0"  # Replace with the actual video ID
    def post(self, request):
        comment_values=[]
        link = request.POST.get("link")
        content = request.POST.get("link")
        data=self.extract_video_id(link)
        comments = self.get_video_comments(data)
        comment_emotion = []
        for comment in comments:
            #we loop the comments to find out what kind of emotion it contains
            comment_emotion.append( get_emotion(comment))

        for value in comment_emotion:
            list1 = list(value.values())
            comment_values.append(list1[1])
            # comment_values.append[value["comment_value"]]
        result = dict(Counter(comment_values))

        video_link.objects.create(
            link = link,
            content = content,
            video_contents = result
        )
        return render(request,"video_result.html",{"status":True,"video_responses":result, "comments":comment_emotion})
class Video_data(APIView):
    def get(self, request):
        api_link = reverse("form")
        #if they want to post new video link redirecting them to that view
        videos_datas = video_link.objects.all().values()
        return render(request, "video_list_get.html", {"videos": videos_datas, "api":api_link})


#the form to get the video link:
def video_form(request):
    return render(request, "video_forms.html")