import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.tokenizer = nltk.tokenize.TweetTokenizer()
        self.positive = set()
        self.negatives = set()
        file = open(positives, "r")
        file1 = open(negatives, "r")
        
        for line in file:
            if not line.startswith((";", " ")):
                self.positive.add(line.rstrip("\n"))
        file.close()
        
        for line in file1:
            if not line.startswith((";", " ")):
                self.negatives.add(line.rstrip("\n"))
        file1.close()
        
        

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokens = self.tokenizer.tokenize(text)
        sum = 0
        for token in tokens:
            if token.lower() in self.positive:
                sum += 1
            elif token.lower() in self.negatives:
                sum -=1
        return sum
