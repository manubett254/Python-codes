
# Code 5: Weather Tracker

class WeatherTracker:
    def __init__(self):
        self.data = {}

    def add_weather(self, date, temp):
        self.data[date] = temp
        return f"Weather for {date} recorded: {temp}°C."

    def get_weather(self, date):
        return f"Weather on {date}: {self.data.get(date, 'No data available')}°C."

    def average_temperature(self):
        if not self.data:
            return "No data available to calculate average temperature."
        return f"Average Temperature: {sum(self.data.values()) / len(self.data):.2f}°C."

if __name__ == "__main__":
     # Test Weather Tracker
    tracker = WeatherTracker()
    tracker.add_weather("2025-01-20", 25)
    tracker.add_weather("2025-01-21", 28)
    print(tracker.average_temperature())