from textblob import TextBlob

import re


def remove_emojis(text):
    # Define a regular expression pattern to match emojis
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F700-\U0001F77F"  # alchemical symbols
                               u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                               u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                               u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                               u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                               u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                               u"\U00002702-\U000027B0"  # Dingbats
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)

    # Use sub() method to replace emojis with an empty string
    clean_text = emoji_pattern.sub(r'', text)


    return clean_text

def get_emotion(texts):
    text = remove_emojis(texts)
    # Create a TextBlob object
    blob = TextBlob(text)
    result_dictionary= {}
    # Get sentiment polarity
    sentiment_polarity = blob.sentiment.polarity

    # Define emotion categories based on sentiment polarity
    if sentiment_polarity > 0.2:
        result_dictionary["comment_desc"] = texts
        result_dictionary["emotion"] = "Positive"
        result_dictionary["comment_value"] = 1
        return result_dictionary
    elif sentiment_polarity < -0.2:
        result_dictionary["comment_desc"] = texts
        result_dictionary["emotion"] = "Negative"
        result_dictionary["comment_value"] = -1
        return result_dictionary
    else:
        result_dictionary["comment_desc"] = texts
        result_dictionary["emotion"] = "Neutral"
        result_dictionary["comment_value"] = 0
        return result_dictionary
























'''
positive = ["joy","happy","delightful","pleased","ecstatic","cheerful",
            "jubilant","satisfied","Positive Adjectives","positive","excellent",
            "great","fantastic","wonderful","amazing","superb","outstanding",
            "fabulous","Success","Achievement","success","achieve","accomplishment",
            "triumph","victory","thriving","successful","Good Experiences","good","excellent",
            "wonderful","fantastic","amazing","fabulous","awesome","Gratitude","thank you",
            "grateful","appreciation","thankful","Positive Emotions","love","joy","excitement",
            "happiness","satisfaction","bliss","contentment","Optimism","optimistic",
            "hopeful","positive outlook","bright future","Encouragement","encourage","supportive",
            "uplifting","motivational","Well-being","well-being","health","thriving","flourishing",
            "Satisfaction","satisfied","content","fulfilled","pleased"]
negative = ['unsuccessful', 'defeat', 'disappointment', 'setback', 'Fear', 'and', 'Anxiety',
            'fear', 'anxious', 'worried', 'uneasy', 'apprehensive', 'nervous', 'terrified',
            'Anger', 'anger', 'rage', 'fury', 'wrath', 'indignation', 'hostility', 'Pain',
            'Suffering', 'pain', 'suffer', 'agony', 'torment', 'misery', 'distress', 'Negative',
            'Adjectives', 'negative', 'bad', 'terrible', 'awful', 'dreadful', 'horrible', 'miserable',
            'Regret', 'regret', 'remorse', 'sorry', 'repentant', 'Discontent', 'discontent',
            'dissatisfaction', 'displeasure', 'discontented', 'Sadness', 'sad', 'unhappy',
            'disheartened', 'sorrowful', 'melancholy', 'gloomy', 'forlorn', 'Disapproval',
            'dislike', 'disapprove', 'hate', 'loathe', 'detest', 'despise', 'Frustration',
            'frustrated', 'annoyed', 'irritated', 'agitated', 'upset', 'angered', 'infuriated',
            'Failure', 'Setback', 'failure']

neutrals = ['neutral', 'indifferent', 'unbiased', 'objective', 'impartial', 'neither', 'good', 'nor',
            'bad', 'General', 'Statements', 'statement', 'fact', 'information', 'data', 'details',
            'Descriptive', 'Terms:', 'normal', 'average', 'standard', 'typical', 'ordinary',
            'Non-Emotional', 'Adjectives', 'neutral', 'mild', 'moderate', 'unremarkable', 'uneventful',
            'Factual', 'Language:', 'fact', 'evidence', 'observation', 'reality', 'Non-Opinionated',
            'Phrases:', 'it', 'is', 'what', 'it', 'is', 'as', 'it', 'stands', 'matter', 'of', 'fact',
            'without', 'bias', 'without', 'emotion', 'Objective', 'Language:', 'objective', 'unbiased',
            'impartial', 'unemotional', 'factual', 'Informative', 'Statements', 'information', 'data',
            'details', 'explanation', 'Commonplace', 'Terms:', 'usual', 'routine', 'commonplace',
            'ordinary', 'Balanced', 'Statements', 'balanced', 'even-handed', 'fair', 'equitable']


def analyze_sentiment(text):

    # Determine the sentiment category
    result_dictionary={}
    for words in text.split():
        # Convert the string and list elements to lowercase for case-insensitive comparison
        lowercase_string = words.lower()
        lowercase_positive = [item.lower() for item in positive]
        lowercase_negative = [item.lower() for item in negative]
        lowercase_neutral = [item.lower() for item in neutrals]

        if lowercase_string in lowercase_positive:
            result_dictionary["comment_desc"] = text
            result_dictionary["emotion"] = "Positive"
            result_dictionary["comment_value"]=1
            #we have to break it here because each comment one emotion is enough we dont have to loop all words of a comment
            break
        elif lowercase_string in lowercase_negative:
            result_dictionary["comment_desc"] = text
            result_dictionary["emotion"] = "Negative"
            result_dictionary["comment_value"]=-1
            break
        elif lowercase_string in lowercase_neutral:
            result_dictionary["comment_desc"] = text
            result_dictionary["emotion"] = "Neutral"
            result_dictionary["comment_value"]=0
            break
        else:
            result_dictionary["comment_desc"] = text
            result_dictionary["emotion"] = "No Emotions"
            result_dictionary["comment_value"]=None
            break
    # Return the results
    return result_dictionary


# # Example usage:
# text_to_analyze = "I love using this product. It's amazing!"
# result = analyze_sentiment(text_to_analyze)
#
# # Print the results
#
# print("Sentiment Category:", result["sentiment_category"])
'''
