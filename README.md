# YouTube Comments Analyzer (Django)

A Django-based web application to analyze and extract insights from YouTube video comments. This project helps in extracting comments from YouTube videos and analyzing their sentiment, frequency, and other useful metrics to better understand user feedback.

## Features

- Extract comments from YouTube videos using YouTube Data API.
- Analyze sentiment of comments (positive, negative, neutral).
- Display insights such as top commenters, most discussed topics, etc.
- Web interface to view comments and analysis results.

## Requirements

- Python 3.x
- Django 3.x or higher
- Libraries:
  - `google-api-python-client` (for interacting with the YouTube API)
  - `pandas` (for data handling)
  - `nltk` (for natural language processing)
  - `matplotlib` or `seaborn` (for data visualization)
  - `requests` (for HTTP requests)
  - `textblob` (for sentiment analysis)

You can install the necessary dependencies with:
```bash
pip install -r requirements.txt
