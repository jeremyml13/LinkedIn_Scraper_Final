from collections import Counter

# simple list of English stopwords
stopwords = set([
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers",
    "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves",
    "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are",
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does",
    "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until",
    "while", "of", "at", "by", "for", "with", "about", "against", "between", "into",
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down",
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here",
    "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more",
    "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
    "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"
])

# Given a body of text, returns the most used word that is not a stopword
def most_used_word(text):
    # Tokenize the text
    words = text.lower().split()

    # Filter out stopwords and non-alphabetic characters
    filtered_words = [word.strip('.,!?;()[]{}"\'') for word in words if word.strip('.,!?;()[]{}"\'') not in stopwords and word.isalpha()]

    # Count word frequencies
    word_counts = Counter(filtered_words)

    # Find the word with the highest frequency
    most_used = word_counts.most_common(1)
    if most_used:
        return most_used[0][0]  # Return the word
    else:
        return None  # Return None if no suitable word is found

# Example usage
#text = "Hello world! Welcome to the world of programming. Programming is fun."
#print(most_used_word(text))
