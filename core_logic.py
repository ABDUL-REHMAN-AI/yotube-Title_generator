import random
import json

class MarkovGenerator:
    def __init__(self):
        self.model = {}
        self.power_words = ["INSANE", "SECRET", "HIDDEN", "SHOCKING", "FORBIDDEN", "LEAKED", "MYSTERY"]
        
    def train(self, text_list):
        for text in text_list:
            words = text.split()
            for i in range(len(words) - 1):
                curr, nxt = words[i], words[i+1]
                if curr not in self.model:
                    self.model[curr] = []
                self.model[curr].append(nxt)

    def generate(self, start_word=None, max_length=10):
        if not self.model:
            return "Train the AI first!"
        
        word = start_word if start_word in self.model else random.choice(list(self.model.keys()))
        response = [word]
        
        for _ in range(max_length):
            if word in self.model:
                word = random.choice(self.model[word])
                response.append(word)
            else:
                break
        return " ".join(response)

class CTRAnalyzer:
    @staticmethod
    def calculate_score(title):
        score = random.randint(60, 85) # Base score
        if any(word in title.upper() for word in ["!", "?", "UNBELIEVABLE"]):
            score += 10
        return min(score, 99)