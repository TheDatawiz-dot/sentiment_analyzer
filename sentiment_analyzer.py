from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text.

    Args:
        text: The string to be analyzed.

    Returns:
        A string indicating the sentiment (Positive, Negative, or Neutral).
    """
    analysis = TextBlob(text)
    
    # Classify the polarity of the text
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == '__main__':
    print("Welcome to the Sentiment Analyzer!")
    print("Enter a sentence to analyze its sentiment, or type 'quit' to exit.")

    while True:
        user_input = input("> ")
        if user_input.lower() == 'quit':
            break
        
        sentiment = analyze_sentiment(user_input)
        print(f"Sentiment: {sentiment}")
