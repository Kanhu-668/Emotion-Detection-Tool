from collections import Counter

# Optional: Uncomment below lines if nltk is installed
# import nltk
# from nltk.corpus import stopwords
# nltk.download('stopwords')

def preprocess_text(text):
    """Clean and tokenize input text."""
    text = text.lower().strip()
    words = text.split()
    
    # Optional: Remove stopwords (if nltk available)
    # stop_words = set(stopwords.words('english'))
    # words = [word for word in words if word not in stop_words]
    
    return words


def detect_emotion(sentence):
    """Detect the dominant emotion from input text."""
    emotion_keywords = {
        "joy": ["happy", "joy", "smile", "glad", "delight", "excited"],
        "sadness": ["sad", "cry", "unhappy", "down", "depressed"],
        "anger": ["angry", "mad", "furious", "rage", "annoyed"],
        "fear": ["afraid", "scared", "fear", "terrified", "nervous"],
        "love": ["love", "adore", "care", "affection", "romantic"]
    }

    emojis = {
        "joy": "😊",
        "sadness": "😢",
        "anger": "😠",
        "fear": "😨",
        "love": "❤️"
    }

    words = preprocess_text(sentence)
    emotion_count = Counter()

    for word in words:
        for emotion, keywords in emotion_keywords.items():
            if word in keywords:
                emotion_count[emotion] += 1

    if not emotion_count:
        return "No clear emotion detected 🤔"

    dominant_emotion = emotion_count.most_common(1)[0][0]
    emoji = emojis.get(dominant_emotion, "")
    return f"Detected Emotion: {dominant_emotion.capitalize()} {emoji}"


def main():
    print("Welcome to the Emotion Detection Tool! 🎭")
    print("Type 'exit' to quit.\n")

    while True:
        sentence = input("Enter a sentence describing your feeling: ").strip()
        if sentence.lower() == "exit":
            print("Goodbye! Take care! 👋")
            break

        result = detect_emotion(sentence)
        print(result)
        print()


if __name__ == "__main__":
    main()
