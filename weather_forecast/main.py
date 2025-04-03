
#Importing 'datetime' class from 'datetime' module, which is used to work with dates and times.
from datetime import datetime

# insert_weather_data: function for inserting weather data into a db
# weather record - class: representing the weather data table in the db
# recreate_table - function: drops an existing weather data table and recreates it/ensures it exists
from database import insert_weather_data, recreate_table, query_weather_data
# importing the weatherdata class from weather_data  file.
from weather_data import WeatherData


# Importing 'sessionmaker' class from sqlalchemy, which is a factory for creating new 'Session' objects.
# Session objects are sued to manage database transactions.

# This function put together the process of retrieving weather data for a specific location and date, printing the data,
# ensuring the database table is correctly set up, and then inserting the retrieved data into the db
def main():
    latitude = 40.0806
    longitude = -80.9001
    today = datetime.today()

    # An instance of the 'WeatherData' class is created using lat, long, current date
    weather = WeatherData(latitude, longitude, today)

    # The 'fetch_weather_data()' method is called on this instance to retrieve the weather data for the location
    # and date range, most recent 5 years
    weather.fetch_weather_data()

    # Generating the 3 weather variables in part c2
    print("\nWeather Variables Asked in Part C2:")
    weather.fetch_mean_temperature()
    weather.fetch_max_wind_speed()
    weather.fetch_precipitation_sum()

    # This prints the 'WeatherData' object, which uses the '__repr__' method of the 'WeatherData'
    # Generating the raw data return from the API url. This is helpful in checking if the table has the correct data
    # Compare these raw data to the printed/generated query right below this information
    # Raw data line starts with WeatherData, query line starts with ID
    print("\nAll raw weather data from API (use this to verify if data inserted are correct):")
    print(weather)

    # recreate_table is called to ensure that the db table for weather data exists, and reset it daily
    # this function returns an 'engine' object which is the sqlalchemy connection to the db
    engine = recreate_table()

    # This is called to insert the weather data fetched by the 'WeatherData' object into the db.
    # The 'engine' is passed to connect to the appropriate db
    insert_weather_data(engine, weather)

    # Query the database to verify data insertion
    print("\nAll records inserted in the database:")
    query_weather_data(engine)

main()