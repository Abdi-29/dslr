import math

class Feature:
    def __init__(self, name, values):
        self.name = name
        self.values = [v for v in values if v is not None]
        self.count = len(self.values)

    def calculate_mean(self):
        return sum(self.values) / self.count if self.count > 0 else 0

    def calculate_std(self):
        if self.count <= 1:
            return 0
        mean = self.calculate_mean()
        variance = sum((x - mean) ** 2 for x in self.values) / self.count
        return math.sqrt(variance)

    def calculate_min(self):
        return min(self.values) if self.values else None

    def calculate_max(self):
        return max(self.values) if self.values else None

    def calculate_percentile(self, percentile):
        if not self.values:
            return None
        sorted_values = sorted(self.values)
        index = int((percentile / 100) * (self.count - 1))
        return sorted_values[index]

    def calculate_statistics(self):
        mean = self.calculate_mean()
        std = self.calculate_std()
        min_val = self.calculate_min()
        max_val = self.calculate_max()
        p25 = self.calculate_percentile(25)
        p50 = self.calculate_percentile(50)
        p75 = self.calculate_percentile(75)

        return {
            "Count": self.count,
            "Mean": mean,
            "Std": std,
            "Min": min_val,
            "25%": p25,
            "50%": p50,
            "75%": p75,
            "Max": max_val
        }
