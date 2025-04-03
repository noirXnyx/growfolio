import requests #Python library used to make HTTP requests. This library simplifies the process
                # of sending HTTP requests to interact with web services (APIs) and retrieve data.

# Part C1 in the task.
# As specified in the task, this is the class that contains and encapsulate all the data and methods
# related to weather data for a specific location and date
class WeatherData:
    def __init__(self, latitude, longitude, date):
        self.latitude = latitude
        self.longitude = longitude
        self.date = date
        self.year = date.year
        self.month = date.month
        self.day = date.day
        self.avg_temp = None
        self.min_temp = None
        self.max_temp = None
        self.avg_wind_speed = None
        self.min_wind_speed = None
        self.max_wind_speed = None
        self.sum_precipitation = None
        self.min_precipitation = None
        self.max_precipitation = None
        self.data = None

    # This is a special method that returns a string representation of the object
    # When inspecting an object in an interactive session, Python calls the '__repr__'
    # This is useful for debugging and logging, as it shows the current state of the object's attributes
    # This is particularly useful in quickly understanding the data contained within the instance 'WeatherData'
    def __repr__(self):
        return (f"WeatherData({self.latitude}, {self.longitude}, {self.date}, "
                f"avg_temp={self.avg_temp}, min_temp={self.min_temp}, max_temp={self.max_temp}, "
                f"avg_wind_speed={self.avg_wind_speed}, min_wind_speed={self.min_wind_speed}, max_wind_speed={self.max_wind_speed}, "
                f"sum_precipitation={self.sum_precipitation}, min_precipitation={self.min_precipitation}, max_precipitation={self.max_precipitation})")

    # This part shows the method for fetching weather data for the specified location and date range
    # URL is directly copied from open meteo right after changing the location, timezone, and daily weather variables
    # In task part 2, it is specified that the data should be the most recent 5 years, so I made the start and end dates dynamic.
    def fetch_weather_data(self):
        start_date = (self.date.replace(year=self.date.year - 5)).strftime('%Y-%m-%d')
        end_date = self.date.strftime('%Y-%m-%d')
        url = (f"https://archive-api.open-meteo.com/v1/archive?"
               f"latitude={self.latitude}&longitude={self.longitude}&start_date={start_date}&end_date={end_date}"
               f"&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum,wind_speed_10m_max"
               f"&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York")

        # This is the GET request sent to the constructed URL. The URL is taken directly from open-meteo and edited.
        # Response's status code 200 indicates success, and the response is parsed as JSON and stored in the 'data' variable
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            # Processing the retrieved data.
            # This code calculates the average, minimum, maximum,and sum for the relevant weather parameters.
            # Mean = add up all the given values, then divide by how many values there are. This calculation
            # is the dame as getting the average. So, for ease of use, I am using avg all throughout.
            # Filter out None values before summing and averaging. 'None' values represent missing data
            temp_mean_values = [val for val in data['daily']['temperature_2m_mean'] if val is not None]
            temp_min_values = [val for val in data['daily']['temperature_2m_min'] if val is not None]
            temp_max_values = [val for val in data['daily']['temperature_2m_max'] if val is not None]
            wind_speed_values = [val for val in data['daily']['wind_speed_10m_max'] if val is not None]
            precipitation_values = [val for val in data['daily']['precipitation_sum'] if val is not None]

            # Calculate averages, min, and max while handling empty lists
            self.avg_temp = sum(temp_mean_values) / len(temp_mean_values) if temp_mean_values else None
            self.min_temp = min(temp_min_values) if temp_min_values else None
            self.max_temp = max(temp_max_values) if temp_max_values else None

            self.avg_wind_speed = sum(wind_speed_values) / len(wind_speed_values) if wind_speed_values else None
            self.min_wind_speed = min(wind_speed_values) if wind_speed_values else None
            self.max_wind_speed = max(wind_speed_values) if wind_speed_values else None

            self.sum_precipitation = sum(precipitation_values) if precipitation_values else None
            self.min_precipitation = min(precipitation_values) if precipitation_values else None
            self.max_precipitation = max(precipitation_values) if precipitation_values else None

        # This is for handling errors. If the API request fails (status code is not 200), an error message is
        # printed with the relevant status code
        else:
            print(f"Error fetching data: {response.status_code}")

# separate methods for part c2
    def fetch_mean_temperature(self):
        start_date = (self.date.replace(year=self.date.year - 5)).strftime('%Y-%m-%d')
        end_date = self.date.strftime('%Y-%m-%d')
        url = (f"https://archive-api.open-meteo.com/v1/archive?"
               f"latitude={self.latitude}&longitude={self.longitude}&start_date={start_date}&end_date={end_date}"
               f"&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum,wind_speed_10m_max"
               f"&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York")

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            temp_mean_values = [val for val in data['daily']['temperature_2m_mean'] if val is not None]
            self.avg_temp = sum(temp_mean_values) / len(temp_mean_values) if temp_mean_values else None
            print(f"Mean Temperature: {self.avg_temp} Fahrenheit")
        else:
            print(f"Error fetching mean temperature data: {response.status_code}")

    def fetch_max_wind_speed(self):
        start_date = (self.date.replace(year=self.date.year - 5)).strftime('%Y-%m-%d')
        end_date = self.date.strftime('%Y-%m-%d')
        url = (f"https://archive-api.open-meteo.com/v1/archive?"
               f"latitude={self.latitude}&longitude={self.longitude}&start_date={start_date}&end_date={end_date}"
               f"&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum,wind_speed_10m_max"
               f"&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York")

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            wind_speed_values = [val for val in data['daily']['wind_speed_10m_max'] if val is not None]
            self.max_wind_speed = max(wind_speed_values) if wind_speed_values else None
            print(f"Maximum Wind Speed: {self.max_wind_speed} mph")
        else:
            print(f"Error fetching maximum wind speed data: {response.status_code}")

    def fetch_precipitation_sum(self):
        start_date = (self.date.replace(year=self.date.year - 5)).strftime('%Y-%m-%d')
        end_date = self.date.strftime('%Y-%m-%d')
        url = (f"https://archive-api.open-meteo.com/v1/archive?"
               f"latitude={self.latitude}&longitude={self.longitude}&start_date={start_date}&end_date={end_date}"
               f"&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum,wind_speed_10m_max"
               f"&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York")

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            precipitation_values = [val for val in data['daily']['precipitation_sum'] if val is not None]
            self.sum_precipitation = sum(precipitation_values) if precipitation_values else None
            print(f"Sum Precipitation: {self.sum_precipitation} inch")
        else:
            print(f"Error fetching precipitation data: {response.status_code}")
